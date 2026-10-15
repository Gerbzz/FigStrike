# FigStrike hosted workflow evidence

These exports came from [public Ubuntu run 38734789749](https://github.com/Gerbzz/FigStrike/actions/runs/38734789749) at application source commit `01a7ba29d8b42fef743c4e5b97867bb7fd1c1666`. The workflow built the native editor and CLI, created a `.figcraft` file from `.github/figstrike-smoke.json`, reopened it in a separate CLI process and exported PNG, SVG and PDF. It also reopened the synthetic upstream `examples/ridgeline-app.figcraft` sample and exported its PNG. The original run artifact includes the native document, SVG, PDF, metadata and logs but expires after seven days.

- [`created.png`](created.png): newly created text and auto-layout frame.
- [`ridgeline.png`](ridgeline.png): render of the upstream synthetic Ridgeline sample; the black page surroundings in the PNG are transparent canvas pixels displayed against a dark viewer.
- [`figstrike-first-run.png`](figstrike-first-run.png): uncropped native desktop first-run window from [public startup run 38739905782](https://github.com/Gerbzz/FigStrike/actions/runs/38739905782) on Ubuntu/Xvfb with Mesa software graphics. The app window occupies 1440×900 of the 1600×1000 virtual display. The approved PWDS logo appears in its home header.

The source and artwork provenance for all three images is recorded in [`ATTRIBUTION.md`](../../ATTRIBUTION.md). The first two show renderer output; the third shows the real FigStrike desktop window.
