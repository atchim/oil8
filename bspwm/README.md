# 🛢️ Oil 8 for [bspwm]

## 🎨 Installation

The installation of the Oil 8 theme for the [bspwm] tiling window manager is
based on the [`oil8.sh`] script, which sets the border and pre-selection
feedback colors via `bspc config`. Follow one of the methods below to install
Oil 8 for bspwm.

### 🔗 Source the [`oil8.sh`] File (Recommended)

To apply the Oil 8 colors, source [`oil8.sh`] from the `bspwmrc` file, as shown
below. Replace the path with the correct location of [`oil8.sh`].

```sh
. path/to/oil8.sh
```

Symlinking [`oil8.sh`] is recommended over copying, since updates to the theme
will flow in with a `git pull` on this repository. This method requires
`bspwmrc` to use a POSIX-compliant shell interpreter (the default on most
distributions).

### 📋 Copy the Color Configuration

It is also possible to just copy the `bspc config` commands from [`oil8.sh`]
into the `bspwmrc` file. If `bspwmrc` uses a non-shell interpreter (e.g.
[Python](https://www.python.org/)), adapt the commands to that language.

[bspwm]: https://github.com/baskerville/bspwm
[`oil8.sh`]: oil8.sh
