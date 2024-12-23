import numpy as np
import copy


def gauss(a, b):
    """
    Given two matrices, `a` and `b`, with `a` square, the determinant
    of `a` (returned as `det`) and a matrix `x` (returned as `b`) such
    that a*x = b are returned. If `b` is the identity, then `x` is the
    inverse of `a`.

    Parameters
    ----------
    a : np.array or list of lists
        'n x n' array
    b : np. array or list of lists
        'm x n' array

    Returns
    -------
    det : float
        The determinant of a
    b : np.array or list of lists
        Solution of Ax=b

    Examples
    --------
    >>> a = [[2, 0, -1], [0, 5, 6], [0, -1, 1]]
    >>> b = [[2], [1], [2]]
    >>> det, x = gauss(a, b)
    >>> det
    22.0
    >>> x
    [[1.5], [-1.0], [1.0]]
    """
    a = copy.deepcopy(a)
    b = copy.deepcopy(b)
    n = len(a)
    p = len(b[0])
    det = 1.
    for i in range(n - 1):
        k = i
        for j in range(i + 1, n):
            if abs(a[j][i]) > abs(a[k][i]):
                k = j
        if k != i:
            a[i], a[k] = a[k], a[i]
            b[i], b[k] = b[k], b[i]
            det = -det

        for j in range(i + 1, n):
            t = a[j][i]/a[i][i]
            for k in range(i + 1, n):
                a[j][k] -= t*a[i][k]
            for k in range(p):
                b[j][k] -= t*b[i][k]

    for i in range(n - 1, -1, -1):
        for j in range(i + 1, n):
            t = a[i][j]
            for k in range(p):
                b[i][k] -= t*b[j][k]
        t = 1/a[i][i]
        det *= a[i][i]
        for j in range(p):
            b[i][j] *= t
    return det, b


def matmul(a, b):
    """
    Multiplies two matrices `a` and `b`.

    Parameters
    ----------
    a : list of lists
        The first matrix with dimensions `n x p`.
    b : list of lists
        The second matrix with dimensions `p x q`.

    Returns
    -------
    c : list of lists
        The resulting matrix with dimensions `n x q`.

    Raises
    ------
    ValueError
        If the number of columns in `a` does not match the number of rows in `b`.

    Examples
    --------
    >>> a = [[1, 2], [3, 4]]
    >>> b = [[5, 6], [7, 8]]
    >>> matmul(a, b)
    [[19, 22], [43, 50]]
    """
    n, p = len(a), len(a[0])
    p1, q = len(b), len(b[0])
    if p != p1:
        raise ValueError("Incompatible dimensions")
    c = zeromat(n, q)
    for i in range(n):
        for j in range(q):
            c[i][j] = sum(a[i][k]*b[k][j] for k in range(p))
    return c


def zeromat(p, q):
    """
    Creates a zero matrix with dimensions `p x q`.

    Parameters
    ----------
    p : int
        The number of rows in the matrix.
    q : int
        The number of columns in the matrix.

    Returns
    -------
    list of lists
        A `p x q` matrix filled with zeros.

    Examples
    --------
    >>> zeromat(2, 3)
    [[0, 0, 0], [0, 0, 0]]
    """
    return [[0]*q for i in range(p)]


# if __name__ == "__main__":
    # print('Running l4mod example:')
    # a = [[2, 0, -1], [0, 5, 6], [0, -1, 1]]
    # b = [[2], [1], [2]]
    # print('Setting the matrix A as:')
    # print('a')
    # print('Setting b as:')
    # print('b')
    # det, x = gauss(a, b)
    # print('The determinant of A is:')
    # print(det)
    # print('The solution of Ax=b is:')
    # print(x)
