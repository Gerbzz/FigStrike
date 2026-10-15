# FigStrike hosted workflow evidence

These exports came from [public Ubuntu run 38734789749](https://github.com/Gerbzz/FigStrike/actions/runs/38734789749) at application source commit `01a7ba29d8b42fef743c4e5b97867bb7fd1c1666`. The workflow built the native editor and CLI, created a `.figcraft` file from `.github/figstrike-smoke.json`, reopened it in a separate CLI process and exported PNG, SVG and PDF. It also reopened the synthetic upstream `examples/ridgeline-app.figcraft` sample and exported its PNG. The original run artifact includes the native document, SVG, PDF, metadata and logs but expires after seven days.

- [`created.png`](created.png): newly created text and auto-layout frame.
- [`ridgeline.png`](ridgeline.png): render of the upstream synthetic Ridgeline sample; the black page surroundings in the PNG are transparent canvas pixels displayed against a dark viewer.
- [`figstrike-first-run.png`](figstrike-first-run.png): uncropped native desktop first-run window from [public startup run 38739905782](https://github.com/Gerbzz/FigStrike/actions/runs/38739905782) on Ubuntu/Xvfb with Mesa software graphics. The app window occupies 1440×900 of the 1600×1000 virtual display. The approved PWDS logo appears in its home header.

The source and artwork provenance for all three images is recorded in [`ATTRIBUTION.md`](../../ATTRIBUTION.md). The first two show renderer output; the third shows the real FigStrike desktop window.

## Windows 2025 hosted run

[Public run 38746168229](https://github.com/Gerbzz/FigStrike/actions/runs/38746168229) built the full desktop and CLI binaries, passed 17 CLI integration tests, and created/reopened a native `.figcraft` design on Windows. Its CLI exported PNG, SVG and PDF, and a pinned pure-Python PDF parser found selectable “Hello from FigStrike” text. It also reopened and exported the synthetic Ridgeline sample.

- [`figstrike-windows-editor.png`](figstrike-windows-editor.png): unmodified capture of the running native Windows editor with the saved design open. The 1024×768 hosted desktop constrains the window; the black outer pixels are outside the app surface.
- [`figstrike-windows-created.png`](figstrike-windows-created.png) and [`figstrike-windows-ridgeline.png`](figstrike-windows-ridgeline.png): Windows renderer exports from the created design and upstream synthetic sample.
- [`figstrike-windows-verification.json`](figstrike-windows-verification.json) and [`figstrike-windows-desktop-status.json`](figstrike-windows-desktop-status.json): exact CLI and native process/window checks.

These captures came from code commit `f829325f703f580cedad802cb162fdf45036feeb`; the small artifact originally retained them for one day. Their provenance and licences are listed in [`ATTRIBUTION.md`](../../ATTRIBUTION.md).
