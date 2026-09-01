import pytest

from basic_calc import BasicCalc
from calculator_exceptions import CalculatorZeroDivisionError


@pytest.mark.critical
def test_divide_positive():
    assert BasicCalc.divide(10, 2) == 5


@pytest.mark.critical
def test_divide_negative_zero_division():
    with pytest.raises(CalculatorZeroDivisionError):
        BasicCalc.divide(10, 0)

@pytest.mark.parametrize(
    "first, second, expected",
    [
        (10, 2, 5.0),       # целочисленное деление без остатка
        (7, 2, 3.5),        # деление с дробным результатом
        (-10, 2, -5.0),     # отрицательное число в делимом
        (10, -2, -5.0),     # отрицательное число в делителе
        (5, 0.5, 10.0),     # деление на дробное число
    ],
)
def test_divide_parametrized(first, second, expected):
    # Функцию divide выбрали для параметризации, потому что в ней
    # больше всего разных сценариев поведения (целые/дробные числа,
    # положительные/отрицательные значения), в отличие от add/subtract/multiply,
    # где логика значительно проще и однотипнее.
    assert BasicCalc.divide(first, second) == expected