"""Functions to manage a users shopping cart items."""


def add_item(current_cart: dict[str, int],
             items_to_add: list[str]) -> dict[str, int]:
    """Add items to shopping cart.

    :param current_cart: dict - the current shopping cart.
    :param items_to_add: iterable - items to add to the cart.
    :return: dict - the updated user cart dictionary.
    """
    for item in items_to_add:
        current_cart[item] = current_cart.get(item, 0) + 1
    return current_cart


def read_notes(notes: list[str]) -> dict[str, int]:
    """Create user cart from an iterable notes entry.

    :param notes: iterable of items to add to cart.
    :return: dict - a user shopping cart dictionary.
    """
    return add_item({}, notes)


def update_recipes(ideas: dict, recipe_updates: dict) -> dict:
    """Update the recipe ideas dictionary.

    :param ideas: dict - The "recipe ideas" dict.
    :param recipe_updates: dict - dictionary with updates for the ideas
    section.
    :return: dict - updated "recipe ideas" dict.
    """
    for key, value in recipe_updates:
        ideas[key] = value
    return ideas


def sort_entries(cart: dict) -> dict:
    """Sort a users shopping cart in alphabetically order.

    :param cart: dict - a users shopping cart dictionary.
    :return: dict - users shopping cart sorted in alphabetical order.
    """
    new_cart = {}
    for key in sorted(list(cart.keys())):
        new_cart[key] = cart[key]
    return new_cart


def send_to_store(cart: dict[str],
                  aisle_mapping: dict[str, list[str, bool]]
                  ) -> dict[str, list[int, str, bool]]:
    """Combine users order to aisle and refrigeration information.

    :param cart: dict - users shopping cart dictionary.
    :param aisle_mapping: dict - aisle and refrigeration information
    dictionary.
    :return: dict - fulfillment dictionary ready to send to store.
    """
    for item in cart:
        aisle_mapping[item].insert(0, cart[item])

    new_cart = {}
    for key in sorted(list(aisle_mapping.keys()), reverse=True):
        new_cart[key] = aisle_mapping[key]
    return new_cart


def update_store_inventory(fulfillment_cart: dict[str, list[int, str, bool]],
                           store_inventory: dict[str, list[int, str, bool]]
                           ) -> dict[str, list[int, str, bool]]:
    """Update store inventory levels with user order.

    :param fulfillment cart: dict - fulfillment cart to send to store.
    :param store_inventory: dict - store available inventory
    :return: dict - store_inventory updated.
    """
    for key, value in fulfillment_cart.items():
        result = int(store_inventory[key][0]) - int(value[0])
        store_inventory[key][0] = 'Out of Stock' if result <= 0 else result
    return store_inventory
