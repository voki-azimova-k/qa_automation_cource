import pytest

from basic_calc import BasicCalc


@pytest.mark.critical
def test_add_positive():
    assert BasicCalc.add(2, 3) == 5


@pytest.mark.critical
def test_add_negative_invalid_type():
    # Невалидный аргумент (строка) должен восприниматься как 0
    assert BasicCalc.add("abc", 3) == 3