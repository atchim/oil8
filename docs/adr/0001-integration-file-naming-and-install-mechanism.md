# Integration file naming and install mechanism

Each integration ships its theme as `oil8.<ext>` and recommends an install path
that lets the file be **symlinked** from this repository, so users get theme
updates via `git pull` without touching the target tool's main configuration.
The `<ext>` follows the target tool's own convention (`oil8.toml` for
Alacritty, `oil8.sh` for bspwm sourced from `bspwmrc`, `oil8.rasi` for rofi
themes, `oil8.conf` for Dunst drop-ins under `dunstrc.d/`, etc.). When the
target tool requires its native filename and offers no include or drop-in
mechanism — Zathura's `zathurarc` is the current example — the integration
uses that filename and falls back to a copy-based install.

## Considered Options

- **Drop-in / source-based install (chosen).** Symlinks survive updates and
  keep theme content out of the user's main config.
- **Copy-paste snippets.** The previous default for the Dunst integration.
  Rejected because the user's existing `dunstrc` would already define
  `background`, `foreground`, and `frame_color`, forcing a manual merge on
  every update.
