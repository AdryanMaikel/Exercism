def flatten(iterable: list) -> list:
    values = []
    for value in iterable:
        if isinstance(value, list):
            values.extend(flatten(value))
        elif isinstance(value, int):
            values.append(value)
    return values
