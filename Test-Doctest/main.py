def to_absolute(number):
    """
    >>> to_absolute(1)
    1
    >>> to_absolute(-1)
    1
    >>> to_absolute(0)
    0
    """
    if number > 0:
        return number
    else:
        return -number

def is_even(number):
    """
    >>> is_even(0)
    True
    >>> is_even(1)
    False
    >>> is_even(2)
    True
    """
    return number % 2 == 0
