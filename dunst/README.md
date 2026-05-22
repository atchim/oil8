# 🛢️ Oil 8 for [Dunst]

The Oil 8 integration for the [Dunst] notification daemon is a color-only
[`oil8.conf`] designed to be installed as a [drop-in], so it overrides the
palette of an existing `dunstrc` without forcing edits to it.

## 🎨 Installation

### 🔗 Symlink as a Drop-in (Recommended)

Symlink [`oil8.conf`] into Dunst's drop-in directory:

```sh
ln -s path/to/oil8.conf ~/.config/dunst/dunstrc.d/oil8.conf
```

Drop-ins are loaded after the main `dunstrc` in lexical order, so Oil 8 wins
over the colors defined there. Symlinking is preferred over copying, since
updates to the theme will flow in with a `git pull` on this repository.

The filename must end in `.conf` for Dunst to read it. If other drop-ins are
present, prefix the symlink with a number (e.g. `50-oil8.conf`) to control
ordering — see [`dunst(1)`][dunst-man] for details.

### 📋 Merge Into `dunstrc`

Alternatively, copy the `[global]`, `[urgency_low]`, and `[urgency_critical]`
keys from [`oil8.conf`] into the corresponding sections of the `dunstrc` file
used by the daemon. Existing color keys in those sections must be removed
first, since Dunst does not merge duplicate keys within a section.

[Dunst]: https://dunst-project.org/
[drop-in]: https://man.archlinux.org/man/extra/dunst/dunst.1.en#FILES
[dunst-man]: https://man.archlinux.org/man/extra/dunst/dunst.1.en
[`oil8.conf`]: oil8.conf
