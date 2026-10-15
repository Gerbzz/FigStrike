# Attribution

Every asset bundled in this repository (images, icons, fonts, data files) is listed here with its
author, source and licence. `cargo xtask assets` fails if a file under `assets/` or
`docs/images/` is missing from this list.

FigCraft's user-interface icons are drawn in code (`crates/ui-egui/src/icons.rs`): original work,
MIT OR Apache-2.0. No third-party icon sets are used.

## Assets in this repository

| Path | Author | Source | Licence | Notes |
|---|---|---|---|---|
| `assets/app-icon/` (all files: `figcraft.svg`, `figcraft-small.svg`, `figcraft-*.png`, `figcraft.ico`, `hicolor/`) | The project owner (engraving-style drawing, vectorised) | Original work, see [`assets/app-icon/README.md`](assets/app-icon/README.md); derived files rendered by `cargo xtask icon` | MIT OR Apache-2.0, [`assets/app-icon/LICENSE.txt`](assets/app-icon/LICENSE.txt) | FigCraft app icon (chameleon) |
| `assets/branding/PWDS-logo.png` | Pro WebDev Solutions | Existing approved mark from `Gerbzz/PWDS-Strike-Launcher`, copied byte for byte | Separate PWDS brand terms in [`assets/branding/LICENSE-brand.txt`](assets/branding/LICENSE-brand.txt) | FigStrike home and About only; SHA-256 `B4C19554261C06EFCA0EE81879BC9CCCAFBEF7FDE84E92328354324E39670C18` |
| `docs/images/` (all screenshots and exports: `shot-*.png`, `art-*.png`) | FigCraft contributors | Screenshots of FigCraft showing synthetic demo documents made in FigCraft, and PNG exports of those documents by FigCraft's renderer | MIT OR Apache-2.0 | No third-party artwork |
| `docs/evidence/created.png` | FigStrike contributors | PNG exported by the FigStrike CLI from the synthetic command script `.github/figstrike-smoke.json` in [hosted run 38734789749](https://github.com/Gerbzz/FigStrike/actions/runs/38734789749) | MIT OR Apache-2.0 | Workflow result; no third-party artwork |
| `docs/evidence/ridgeline.png` | FigCraft contributors; exported by FigStrike | PNG exported by the FigStrike CLI from `examples/ridgeline-app.figcraft` in [hosted run 38734789749](https://github.com/Gerbzz/FigStrike/actions/runs/38734789749) | MIT OR Apache-2.0 | Synthetic upstream demo; no third-party artwork |
| `docs/evidence/figstrike-first-run.png` | FigStrike contributors; underlying template art by FigCraft contributors | Native desktop screenshot captured in [hosted run 38739905782](https://github.com/Gerbzz/FigStrike/actions/runs/38739905782), including the separately licensed PWDS logo | UI and templates: MIT OR Apache-2.0; logo: [`assets/branding/LICENSE-brand.txt`](assets/branding/LICENSE-brand.txt) | Uncropped Xvfb first-run screen |
| `docs/evidence/figstrike-windows-editor.png` | FigStrike contributors | Unmodified Windows native editor screen capture from [green run 38746168229](https://github.com/Gerbzz/FigStrike/actions/runs/38746168229), showing the synthetic design created by the CLI | MIT OR Apache-2.0 | 1024×768 hosted desktop; the window did not use all virtual screen pixels |
| `docs/evidence/figstrike-windows-created.png` | FigStrike contributors | Windows CLI PNG export from `.github/figstrike-smoke.json` in [green run 38746168229](https://github.com/Gerbzz/FigStrike/actions/runs/38746168229) | MIT OR Apache-2.0 | Synthetic text and auto layout |
| `docs/evidence/figstrike-windows-ridgeline.png` | FigCraft contributors; exported by FigStrike | Windows CLI PNG export of synthetic `examples/ridgeline-app.figcraft` in [green run 38746168229](https://github.com/Gerbzz/FigStrike/actions/runs/38746168229) | MIT OR Apache-2.0 | No third-party artwork |
| `docs/evidence/figstrike-windows-verification.json`, `docs/evidence/figstrike-windows-desktop-status.json` | FigStrike contributors | Machine-readable CLI and native-window reports from [green run 38746168229](https://github.com/Gerbzz/FigStrike/actions/runs/38746168229) | MIT OR Apache-2.0 | These reports are synthetic verification, not release acceptance |
| `docs/evidence/figstrike-windows-native-edited.figcraft` | FigStrike contributors | Synthetic native-editor document created, keyboard-edited, saved and reopened in [green run 38760286187](https://github.com/Gerbzz/FigStrike/actions/runs/38760286187) | MIT OR Apache-2.0 | Original frame and rectangle; no third-party media |
| `docs/evidence/figstrike-windows-native-edited.png` | FigStrike contributors | Unmodified in-app screenshot of the reopened Windows editor in [green run 38760286187](https://github.com/Gerbzz/FigStrike/actions/runs/38760286187) | MIT OR Apache-2.0 | 1024x768 hosted desktop; saved frame and rectangle visible |
| `docs/evidence/figstrike-windows-native-edit-verification.json` | FigStrike contributors | Exact before, edited and reopened node values from [green run 38760286187](https://github.com/Gerbzz/FigStrike/actions/runs/38760286187) | MIT OR Apache-2.0 | Native control channel routed ArrowRight through the UI shortcut handler |
| `examples/*.figcraft` | FigCraft contributors | Synthetic demo documents built through FigCraft's command API; invented copy, shapes and vectors drawn from scratch, no images or embedded fonts | MIT OR Apache-2.0 | Text uses Inter (OFL, from craft-fonts or the system); no third-party artwork |

## Fonts (build input, not in this repository)

Release builds embed fonts from the optional craft-fonts build input
([storytold/craft-fonts](https://github.com/storytold/craft-fonts), `CRAFT_FONTS_DIR`). Its own
`ATTRIBUTION.md` and licence files are authoritative; the packages ship each font's licence.

| Family | Licence | Upstream |
|---|---|---|
| Inter | SIL Open Font License 1.1 | https://github.com/rsms/inter |
| Roboto, Montserrat, Lato, Open Sans, Poppins, Nunito Sans, Merriweather, Playfair Display, Source Sans 3, Source Serif 4, Carlito, Caladea | SIL Open Font License 1.1 | Google Fonts / upstream repositories (see craft-fonts) |
| Liberation Sans, Serif, Mono | SIL Open Font License 1.1 | https://github.com/liberationfonts |
| BIZ UDPGothic, BIZ UDMincho, Shippori Mincho, Noto Sans Arabic | SIL Open Font License 1.1 | Google Fonts (see craft-fonts) |

egui's default fonts (compiled into the `egui`/`epaint` crates) keep their own licences (OFL / Apache-2.0 / Ubuntu Font Licence); see those crates.
