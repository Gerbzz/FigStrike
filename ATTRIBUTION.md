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
