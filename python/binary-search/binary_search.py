def find(search_list: list[int], value: int) -> int:
    try:
        return search_list.index(value)
    except Exception:
        raise ValueError("value not in array")
