from acsefunctions import factorial, gamma, bessel_j
import numpy as np

print(bessel_j(np.array([0, 1]), 1.0))

# def single_factorial(n):
#     if n == 0 or n == 1:
#         return 1
#     else:
#         result = 1
#         for i in range(2, n + 1):
#             result *= i
#         return result
#
# def factorial(x):
#     x = np.asarray(x)
#
#     # Check if x is a scalar (0-D array)
#     if x.ndim == 0:
#         return single_factorial(x)
#
#     # Apply factorial computation on each element if x is an array
#     return np.array([single_factorial(xi) for xi in x])
#
# print(factorial(0))