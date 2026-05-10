# 🛢️ Oil 8 for [rofi]

The rofi integration provides three files:

- [`oil8.rasi`]: the Oil 8 palette as rasi color variables for use in any rofi
  theme.
- [`board.rasi`]: the default Oil 8 theme that imports [`oil8.rasi`] and styles
  standard rofi widgets.
- [`dmenu.rasi`]: a horizontal, bottom-anchored variant that imports
  [`board.rasi`].

## 🎨 Installation

Place the three files into the rofi themes directory (typically
`~/.config/rofi/themes/`). Symlinking is recommended over copying, since
updates to the theme will flow in with a `git pull` on this repository.

## 🚀 Usage

Apply the default Oil 8 theme to a rofi launcher:

```sh
rofi -show drun -theme board
```

Use the dmenu variant for a horizontal, bottom-anchored bar:

```sh
rofi -dmenu -theme dmenu
```

Reference the palette from a custom rofi theme via `@theme "oil8"`:

```rasi
@theme "oil8"

* {
  background-color: @dark-gunmetal;
  text-color: @bone;
}

prompt {
  text-color: @chinese-green;
}
```

[`board.rasi`]: board.rasi
[`dmenu.rasi`]: dmenu.rasi
[`oil8.rasi`]: oil8.rasi
[rofi]: https://github.com/davatorium/rofi
