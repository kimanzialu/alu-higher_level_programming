"""Module for MyList class."""


class MyList(list):
    """sorted  list class"""

    def print_sorted(self):
        """Prints the list in ascending order."""
        print(sorted(self))
