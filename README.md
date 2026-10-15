# FigStrike

FigStrike is a Rust interface design and prototyping application based on the complete open-source [FigCraft](https://github.com/storytold/figcraft) app. The native editor includes frames, auto layout, components and variants, styles, variables, vector editing, interactive prototypes, import/export, and a command-driven CLI. The repository contains the full application, not a crate extract or a UI mockup.

**Status:** early alpha. This is a source integration and public draft. It is not a production-ready Figma replacement. Read [the verified status and gaps](docs/FIGSTRIKE_STATUS.md) before relying on it for client files.

The first-run home screen and About panel use the approved PWDS logo. The original ArtCraft marks have been removed. The software stays dual-licensed under [MIT](LICENSE-MIT) or [Apache-2.0](LICENSE-APACHE), with upstream credit in [NOTICE](NOTICE) and per-asset credit in [ATTRIBUTION.md](ATTRIBUTION.md). The PWDS mark has separate [brand terms](assets/branding/LICENSE-brand.txt).

## Build and use

Requires Rust 1.95 or newer and the native libraries for egui/winit. See the upstream [building instructions](https://github.com/storytold/figcraft#get-started) for platform dependencies. This fork preserves the internal `figcraft` crate/binary names and `.figcraft` native format so existing files and scripts remain compatible.

```sh
cargo build --locked -p figcraft -p figcraft-cli
cargo run --locked -p figcraft
cargo run --locked -p figcraft-cli -- info examples/ridgeline-app.figcraft
cargo run --locked -p figcraft-cli -- export examples/ridgeline-app.figcraft -o screens.pdf
```

The editor can open/save the native file, and the CLI can inspect, render, export, convert, and run engine command scripts. See [CLI commands](docs/cli.md), [control protocol](docs/control-protocol.md), and [engine architecture](docs/architecture.md). Existing examples under `examples/` are original FigCraft contributor work and retain their attribution.

The bundled chameleon app icon remains under its separate permissive source license. It is an inherited upstream asset, not the FigStrike logo. Packaging and broader brand cleanup remain on the status list.

## Source and licensing

The imported source is pinned to [FigCraft commit `102404e8c3d23d86c3490c1a6beff3202bb73e25`](https://github.com/storytold/figcraft/commit/102404e8c3d23d86c3490c1a6beff3202bb73e25). This repo starts with an independent root commit so the upstream restricted ArtCraft artwork is absent from its public Git history. Software copyright and licenses remain in the root license files and NOTICE. FigStrike is an independent modified fork; ArtCraft does not endorse it.
