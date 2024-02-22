COLOR_BANDS = {"black": 0, "brown": 1, "red": 2, "orange": 3, "yellow": 4,
               "green": 5, "blue": 6, "violet": 7, "grey": 8, "white": 9}


def label(colors: list[str]) -> str:
    last_color = colors[2]
    color_band = COLOR_BANDS[last_color]
    print(color_band)
    ohms = str(int("".join([str(COLOR_BANDS[color])
                            for color in colors[0:2]]))) + "0" * color_band

    # if ohms.startswith("0"):
    #     splited = ohms.split(" ")
    #     ohms = " ".join([int(splited[0]), splited[1]])
    if ohms.endswith("000000000"):
        ohms = ohms.replace("000000000", "") + " gigaohms"
    elif ohms.endswith("000000"):
        ohms = ohms.replace("000000", "") + " megaohms"
    elif ohms.endswith("000"):
        ohms = ohms.replace("000", "") + " kiloohms"
    else:
        ohms = f"{ohms} ohms"
    return ohms
