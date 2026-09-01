import pytest

from basic_calc import BasicCalc


@pytest.mark.critical
def test_multiply_positive():
    assert BasicCalc.multiply(3, 4) == 12


@pytest.mark.critical
def test_multiply_negative_invalid_type():
    # Невалидный аргумент (строка) должен восприниматься как 0
    assert BasicCalc.multiply("abc", 4) == 0