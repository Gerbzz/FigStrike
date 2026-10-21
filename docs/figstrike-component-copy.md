# FigStrike component copy port

This source port starts at FigStrike main
`4def472a72ca9dd8737d73ebe814c87b4cc3f539`. It adapts
[FigCraft b82369201dec672737e6f09b15ffa2ae76d0b31b](https://github.com/storytold/figcraft/commit/b82369201dec672737e6f09b15ffa2ae76d0b31b)
by bflatastic, including its prerequisite
[0108a7c2f5dda45304320469caa0c8e36cac1d65](https://github.com/storytold/figcraft/commit/0108a7c2f5dda45304320469caa0c8e36cac1d65)
by MortenHusted (co-authored by Codex). Original software attribution and licences remain in place.

Duplicate and Alt-drag use `components::copy_in_file`: a copied main becomes a linked instance
with its original local transform and the existing offset and selection behavior. A variant
copied inside a component set remains a new variant; sets and ordinary layers are deep-copied.
Instances keep their default names under the rename-duplicates preference.

The older FigStrike clipboard lacked the prerequisite's same-file component behavior. Its port
marks roots copied with Copy separately from Cut, creates instances only while the copied main
still exists in the same document, preserves the copied world transform, and avoids implicitly
pasting inside the main. Undo drops markers for discarded component IDs so an unrelated component
created with a reused ID cannot become the paste's main. Foreign-file adoption and the existing
deep-copy fallback are retained. No new command, dependency, file format or UI surface is added.
Unrelated upstream changes, including later clipboard import features, are outside this port.
The existing public Rust helper `copy_to_clipboard(s, ids)` retains its signature and Copy semantics;
a private helper distinguishes Cut without breaking current callers.

## Regression coverage

The eight upstream test functions cover linked updates, mixed selections and duplicate names,
default offsets, Alt-drag positions, variants and whole sets, same-file Paste/Paste Over/Paste to
Replace, cut/foreign-file copies, undo ID reuse, copied transforms and atomic refusal to paste
inside a main. Added assertions cover ordinary-layer renaming and Alt-drag as one undo step with
exact undo/redo restoration. Two additional tests cover transformed nested-main duplication with
explicit offsets and sibling order, and preserving a main nested inside a copied frame.

## Validation status

Only source and lightweight checks are authorized while SkinStrike owns the heavy-build slot.

| Check | Status |
|---|---|
| `git diff --check` | Executed, passed |
| `rustfmt --edition 2024 --config skip_children=true --check` on the five changed Rust files | Executed, passed; parses/formats source, does not type-check |
| `cargo metadata --no-deps --offline --locked --format-version 1` | Executed, passed; 21 workspace packages, no dependency resolution or build |
| Dependency review | No manifest or lockfile changes; no new dependency or feature |
| Branding, licences, attribution and assets | No changes to their files |
| Prior safeguards | Existing instance-edit validation, foreign adoption and transaction paths retained; runtime checks pending |
| Ten new Rust regression test functions | Never compiled or executed in this session |
| Engine/UI/CLI tests, full `cargo xtask ci`, WASM and native pointer smoke | Never run; remain acceptance gates |

No behavioral test is reported as passing or failing. No generated executable was run. Full CI
and a native Duplicate/Alt-drag check must be completed after the heavy-build slot is available,
using a separate target directory and keeping at least 20 GiB free. Start with
`cargo test --locked -p figcraft-engine --lib components_behaviour_tests`, then run the repository's
full `cargo xtask ci` gate and native pointer checks. Do not publish based on source checks alone.

The repository's `AGENTS.md` was read. Its referenced `storytold/craftrules/AGENTS.md` was unavailable
through GitHub (404); no shared-rules content was inferred. The user's source-only and
no-publication restrictions take precedence over the repository's usual full-CI/push instructions.
