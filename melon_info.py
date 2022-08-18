"""Print out all the melons in our inventory."""


from melons import melon


def print_melon():
    """Print each melon with corresponding attribute information."""

    for name, value_dict in melon.items():
        print(name.upper())

        for attribute, value in melon[name].items():
            print(f"{attribute} : {value}")
        print("--------------------------------------")

print(print_melon())