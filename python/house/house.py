def recite(start_verse, end_verse):
    with open(r"python\house\music.txt", "r", encoding="utf-8") as file:
        lines = file.read().split("\n\n")[start_verse-1:end_verse]

    return [line.replace("\n", " ") for line in lines]
