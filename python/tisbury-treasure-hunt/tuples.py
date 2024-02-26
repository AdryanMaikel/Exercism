"""Functions to help Azara and Rui locate pirate treasure."""


def get_coordinate(record: tuple) -> str:
    """Return coordinate value from a tuple containing the treasure
    name, and treasure coordinate.

    :param record: tuple - with a (treasure, coordinate) pair.
    :return: str - the extracted map coordinate.
    """
    return record[1]


def convert_coordinate(coordinate: str) -> tuple[str]:
    """Split the given coordinate into tuple containing its individual
    components.

    :param coordinate: str - a string map coordinate
    :return: tuple - the string coordinate split into its individual
    components.
    """
    return tuple(coordinate)


def compare_records(azara_record: tuple[str], rui_record: tuple[str]) -> bool:
    """Compare two record types and determine if their coordinates match.

    :param azara_record: tuple - a (treasure, coordinate) pair.
    :param rui_record: tuple - a (location, tuple(coordinate_1,
    coordinate_2), quadrant) trio.
    :return: bool - do the coordinates match?
    """
    return azara_record[1] == "".join(rui_record[1])


def create_record(azara_record: tuple[str], rui_record: tuple[str]):
    """Combine the two record types (if possible) and create a combined
    record group.

    :param azara_record: tuple - a (treasure, coordinate) pair.
    :param rui_record: tuple - a (location, coordinate, quadrant) trio.
    :return: tuple or str - the combined record (if compatible), or the
    string "not a match" (if incompatible).
    """
    if azara_record[1] == "".join(rui_record[1]):
        return azara_record + rui_record
    return "not a match"


def clean_up(combined_record_group: tuple[tuple[str]]) -> str:
    """Clean up a combined record group into a multi-line string of
    single records.

    :param combined_record_group: tuple - everything from both
    participants.
    :return: str - everything "cleaned", excess coordinates and
    information are removed.

    The return statement should be a multi-lined string with items
    separated by newlines.

    (see HINTS.md for an example).
    """
    result_str = """"""
    for row in combined_record_group:
        row = list(row)
        row.pop(1)
        result_str += f"{tuple(row)}\n"
    return result_str
