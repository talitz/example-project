from random import randint


def random_number_generator(start, stop):
    """Returns a random number between start and stop.

    Parameters
    ----------
    start : int
        Lowest possible number.
    stop : int
        Highest possible number.

    Returns
    -------
    int
        A random integer between start and stop.

    Examples
    --------
    >>> random_number_generator(0, 10)
    5  #random

    """
    return randint(start, stop)
