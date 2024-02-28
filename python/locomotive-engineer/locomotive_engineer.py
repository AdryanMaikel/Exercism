"""Functions which helps the locomotive engineer to keep track of the train."""


def get_list_of_wagons(*args: int):
    """Return a list of wagons.

    :param: arbitrary number of wagons.
    :return: list - list of wagons.
    """
    return list(args)


def fix_list_of_wagons(each_wagons_id: list[int],
                       missing_wagons: list[int]) -> list[int]:
    """Fix the list of wagons.

    :param each_wagons_id: list - the list of wagons.
    :param missing_wagons: list - the list of missing wagons.
    :return: list - list of wagons.
    """
    MIN = min(each_wagons_id)
    index = each_wagons_id.index(MIN)
    return [MIN, *missing_wagons, *each_wagons_id[index+1:],
            *each_wagons_id[:index]]


def add_missing_stops(route: dict[str, str], **kwargs: dict[str, str]
                      ) -> dict[str, str | list[str]]:
    """Add missing stops to route dict.

    :param route: dict - the dict of routing information.
    :param: arbitrary number of stops.
    :return: dict - updated route dictionary.
    """
    return {**route, "stops": [*kwargs.values()]}


def extend_route_information(route: dict[str, str],
                             more_route_information: dict[str, str]
                             ) -> dict[str, str]:
    """Extend route information with more_route_information.

    :param route: dict - the route information.
    :param more_route_information: dict -  extra route information.
    :return: dict - extended route information.
    """
    return {**route, **more_route_information}


def fix_wagon_depot(wagons_rows: list[list[tuple[int, str]]]
                    ) -> list[list[tuple[int, str]]]:
    """Fix the list of rows of wagons.

    :param wagons_rows: list[list[tuple]] - the list of rows of wagons.
    :return: list[list[tuple]] - list of rows of wagons.
    """

    # list1, list2, list3 = [], [], []
    # for wagon_row in wagons_rows:
    #     list1.append(wagon_row[0])
    #     list2.append(wagon_row[1])
    #     list3.append(wagon_row[2])
    # print([list1, list2, list3])

    a, b, c = zip(*wagons_rows)
    return [[*a], [*b], [*c]]
