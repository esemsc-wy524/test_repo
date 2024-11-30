import numpy as np
import pytest
from l4mod import matmul, zeromat, gauss
import l4mod

class TestUnits:
    @pytest.mark.parametrize("a, b, expected", [
        ([[1, 2, 3], [4, 5, 6], [7, 8, 9]],
         [[1, 2], [3, 4], [5, 6]],
         [[22, 28], [49, 64], [76, 100]]),
    ])
    def test_matmul(self, a, b, expected):
        assert matmul(a, b) == expected

    @pytest.mark.parametrize("a, b, expected", [
        (2, 1, [[0], [0]]),
        (1, 3, [[0, 0, 0]]),
    ])
    def test_zeromat(self, a, b, expected):
        assert zeromat(a, b) == expected

    @pytest.mark.parametrize("a, b, expected", [
        ([[2, 0, -1], [0, 5, 6], [0, -1, 1]],
         [[2], [1], [2]],
         (22.0, [[1.5], [-1.0], [1.0]])),
    ])
    def test_gauss(self, a, b, expected):
        assert gauss(a, b) == expected

class TestModule:
    @pytest.mark.parametrize("a, b, expected", [
        ([[1, 2, 3], [4, 5, 6], [7, 8, 9]],
         [[1, 2], [3, 4], [5, 6]],
         [[22, 28], [49, 64], [76, 100]]),
    ])
    def test_l4mod_matmul(self, a, b, expected):
        assert l4mod.matmul(a, b) == expected

    @pytest.mark.parametrize("a, b, expected", [
        (2, 1, [[0], [0]]),
        (1, 3, [[0, 0, 0]]),
    ])
    def test_l4mod_zeromat(self, a, b, expected):
        assert l4mod.zeromat(a, b) == expected

    @pytest.mark.parametrize("a, b, expected", [
        ([[2, 0, -1], [0, 5, 6], [0, -1, 1]],
         [[2], [1], [2]],
         (22.0, [[1.5], [-1.0], [1.0]])),
    ])
    def test_gauss(self, a, b, expected):
        assert l4mod.gauss(a, b) == expected