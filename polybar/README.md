# 🛢️ Oil 8 for [Polybar]

## 🎨 Installation

The installation of the Oil 8 theme for the [Polybar] status bar creation tool
is based on color
[variables](https://github.com/polybar/polybar/wiki/Configuration#custom-variables)
defined in the [`oil8.ini`] file. To use the color definitions, just reference
the colors via `${oil8.color-name}`, as shown in the example below.

> [!NOTE]
> The color names for Polybar are in
> [kebab case](https://en.wikipedia.org/wiki/Letter_case#Kebab_case), meaning
> underscores (`_`) are replaced with hyphens (`-`). For example, `eerie-black`
> should be used instead of `eerie_black`.

```ini
[bar/mybar]
background = ${oil8.eerie-black}
foreground = ${oil8.bone}
```

To make the color variables available for use, follow one of the methods below.

### 🔗 Include the [`oil8.ini`] File (Recommended)

To include the [`oil8.ini`] file, set its path as value for the
[`include-file`](https://github.com/polybar/polybar/wiki/Configuration#file-inclusion)
predefined key-value pair, as shown in the following example.

```ini
include-file = path/to/oil8.ini

[modules/tmp]
format-background = ${oil8.space-cadet}
format-foreground = ${oil8.chinese-green}
```

### 📋 Copy the Color Specifications

It is also possible to simply copy the color definitions from the [`oil8.ini`]
into the configuration file that will use the colors.

[`oil8.ini`]: oil8.ini
[Polybar]: https://polybar.github.io/
