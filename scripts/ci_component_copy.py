"""Check component-copy behavior in a hosted native editor; this is not Room acceptance."""

from __future__ import annotations

import json
import os
from pathlib import Path
import socket
import subprocess
import sys
import time


class NativeEditor:
    def __init__(self, executable: Path, output: Path):
        with socket.socket() as probe:
            probe.bind(("127.0.0.1", 0))
            port = probe.getsockname()[1]
        self.output = output
        self.log = (output / "native.log").open("wb")
        self.process = subprocess.Popen(
            [str(executable), "--control", str(port)], stdout=self.log, stderr=subprocess.STDOUT
        )
        self.connection = None
        self.stream = None
        self.next_id = 0
        try:
            for _ in range(60):
                if self.process.poll() is not None:
                    raise RuntimeError(f"native editor exited: {self.process.returncode}")
                try:
                    self.connection = socket.create_connection(("127.0.0.1", port), timeout=2)
                    self.connection.settimeout(65)
                    self.stream = self.connection.makefile("rwb")
                    self.call("ui.inspect")
                    break
                except (ConnectionError, OSError, TimeoutError):
                    self.disconnect()
                    time.sleep(1)
            else:
                raise RuntimeError("native editor did not become ready")
        except BaseException:
            self.close()
            raise

    def call(self, method: str, params: dict | None = None):
        request_id = self.next_id
        self.next_id += 1
        request = {"id": request_id, "method": method, "params": params or {}}
        self.stream.write((json.dumps(request) + "\n").encode())
        self.stream.flush()
        reply = json.loads(self.stream.readline())
        if reply.get("id") != request_id or not reply.get("ok"):
            raise RuntimeError(f"{method}: {reply}")
        return reply["result"]

    def command(self, command: str, params: dict | None = None):
        return self.call("engine.execute", {"command": command, "params": params or {}})

    def node(self, node_id: int, depth: int = 1):
        return self.call("node.get", {"id": node_id, "depth": depth})

    def disconnect(self):
        if self.stream is not None:
            self.stream.close()
            self.stream = None
        if self.connection is not None:
            self.connection.close()
            self.connection = None

    def close(self):
        self.disconnect()
        if self.process.poll() is None:
            self.process.terminate()
            try:
                self.process.wait(timeout=10)
            except subprocess.TimeoutExpired:
                self.process.kill()
                self.process.wait(timeout=10)
        self.log.close()


def verify(editor: NativeEditor) -> dict:
    editor.command("file.new", {"name": "Hosted component copy acceptance"})
    editor.call("ui.set", {"home": False, "focusRegion": "canvas"})
    frame = editor.command(
        "frame.create", {"x": 0, "y": 0, "width": 100, "height": 100, "name": "Tile"}
    )["id"]
    main = editor.command("component.create", {"ids": [frame]})["id"]
    before = editor.call("document.inspect")
    key = editor.call("ui.key", {"key": "D", "cmd": True})
    assert key["command"] == "edit.duplicate", key
    duplicate_id, = editor.call("document.inspect")["selection"]
    duplicate = editor.node(duplicate_id)
    assert duplicate["type"] == "INSTANCE" and duplicate["mainComponent"] == main, duplicate
    assert duplicate["name"] == "Tile" and duplicate["x"] == 200, duplicate
    editor.command("edit.undo")
    assert editor.node(duplicate_id) is None
    assert editor.call("document.inspect")["pages"] == before["pages"]
    editor.command("edit.redo")
    assert editor.node(duplicate_id) == duplicate

    editor.command("select.set", {"ids": [main]})
    before_drag = editor.call("document.inspect")
    dragged = editor.call("ui.pointer", {"kind": "drag", "x": 50, "y": 50, "to": [50, 250], "alt": True})
    dragged_id, = dragged["selection"]
    instance = editor.node(dragged_id)
    assert instance["type"] == "INSTANCE" and instance["mainComponent"] == main, instance
    assert (instance["x"], instance["y"]) == (0, 200), instance
    assert editor.node(main)["x"] == 0 and editor.node(main)["y"] == 0
    after_drag = editor.call("document.inspect")
    assert len(after_drag["history"]["undo"]) == len(before_drag["history"]["undo"]) + 1
    editor.command("edit.undo")
    assert editor.node(dragged_id) is None
    assert editor.call("document.inspect")["pages"] == before_drag["pages"]
    editor.command("edit.redo")
    assert editor.node(dragged_id) == instance

    editor.command("node.set", {"id": main, "props": {"fill": "#123456"}})
    main_fills = editor.node(main)["fills"]
    assert editor.node(duplicate_id)["fills"] == main_fills
    assert editor.node(dragged_id)["fills"] == main_fills

    variants = []
    for x, state in [(400, "Default"), (600, "Hover")]:
        frame = editor.command(
            "frame.create", {"x": x, "y": 0, "width": 100, "height": 100, "name": f"State={state}"}
        )["id"]
        variants.append(editor.command("component.create", {"ids": [frame]})["id"])
    variant_set = editor.command("component.combineVariants", {"ids": variants})["id"]
    copy = editor.command("edit.duplicate", {"ids": [variants[1]]})["ids"][0]
    assert editor.node(copy)["type"] == "COMPONENT"
    assert len(editor.node(variant_set)["children"]) == 3

    document = editor.output / "component-copy.figcraft"
    editor.command("file.saveAs", {"path": str(document)})
    assert document.stat().st_size > 100
    editor.command("view.zoomFit")
    screenshot = editor.output / "component-copy.png"
    editor.call("ui.screenshot", {"path": str(screenshot)})
    assert screenshot.stat().st_size > 1000
    return {
        "environment": "GitHub-hosted native Windows; not Room acceptance",
        "head": subprocess.check_output(["git", "rev-parse", "HEAD"], text=True).strip(),
        "workflowSha": os.environ.get("GITHUB_SHA"),
        "main": main,
        "duplicate": duplicate,
        "altDrag": instance,
        "linkedFill": main_fills,
        "variantSet": variant_set,
        "newVariant": copy,
        "checks": ["Duplicate shortcut", "Alt-drag", "linked updates", "variant duplication", "undo/redo"],
    }


def main():
    executable, output = (Path(arg).resolve() for arg in sys.argv[1:])
    output.mkdir(parents=True, exist_ok=True)
    assert executable.is_file(), executable
    editor = NativeEditor(executable, output)
    try:
        report = verify(editor)
        (output / "verification.json").write_text(json.dumps(report, indent=2), encoding="utf-8")
        print(json.dumps(report, indent=2))
    finally:
        editor.close()


if __name__ == "__main__":
    main()
