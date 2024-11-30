import test_package
import numpy as np

def test_matrix_addition():
    A = np.array([[1, 2], [3, 4]])
    B = np.array([[5, 6], [7, 8]])
    expected = np.array([[6, 8], [10, 12]])
    np.testing.assert_array_equal(test_package.matrix_operations.matrix_addition(A, B), expected)

def test_elementwise_multiplication():
    A = np.array([1, 2, 3])
    B = np.array([4, 5, 6])
    expected = np.array([4, 10, 18])
    np.testing.assert_array_equal(test_package.array_operations.elementwise_multiplication(A, B), expected)

def test_calculate_mean():
    data = np.array([1, 2, 3, 4, 5])
    expected = 3
    assert test_package.statistics.calculate_mean(data) == expected