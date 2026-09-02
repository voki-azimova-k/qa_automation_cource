from basic_calc import MemoryCalc


def test_memory_calc_add_with_memory(memory_calc):
    memory_calc.add(5, 3)
    assert memory_calc.memory_top == 8


def test_memory_calc_add_uses_memory_as_second_argument(memory_calc):
    memory_calc.memo_plus(10)
    memory_calc.add(5)
    assert memory_calc.memory_top == 15


def test_memory_calc_subtract(memory_calc):
    memory_calc.subtract(10, 4)
    assert memory_calc.memory_top == 6


def test_memory_calc_multiply(memory_calc):
    memory_calc.multiply(3, 4)
    assert memory_calc.memory_top == 12


def test_memory_calc_divide(memory_calc):
    memory_calc.divide(10, 2)
    assert memory_calc.memory_top == 5


def test_memory_calc_preserves_state_between_instances():
    # Регрессионный тест: подтверждает исправление синглтона —
    # __init__ больше не сбрасывает память при повторном MemoryCalc(),
    # если объект уже был создан ранее.
    first_calc = MemoryCalc()
    first_calc.memory.clear()
    first_calc.memo_plus(42)

    second_calc = MemoryCalc()

    assert first_calc is second_calc
    assert second_calc.memory_top == 42