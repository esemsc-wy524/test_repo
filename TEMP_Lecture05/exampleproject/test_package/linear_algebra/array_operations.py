import numpy as np


def elementwise_multiplication(A, B):
    """Multiplies two arrays element-wise.

    Parameters
    ----------
    A : np.ndarray
        First array.
    B : np.ndarray
        Second array.

    Returns
    -------
    np.ndarray
        The element-wise product of A and B.
    """
    return np.multiply(A, B)


def elementwise_division(A, B):
    """Divides two arrays element-wise.

    Parameters
    ----------
    A : np.ndarray
        Numerator array.
    B : np.ndarray
        Denominator array.

    Returns
    -------
    np.ndarray
        The element-wise division of A by B.

    Raises
    ------
    ZeroDivisionError
        If any element of B is zero.
    """
    return np.divide(A, B)