# 🛢️ Oil 8 for [bspwm]

## 🎨 Installation

The installation of the Oil 8 theme for the [bspwm] tiling window manager is
based on color configurations defined in the `bspwmrc` file with the `bspc`
command.

> [!NOTE]
> The `bspwmrc` file is typically an executable script beginning with a
> [shebang](https://en.wikipedia.org/wiki/Shebang_(Unix)) that specifies a
> [POSIX-compliant shell](https://en.wikipedia.org/wiki/Unix_shell#Bourne_shell)
> (`#!/bin/sh`) or even a specific shell like
> [Bash](https://www.gnu.org/software/bash/)
> (`#!/bin/bash`). However, any executable program, such as
> [Python](https://www.python.org/), can be used as the interpreter. As a
> result, the method for setting color configurations may vary depending on the
> interpreter defined by the shebang.

If the `bspwmrc` file has a shebang using a shell interpreter like `sh`,
`bash`, of `fish`, just copy the content of the [`bspwmrc`] file into the
configuration file for bspwm. Otherwise, adapt the color configuration commands
in [`bspwmrc`] to match the syntax and conventions of the specified
language/interpreter.

[bspwm]: https://github.com/baskerville/bspwm
[`bspwmrc`]: bspwmrc
