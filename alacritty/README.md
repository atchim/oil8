# 🛢️ Oil 8 for [Alacritty]

## 🎨 Installation

Follow one of the methods below to install the Oil 8 color scheme for
[Alacritty]. The recommended approach is to import the palette file, which
keeps the configuration modular and easy to update.

### 🔗 Import the Palette File (Recommended)

To import the Oil 8 palette into thek `alacritty.toml` configuration, simply
add the following line, replacing the path with the correct location of the
[`palette.toml`](palette.toml) file.

```toml
import = ['path/to/alacritty/palette.toml']
```

If the import key already exists in the `alacritty.toml`, append the path to
the Oil 8 palette as shown above. This method ensures that future updates to
the palette are easy to apply.

### 📋 Copy the Color Specifications

It is also possible to just copy the color specifications from the
[`palette.toml` file](palette.toml) into the `alacritty.toml`
configuration file.

[Alacritty]: https://alacritty.org/