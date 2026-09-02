import pytest


@pytest.mark.parametrize(
    "value, expected_top",
    [
        (5, 5),
        (0, 0),
        (-3, -3),
        (2.5, 2.5),
        ("abc", 0),  # невалидное значение должно восприниматься как 0
    ],
)
def test_memo_plus_parametrized(memory_calc, value, expected_top):
    # Фикстура memory_calc даёт "чистый" калькулятор с пустой памятью
    # перед каждым запуском теста, поэтому можно безопасно проверять
    # результат memo_plus без влияния других тестов друг на друга.
    memory_calc.memo_plus(value)
    assert memory_calc.memory_top == expected_top


def test_memo_minus_with_prefilled_value(memory_calc_with_value):
    # Используем фикстуру с предзаполненной памятью (значение 10),
    # чтобы проверить, что memo_minus корректно извлекает его.
    result = memory_calc_with_value.memo_minus()
    assert result == 10
    assert memory_calc_with_value.memory_top == 0