# numbers = "Ten Nine Eight Seven Six Five Four Three Two One".split()
numbers = "One Two Three Four Five Six Seven Eight Nine Ten".split()
verses = {1: " green bottles hanging on the wall,",
          2: "And if one green bottle should accidentally fall,",
          3: "There'll be ~~ green bottles hanging on the wall."}


def recite(start: int, take: int = 1) -> list[str]:
    result = []
    for i in range(take):
        number = numbers[start-i-1]
        next_number = numbers[start-i-2].lower()

        first_verse = verses[1]
        third_verse = verses[3]

        if number == "One":
            next_number = "no"
            first_verse = first_verse.replace("bottles", "bottle")

        if next_number == "one":
            third_verse = third_verse.replace("bottles", "bottle")

        for _ in range(2):
            result.append(f"{number}{first_verse}"),

        result.append(verses[2])

        result.append(third_verse.replace("~~", next_number))

        if i != take-1:
            result.append("")

    return result
