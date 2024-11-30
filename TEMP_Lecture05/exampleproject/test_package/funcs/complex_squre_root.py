import math


def complex_square_roots(number):
    """
    Compute the complex square roots of a real number.

    Parameters
    ----------
    number : float
        A real number for which the complex square roots are to be calculated.

    Returns
    -------
    tuple of complex
        A tuple containing the two complex square roots of the given number.
        If the number is positive, the roots will be real. If the number is zero, both roots will be zero.
        If the number is negative, the roots will be complex.

    Raises
    ------
    ValueError
        If the input is not a real number.

    Examples
    --------
    >>> complex_square_roots(4)
    ((2+0j), (-2+0j))

    >>> complex_square_roots(-4)
    (2j, -2j)

    >>> complex_square_roots(0)
    (0j, 0j)
    """
    if not isinstance(number, (int, float)):
        raise ValueError("Input must be a real number.")

    if number > 0:
        root1 = complex(math.sqrt(number), 0)
        root2 = complex(-math.sqrt(number), 0)
    elif number == 0:
        root1 = root2 = complex(0, 0)
    else:
        root1 = complex(0, math.sqrt(-number))
        root2 = complex(0, -math.sqrt(-number))

    return root1, root2


if __name__ == '__main__':
    import doctest

    doctest.testmod()