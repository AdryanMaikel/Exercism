def proverb(*args, qualifier: str | None) -> str:
    result = []
    if not args:
        return result

    qualifier = f"{qualifier} " if qualifier else ""

    for word1, word2 in zip(args[0:], args[1:]):
        result.append(f"For want of a {word1} the {word2} was lost.")
    result.append("And all for the want of a "+qualifier+args[0]+".")
    return result
