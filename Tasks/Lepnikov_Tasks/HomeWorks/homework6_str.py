############################
# String operations module #
############################

from math import isfinite


def is_int(string):
    """
    Checks if a string passed as a parameter can be converted to an integer number.

    :param string: str
    :return: bool
    """
    try:
        int(string)
        return True
    except ValueError:
        return False


def is_float(string):
    """
    Checks if a string passed as a parameter can be converted to a float number.
    If string = NaN or infinity, False is returned.

    :param string: str
    :return: bool
    """
    try:
        if isfinite(float(string)):
            return True
        raise ValueError
    except ValueError:
        return False


def is_int_or_float(string):
    """
    Checks if a string passed as a parameter can be converted to an integer or float number.
    If string = NaN or infinity, False is returned.

    :param string: str
    :return: bool
    """
    return any([is_int(string), is_float(string)])


def from_string(string):
    """
    Converts a string to an integer or float number.

    :param string: str
    :return: int or float
    """
    return (float, int)[is_int(string)](string)
