# 🛢️ Oil 8 for [qutebrowser]

## 🎨 Installation

The installation of the Oil 8 theme for the [qutebrowser] keyboard-driven
browser is based on the [`oil8.py`] module, which exposes a `draw` function
that applies the color settings to the qutebrowser configuration object.

Place [`oil8.py`] into the qutebrowser configuration directory (typically
`~/.config/qutebrowser/`) so that it can be imported from `config.py`.
Symlinking is recommended over copying, since updates to the theme will flow in
with a `git pull` on this repository.

Then, add the following lines to the `config.py` file used by qutebrowser:

```python
import oil8
oil8.draw(c)
```

[qutebrowser]: https://qutebrowser.org/
[`oil8.py`]: oil8.py
