def find_anagrams(word: str, candidates: list[str]) -> list[str | None]:
    word = word.lower()
    return [candidate for candidate in candidates
            if word != candidate.lower() and
            sorted(word) == sorted(candidate.lower())]
