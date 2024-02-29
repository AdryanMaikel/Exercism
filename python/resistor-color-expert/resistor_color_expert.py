COLOR_BANDS = {"black": 0, "brown": 1, "red": 2, "orange": 3, "yellow": 4,
               "green": 5, "blue": 6, "violet": 7, "grey": 8, "white": 9}

TOLERANCE_BANDS = {"grey": "0.05%", "violet": "0.1%", "blue": "0.25%",
                   "green": "0.5%", "brown": "1%", "red": "2%", "gold": "5%",
                   "silver": "10%"}


def label(colors: list[str]) -> str:
    if len(colors) <= 1:
        return f"{COLOR_BANDS[colors[0]]} ohms"
    last_color = colors[-1]
    color_band = COLOR_BANDS[last_color]
    ohms = str(int("".join([str(COLOR_BANDS[color])
                            for color in colors[0:-1]]))) + "0" * color_band

    if ohms.endswith("000000000"):
        ohms = ohms.replace("000000000", "") + " gigaohms"
    elif ohms.endswith("000000"):
        ohms = ohms.replace("000000", "") + " megaohms"
    elif ohms.endswith("00000"):
        ohms = ohms.replace("00000", "")
        ohms = f"{ohms[0:2]}.{ohms[2:]} megaohms"
    elif ohms.endswith("0000"):
        ohms = ohms.replace("0000", "")
        ohms = f"{ohms[0]}.{ohms[1:]} megaohms"
    elif ohms.endswith("000"):
        ohms = ohms.replace("000", "") + " kiloohms"
    elif ohms.endswith("0") and len(ohms) == 4:
        ohms = ohms.replace("0", "")
        ohms = f"{ohms[0]}.{ohms[1:]} kiloohms"
    else:
        ohms = f"{ohms} ohms"
    return ohms


def resistor_label(colors: list[str]) -> str:
    if len(colors) <= 1:
        return label(colors)
    _label = label(colors[:-1])
    return f"{_label} ±{TOLERANCE_BANDS[colors[-1]]}"
