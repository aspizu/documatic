"""Module docstring."""


class MyCoolClass:
    """Class docstring.

    Long summary.
    """

    def __init__(self, name: str, age: int):
        self.name: str = name
        """Name attribute."""
        self.age: int = age
        """Age attribute."""


def my_cool_function(argument: int) -> None:
    """
    Function docstring.

    Args:
        argument: Argument docstring.

    Returns:
        Cool sentinel value.

    Raises:
        NotImplementedError: Raises docstring.
    """
    raise NotImplementedError
