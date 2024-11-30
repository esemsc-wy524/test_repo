import numpy as np
import pytest


from test_package.linear_algebra.matrix_operations import (
    matrix_addition, matrix_subtraction, matrix_determinant, matrix_inverse
)
from test_package.linear_algebra.array_operations import (
    elementwise_multiplication, elementwise_division
)
from test_package.statistics.statistics import (
    calculate_mean, calculate_median, calculate_std
)

from test_package.funcs import (
    complex_squre_root, mean, prime
)

def test_matrix_addition():
    A = np.array([[1, 2], [3, 4]])
    B = np.array([[5, 6], [7, 8]])
    expected = np.array([[6, 8], [10, 12]])
    np.testing.assert_array_equal(matrix_addition(A, B), expected)

def test_elementwise_multiplication():
    A = np.array([1, 2, 3])
    B = np.array([4, 5, 6])
    expected = np.array([4, 10, 18])
    np.testing.assert_array_equal(elementwise_multiplication(A, B), expected)

def test_calculate_mean():
    data = np.array([1, 2, 3, 4, 5])
    expected = 3
    assert calculate_mean(data) == expected
