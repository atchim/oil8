# 🛢️ Oil 8 for [Alacritty]

## 🎨 Installation

The installation of the Oil 8 theme for the [Alacritty] terminal emulator is
based on the [`oil8.toml`] configuration file, which contains the color
specifications. Follow one of the methods below to install Oil 8 for Alacritty.

### 🔗 Import the [`oil8.toml`] File (Recommended)

To import the Oil 8 color specifications into the `alacritty.toml`
configuration, simply add the following line, replacing the path with the
correct location of the [`oil8.toml`](oil8.toml) file.

```toml
import = ['path/to/oil8.toml']
```

If the import key already exists in the `alacritty.toml`, just append the path
to `oil8.toml`.

### 📋 Copy the Color Specifications

It is also possible to just copy the color specifications from [`oil8.toml`]
into the `alacritty.toml` configuration file.

[Alacritty]: https://alacritty.org/
[`oil8.toml`]: oil8.toml
