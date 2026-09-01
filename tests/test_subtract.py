import pytest

from basic_calc import BasicCalc


@pytest.mark.critical
def test_subtract_negative_invalid_type():
    # Невалидный аргумент (строка) должен восприниматься как 0
    assert BasicCalc.subtract("abc", 4) == -4

@pytest.mark.critical
@pytest.mark.xfail(reason="Внесён баг: subtract использует + вместо - (демонстрация xfail)")
def test_subtract_positive():
    assert BasicCalc.subtract(10, 4) == 6