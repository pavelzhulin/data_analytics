import pytest
from src.matrix.matrix_analysis import MatrixAnalysis as Ma


def test_sum():
    assert Ma.sum([[2, 3, 1], [1, 2, 1]]) == 10
    assert Ma.sum([[6, 3, 6, 2], [4, 7, 2, 1]]) == 31
    assert Ma.sum([[-5, 0, 2, -4], [2, 6, -8, 9]]) == 2


def test_max():
    assert Ma.max([[6, 3, 6, 2], [4, 7, 2, 1]]) == 7
    assert Ma.max([[-5, 0, 2, -4], [2, 6, -8, 9]]) == 9
    assert Ma.max([[3, 3, 3, 3], [3, 3, 3, 3]]) == 3
    assert Ma.max([[3, 3, 4, 3], [3, 3, 3, 4]]) == 4


def test_min():
    assert Ma.min([[6, 3, 6, 2], [4, 7, 2, 1]]) == 1
    assert Ma.min([[-5, 0, 2, -4], [2, 6, -8, 9]]) == -8
    assert Ma.min([[3, 3, 4, 3], [3, 3, 3, 4]]) == 3


def test_mode():
    assert Ma.mode([[6, 3, 6, 2], [4, 7, 2, 1]]) == 6
    assert Ma.mode([[-5, 0, 2, -4], [7, 6, -8, 9]]) == -5
    assert Ma.mode([[3, 6, 3], [5, 9, 5]]) == 3
    assert Ma.min([[3, 3, 3, 3], [3, 3, 3, 3]]) == 3



