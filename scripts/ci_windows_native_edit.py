"""Exercise a real FigStrike desktop session, keyboard edit, save, and reopen."""

from __future__ import annotations

import json
from pathlib import Path
import socket
import subprocess
import sys
import time


APP = Path(sys.argv[1]).resolve()
OUT = Path(sys.argv[2]).resolve()
OUT.mkdir(parents=True, exist_ok=True)
DOCUMENT = OUT / "native-edited.figcraft"
SCREENSHOT = OUT / "native-edited.png"


def free_port() -> int:
    with socket.socket() as probe:
        probe.bind(("127.0.0.1", 0))
        return int(probe.getsockname()[1])


class Desktop:
    def __init__(self, project: Path | None, log_name: str):
        self.port = free_port()
        self.log = (OUT / log_name).open("wb")
        argv = [str(APP), "--control", str(self.port)]
        if project is not None:
            argv.append(str(project))
        self.process = subprocess.Popen(argv, stdout=self.log, stderr=subprocess.STDOUT)
        self.socket: socket.socket | None = None
        self.stream = None
        for _ in range(60):
            if self.process.poll() is not None:
                raise RuntimeError(f"native editor exited during startup: {self.process.returncode}")
            try:
                self.socket = socket.create_connection(("127.0.0.1", self.port), timeout=2)
                self.socket.settimeout(65)
                self.stream = self.socket.makefile("rwb")
                self.call("ui.inspect")
                break
            except (ConnectionError, OSError, TimeoutError):
                if self.stream is not None:
                    self.stream.close()
                    self.stream = None
                if self.socket is not None:
                    self.socket.close()
                    self.socket = None
                time.sleep(1)
        else:
            raise RuntimeError("native editor control channel did not become ready")
        self.next_id = 1

    def call(self, method: str, params: dict | None = None):
        assert self.stream is not None
        request_id = getattr(self, "next_id", 0)
        self.next_id = request_id + 1
        self.stream.write((json.dumps({"id": request_id, "method": method, "params": params or {}}) + "\n").encode())
        self.stream.flush()
        line = self.stream.readline()
        if not line:
            raise RuntimeError(f"native editor closed control channel during {method}")
        reply = json.loads(line)
        if reply.get("id") != request_id or not reply.get("ok"):
            raise RuntimeError(f"{method}: {reply}")
        return reply["result"]

    def command(self, name: str, params: dict | None = None):
        return self.call("engine.execute", {"command": name, "params": params or {}})

    def close(self):
        if self.stream is not None:
            self.stream.close()
        if self.socket is not None:
            self.socket.close()
        if self.process.poll() is None:
            self.process.terminate()
            try:
                self.process.wait(timeout=10)
            except subprocess.TimeoutExpired:
                self.process.kill()
                self.process.wait(timeout=10)
        self.log.close()


assert APP.is_file(), APP
desktop = Desktop(None, "native-first-launch.log")
try:
    desktop.command("file.new", {"name": "Windows native edit proof"})
    desktop.call("ui.set", {"home": False, "focusRegion": "canvas"})
    frame_id = desktop.command("frame.create", {"x": 0, "y": 0, "width": 640, "height": 420, "name": "Proof frame"})["id"]
    rect_id = desktop.command(
        "shape.rectangle",
        {"parent": frame_id, "x": 50, "y": 60, "width": 140, "height": 90, "name": "Keyboard-nudged rectangle"},
    )["id"]
    before = desktop.call("node.get", {"id": rect_id})
    assert before["x"] == 50 and before["y"] == 60 and before["width"] == 140, before
    # This goes through the native UI shortcut handler and current canvas selection.
    desktop.call("ui.key", {"key": "ArrowRight"})
    edited = desktop.call("node.get", {"id": rect_id})
    assert edited["x"] > before["x"] and edited["y"] == before["y"], (before, edited)
    saved = desktop.command("file.saveAs", {"path": str(DOCUMENT)})
    assert DOCUMENT.is_file() and saved["bytes"] == DOCUMENT.stat().st_size, saved
finally:
    desktop.close()

reopened = Desktop(DOCUMENT, "native-reopen.log")
try:
    restored = reopened.call("node.get", {"id": rect_id})
    assert restored["name"] == edited["name"], (edited, restored)
    for key in ("x", "y", "width", "height"):
        assert restored[key] == edited[key], (key, edited, restored)
    ui = reopened.call("ui.inspect")
    assert ui, "the reopened native editor did not provide UI state"
    shot = reopened.call("ui.screenshot", {"path": str(SCREENSHOT)})
    assert SCREENSHOT.is_file() and SCREENSHOT.stat().st_size > 1000, shot
    report = {
        "platform": "windows-2025",
        "method": "native desktop control channel with UI keyboard shortcut",
        "file": DOCUMENT.name,
        "fileBytes": DOCUMENT.stat().st_size,
        "frameId": frame_id,
        "rectangleId": rect_id,
        "before": before,
        "edited": edited,
        "reopened": restored,
        "screenshot": {"width": shot["width"], "height": shot["height"], "bytes": SCREENSHOT.stat().st_size},
    }
    (OUT / "native-edit-verification.json").write_text(json.dumps(report, indent=2), encoding="utf-8")
    print(json.dumps(report, indent=2))
finally:
    reopened.close()
