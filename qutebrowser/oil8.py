# fmt: off
palette = {
  'eerie_black':         '#171629',
  'dark_gunmetal':       '#1c1b34',
  'space_cadet':         '#292449',
  'cyber_grape':         '#5f4c73',
  'antique_fuchsia':     '#8c607b',
  'burnished_brown':     '#a77d72',
  'ecru':                '#bdab87',
  'bone':                '#e1e0c4',
  'caput_mortuum':       '#622d2d',
  'english_red':         '#aa3c55',
  'brink_pink':          '#f35e7c',
  'tulip':               '#fe7c8d',
  'dark_lava':           '#4b3a30',
  'dirty_brown':         '#b25c1f',
  'big_foot_feet':       '#f38f5e',
  'macaroni_and_cheese': '#fab98a',
  'bronze_yellow':       '#606c09',
  'acid_green':          '#bbbd28',
  'chinese_green':       '#d4e05c',
  'inchworm':            '#bcec6a',
  'kombu_green':         '#31452b',
  'green_ryb':           '#4eb332',
  'mantis':              '#72db5e',
  'medium_aquamarine':   '#6ceaa7',
  'brunswick_green':     '#1b5c4d',
  'jungle_green':        '#2d9f84',
  'turquoise':           '#58e9ca',
  'middle_blue':         '#84cfdd',
  'ateneo_blue':         '#024c67',
  'steel_blue':          '#367ba6',
  'blue_jeans':          '#54b7e8',
  'baby_blue_eyes':      '#a4b6fe',
  'pixie_powder':        '#3e2187',
  'blue_pigment':        '#413aa1',
  'violets_are_blue':    '#966ef2',
  'mauve':               '#dd9ffe',
  'japanese_violet':     '#592a5f',
  'byzantine':           '#b22ab7',
  'light_deep_pink':     '#e557cd',
  'persian_pink':        '#fc83c5',
}
# fmt: on


def draw(c):
  p = palette

  # Completion
  # ----------

  c.colors.completion.even.bg = p["eerie_black"]
  c.colors.completion.fg = [p["ecru"], p["burnished_brown"], p["dirty_brown"]]
  c.colors.completion.odd.bg = p["dark_gunmetal"]
  c.colors.completion.match.fg = p["chinese_green"]

  c.colors.completion.category.bg = p["eerie_black"]
  c.colors.completion.category.border.bottom = p["eerie_black"]
  c.colors.completion.category.border.top = p["eerie_black"]
  c.colors.completion.category.fg = p["bone"]

  c.colors.completion.item.selected.bg = p["space_cadet"]
  c.colors.completion.item.selected.border.bottom = p["space_cadet"]
  c.colors.completion.item.selected.border.top = p["space_cadet"]
  c.colors.completion.item.selected.fg = p["bone"]
  c.colors.completion.item.selected.match.fg = p["violets_are_blue"]

  c.colors.completion.scrollbar.bg = p["dark_gunmetal"]
  c.colors.completion.scrollbar.fg = p["space_cadet"]

  # Context Menu
  # ------------

  c.colors.contextmenu.disabled.bg = p["dark_gunmetal"]
  c.colors.contextmenu.disabled.fg = p["burnished_brown"]
  c.colors.contextmenu.menu.bg = p["dark_gunmetal"]
  c.colors.contextmenu.menu.fg = p["ecru"]
  c.colors.contextmenu.selected.bg = p["cyber_grape"]
  c.colors.contextmenu.selected.fg = p["bone"]

  # Downloads
  # ---------

  c.colors.downloads.bar.bg = p["eerie_black"]
  c.colors.downloads.error.bg = p["eerie_black"]
  c.colors.downloads.error.fg = p["brink_pink"]
  c.colors.downloads.start.bg = p["cyber_grape"]
  c.colors.downloads.start.fg = p["bone"]
  c.colors.downloads.stop.bg = p["space_cadet"]
  c.colors.downloads.stop.fg = p["ecru"]
  c.colors.downloads.system.bg = "rgb"
  c.colors.downloads.system.fg = "rgb"

  # Hints
  # -----

  c.colors.hints.bg = p["violets_are_blue"]
  c.colors.hints.fg = p["eerie_black"]
  c.colors.hints.match.fg = p["pixie_powder"]
  c.hints.border = f"1px solid {p['violets_are_blue']}"
  c.hints.radius = 0

  # Key Hints
  # ---------

  c.colors.keyhint.bg = p["eerie_black"]
  c.colors.keyhint.fg = p["antique_fuchsia"]
  c.colors.keyhint.suffix.fg = p["bone"]
  c.keyhint.radius = 0

  # Messages
  # --------

  c.colors.messages.error.bg = p["eerie_black"]
  c.colors.messages.error.border = p["eerie_black"]
  c.colors.messages.error.fg = p["brink_pink"]
  c.colors.messages.info.bg = p["eerie_black"]
  c.colors.messages.info.border = p["eerie_black"]
  c.colors.messages.info.fg = p["chinese_green"]
  c.colors.messages.warning.bg = p["eerie_black"]
  c.colors.messages.warning.border = p["eerie_black"]
  c.colors.messages.warning.fg = p["big_foot_feet"]

  # Prompts
  # -------

  c.colors.prompts.bg = p["eerie_black"]
  c.colors.prompts.border = f"1px solid {p['eerie_black']}"
  c.colors.prompts.fg = p["ecru"]
  c.colors.prompts.selected.bg = p["cyber_grape"]
  c.colors.prompts.selected.fg = p["bone"]
  c.prompt.radius = 0

  # Status Bar
  # ----------

  c.colors.statusbar.caret.bg = p["cyber_grape"]
  c.colors.statusbar.caret.fg = p["bone"]
  c.colors.statusbar.caret.selection.bg = p["cyber_grape"]
  c.colors.statusbar.caret.selection.fg = p["bone"]

  c.colors.statusbar.command.bg = p["eerie_black"]
  c.colors.statusbar.command.fg = p["bone"]
  c.colors.statusbar.command.private.bg = p["eerie_black"]
  c.colors.statusbar.command.private.fg = p["mauve"]

  c.colors.statusbar.insert.bg = p["eerie_black"]
  c.colors.statusbar.insert.fg = p["bone"]
  c.colors.statusbar.normal.bg = p["eerie_black"]
  c.colors.statusbar.normal.fg = p["bone"]
  c.colors.statusbar.passthrough.bg = p["eerie_black"]
  c.colors.statusbar.passthrough.fg = p["bone"]
  c.colors.statusbar.private.bg = p["eerie_black"]
  c.colors.statusbar.private.fg = p["mauve"]
  c.colors.statusbar.progress.bg = p["bone"]

  c.colors.statusbar.url.error.fg = p["brink_pink"]
  c.colors.statusbar.url.fg = p["bone"]
  c.colors.statusbar.url.hover.fg = p["violets_are_blue"]
  c.colors.statusbar.url.success.http.fg = p["green_ryb"]
  c.colors.statusbar.url.success.https.fg = p["mantis"]
  c.colors.statusbar.url.warn.fg = p["chinese_green"]

  # Tabs
  # ----

  c.colors.tabs.bar.bg = p["eerie_black"]
  c.colors.tabs.even.bg = p["eerie_black"]
  c.colors.tabs.even.fg = p["ecru"]
  c.colors.tabs.odd.bg = p["dark_gunmetal"]
  c.colors.tabs.odd.fg = p["ecru"]

  c.colors.tabs.indicator.error = p["brink_pink"]
  c.colors.tabs.indicator.start = p["kombu_green"]
  c.colors.tabs.indicator.stop = p["mantis"]
  c.colors.tabs.indicator.system = "rgb"

  c.colors.tabs.pinned.even.bg = p["eerie_black"]
  c.colors.tabs.pinned.even.fg = p["ecru"]
  c.colors.tabs.pinned.odd.bg = p["eerie_black"]
  c.colors.tabs.pinned.odd.fg = p["ecru"]
  c.colors.tabs.pinned.selected.even.bg = p["space_cadet"]
  c.colors.tabs.pinned.selected.even.fg = p["bone"]
  c.colors.tabs.pinned.selected.odd.bg = p["space_cadet"]
  c.colors.tabs.pinned.selected.odd.fg = p["bone"]

  c.colors.tabs.selected.even.bg = p["space_cadet"]
  c.colors.tabs.selected.even.fg = p["bone"]
  c.colors.tabs.selected.odd.bg = p["space_cadet"]
  c.colors.tabs.selected.odd.fg = p["bone"]
