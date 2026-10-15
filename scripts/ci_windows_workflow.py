"""Windows CLI document round trip and export checks using synthetic inputs."""

from __future__ import annotations

import json
from pathlib import Path
import struct
import subprocess
import sys
from xml.etree import ElementTree

from pypdf import PdfReader


CLI = Path(sys.argv[1]).resolve()
OUT = Path(sys.argv[2]).resolve()
OUT.mkdir(parents=True, exist_ok=True)


def run(*args: str) -> str:
    command = [str(CLI), *args]
    result = subprocess.run(command, text=True, capture_output=True, timeout=180, check=False)
    if result.returncode:
        raise RuntimeError(f"{command!r} failed ({result.returncode}):\n{result.stdout}\n{result.stderr}")
    return result.stdout


def png(path: Path) -> tuple[int, int]:
    data = path.read_bytes()
    assert data.startswith(b"\x89PNG\r\n\x1a\n") and data[12:16] == b"IHDR", path
    assert len(data) > 1000, path
    return struct.unpack(">II", data[16:24])


assert run("--version").startswith("FigStrike ")
source = OUT / "created.figcraft"
commands = run("run", ".github/figstrike-smoke.json", "--out", str(source))
steps = [json.loads(line) for line in commands.splitlines()]
assert len(steps) == 3 and all(step["ok"] for step in steps), steps
assert source.stat().st_size > 100
info = json.loads(run("info", str(source), "--json"))
assert info["nodes"] >= 3
assert any(frame["name"] == "Welcome" for page in info["pages"] for frame in page["frames"])

exported = {}
for suffix in ("png", "svg", "pdf"):
    path = OUT / f"created.{suffix}"
    run("export", str(source), "-o", str(path))
    assert path.stat().st_size > 1000
    exported[suffix] = path.stat().st_size
assert all(side >= 300 for side in png(OUT / "created.png"))
assert ElementTree.parse(OUT / "created.svg").getroot().tag.endswith("svg")
reader = PdfReader(str(OUT / "created.pdf"))
assert len(reader.pages) >= 1
assert "Hello from FigStrike" in " ".join(page.extract_text() or "" for page in reader.pages)

sample = json.loads(run("info", "examples/ridgeline-app.figcraft", "--json"))
assert sample["nodes"] > 300 and sample["variables"] >= 10, sample
run("export", "examples/ridgeline-app.figcraft", "-o", str(OUT / "ridgeline.png"))
assert all(side >= 500 for side in png(OUT / "ridgeline.png"))

report = {
    "platform": "windows-2025",
    "created_nodes": info["nodes"],
    "created_pages": len(info["pages"]),
    "export_bytes": exported,
    "pdf_pages": len(reader.pages),
    "pdf_selectable_text": True,
    "sample_nodes": sample["nodes"],
    "sample_variables": sample["variables"],
}
(OUT / "verification.json").write_text(json.dumps(report, indent=2), encoding="utf-8")
print(json.dumps(report, indent=2))
