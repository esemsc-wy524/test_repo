import numpy as np


def matrix_addition(A, B):
    """Adds two matrices.

    Parameters
    ----------
    A : np.ndarray
        First matrix.
    B : np.ndarray
        Second matrix.

    Returns
    -------
    np.ndarray
        The result of A + B.
    """
    return np.add(A, B)


def matrix_subtraction(A, B):
    """Subtracts two matrices.

    Parameters
    ----------
    A : np.ndarray
        First matrix.
    B : np.ndarray
        Second matrix.

    Returns
    -------
    np.ndarray
        The result of A - B.
    """
    return np.subtract(A, B)


def matrix_determinant(A):
    """Calculates the determinant of a matrix.

    Parameters
    ----------
    A : np.ndarray
        Input matrix.

    Returns
    -------
    float
        The determinant of the matrix A.
    """
    return np.linalg.det(A)


def matrix_inverse(A):
    """Calculates the inverse of a matrix.

    Parameters
    ----------
    A : np.ndarray
        Input matrix.

    Returns
    -------
    np.ndarray
        The inverse of the matrix A.

    Raises
    ------
    LinAlgError
        If the matrix is singular.
    """
    return np.linalg.inv(A)