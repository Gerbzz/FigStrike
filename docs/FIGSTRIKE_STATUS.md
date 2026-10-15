# FigStrike foundation and verification

## Foundation decision

The full native [FigCraft application](https://github.com/storytold/figcraft) is the foundation, pinned at commit [`102404e8c3d23d86c3490c1a6beff3202bb73e25`](https://github.com/storytold/figcraft/commit/102404e8c3d23d86c3490c1a6beff3202bb73e25). The source contains a Rust document engine, egui editor, web frontend, CLI, collaboration server, examples, and tests. It is dual-licensed MIT OR Apache-2.0; both root licenses and the upstream copyright notice are preserved.

[Graphite](https://github.com/GraphiteEditor/Graphite) is a strong open-source Rust graphics editor, but its current focus is vector/raster and procedural graphics rather than a complete interface design and prototype workflow. [Penpot](https://github.com/penpot/penpot) provides a broad open-source product design platform, but its application stack is not a native Rust editor. FigCraft is therefore the closest compatible whole-application base for this slot.

## Integrated in this fork

- Independent public root history, with the restricted ArtCraft artwork removed *before* that root commit. Upstream source provenance is pinned above, and NOTICE and ATTRIBUTION.md retain software and asset credit.
- Existing approved PWDS bitmap, copied byte for byte (SHA-256 `B4C19554261C06EFCA0EE81879BC9CCCAFBEF7FDE84E92328354324E39670C18`) into `assets/branding/`; its separate terms are explicit.
- FigStrike home header and About panel with that logo, version and upstream credit. Normal launches now open the home screen; explicit files and invite links go directly to the editor. Desktop title, Windows version resource, user config path, help link, CLI banner and selected menus identify FigStrike.
- Native `.figcraft` files, command identifiers, Rust package names and CLI executable names stay compatible with upstream files and scripts. The original permissively licensed chameleon icon remains as an inherited app icon, with attribution.
- Upstream release workflows and packaging removed because they contained original product identity and installer identifiers. No release or installer is claimed.

## Verification

- [First hosted run](https://github.com/Gerbzz/FigStrike/actions/runs/38732876222) exposed four UI regressions from the new home header: three tests counted the persistent logo or clicked a template button below the fold, and one found obsolete localization keys. The home layout and catalogs were corrected before the next run.
- [Second hosted run](https://github.com/Gerbzz/FigStrike/actions/runs/38734789749) passed format and asset attribution, 868 engine tests (2 ignored), 329 UI tests (1 ignored), and 17 CLI integration tests. The full desktop and CLI binaries built. A command script created a text frame and auto layout, saved a `.figcraft` document, reopened it in a separate CLI process, and exported PNG, SVG and PDF. The PDF retained selectable text (`pdftotext` found “Hello from FigStrike”). The CLI also reopened and exported the supplied Ridgeline design. I inspected both PNG exports: the new text is legible and the Ridgeline screens and artwork render. The only failed step was Xvfb startup because the Ubuntu runner lacked `libxkbcommon-x11.so`; the app exited before opening a window.
- [Focused startup rerun](https://github.com/Gerbzz/FigStrike/actions/runs/38737866307) installed the missing X11 library and built only the desktop binary. Its screenshot step stopped before launch because the workflow's startup-only path had not created its output directory. The capture step now creates that directory itself; a further startup-only run is pending.

No Rust compilation ran on the local C: drive because another suite task owns that build slot and free space must stay above 20 GiB. Hosted runs use public standard Ubuntu runners, read-only repository permission and bounded job timeouts.

## Known gaps

- Upstream calls this editor alpha. The presence of source and sample documents is not proof of production-quality rendering, collaboration, complex Figma imports or all prototype interactions. `.fig` compatibility is best effort. [Upstream roadmap](https://github.com/storytold/figcraft/blob/102404e8c3d23d86c3490c1a6beff3202bb73e25/ROADMAP.md) and [parity notes](target-app-parity.md) describe the remaining work.
- Windows, macOS, FreeBSD and browser builds, installed packages, first-run visuals on each platform, real external Figma documents and multi-user sessions still require separate verification. The included upstream screenshots document upstream FigCraft; they are not FigStrike screenshots.
- Some inherited interface/help/localization copy and the open-source chameleon icon still say or depict FigCraft. Package identity and translated strings need a deliberate follow-up before a release. Do not use the removed upstream packaging or release scripts for distribution.
