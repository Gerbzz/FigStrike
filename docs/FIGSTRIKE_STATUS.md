# FigStrike foundation and verification

## Foundation decision

The full native [FigCraft application](https://github.com/storytold/figcraft) is the foundation, pinned at commit [`102404e8c3d23d86c3490c1a6beff3202bb73e25`](https://github.com/storytold/figcraft/commit/102404e8c3d23d86c3490c1a6beff3202bb73e25). The source contains a Rust document engine, egui editor, web frontend, CLI, collaboration server, examples, and tests. It is dual-licensed MIT OR Apache-2.0; both root licenses and the upstream copyright notice are preserved.

[Graphite](https://github.com/GraphiteEditor/Graphite) is a strong open-source Rust graphics editor, but its current focus is vector/raster and procedural graphics rather than a complete interface design and prototype workflow. [Penpot](https://github.com/penpot/penpot) provides a broad open-source product design platform, but its application stack is not a native Rust editor. FigCraft is therefore the closest compatible whole-application base for this slot.

## Integrated in this fork

- Independent public root history, with the restricted ArtCraft artwork removed *before* that root commit. Upstream source provenance is pinned above, and NOTICE and ATTRIBUTION.md retain software and asset credit.
- Existing approved PWDS bitmap, copied byte for byte (SHA-256 `B4C19554261C06EFCA0EE81879BC9CCCAFBEF7FDE84E92328354324E39670C18`) into `assets/branding/`; its separate terms are explicit.
- FigStrike home header and About panel with that logo, version and upstream credit. First launch now opens the home screen as intended. Desktop title, Windows version resource, user config path, help link, CLI banner and selected menus identify FigStrike.
- Native `.figcraft` files, command identifiers, Rust package names and CLI executable names stay compatible with upstream files and scripts. The original permissively licensed chameleon icon remains as an inherited app icon, with attribution.
- Upstream release workflows and packaging removed because they contained original product identity and installer identifiers. No release or installer is claimed.

## Verification

The public [Ubuntu full workflow](https://github.com/Gerbzz/FigStrike/actions/runs/38734789749) built the desktop and CLI, passed 868 engine tests (two ignored), 329 UI tests (one ignored), and 17 CLI integration tests. It created and reopened a synthetic `.figcraft` design and exported PNG, SVG, and PDF with selectable text. Its first window attempt lacked a runner library; the [focused startup run](https://github.com/Gerbzz/FigStrike/actions/runs/38739905782) passed and captured the real first-run home screen.

The [Windows document run](https://github.com/Gerbzz/FigStrike/actions/runs/38746168229) built the native editor and CLI, passed all 17 CLI integration tests, opened a saved design in a real window, and rendered the synthetic Ridgeline example. The [focused native-edit run](https://github.com/Gerbzz/FigStrike/actions/runs/38760286187) moved a selected rectangle from x=50 to x=51 through the desktop UI's ArrowRight shortcut, saved the native file, and reopened it in a second editor process with the same geometry. The [reopened editor capture](evidence/figstrike-windows-native-edited.png), [Ridgeline render](evidence/figstrike-windows-ridgeline.png), and [exact persisted values](evidence/figstrike-windows-native-edit-verification.json) are retained in this repository. These artifacts were captured from application work in [draft PR #1](https://github.com/Gerbzz/FigStrike/pull/1); its application code remains unmerged.

No Rust compilation ran on the local C: drive because another suite task owns that build slot and free space must stay above 20 GiB. These are synthetic source checks, not a production release.

## Known gaps

- Upstream calls this editor alpha. The presence of source and sample documents is not proof of production-quality rendering, collaboration, complex Figma imports or all prototype interactions. `.fig` compatibility is best effort. [Upstream roadmap](https://github.com/storytold/figcraft/blob/102404e8c3d23d86c3490c1a6beff3202bb73e25/ROADMAP.md) and [parity notes](target-app-parity.md) describe the remaining work.
- macOS, FreeBSD and browser builds, installed packages, Windows high-DPI and first-run visuals, real external Figma documents and multi-user sessions still require separate verification. The inherited `docs/images/` screenshots document upstream FigCraft; the two images under `docs/evidence/` linked above are actual FigStrike Windows outputs.
- Some inherited interface/help/localization copy and the open-source chameleon icon still say or depict FigCraft. Package identity and translated strings need a deliberate follow-up before a release. Do not use the removed upstream packaging or release scripts for distribution.
