import pytest

import calculator_logger
from basic_calc import MemoryCalc


@pytest.fixture
def memory_calc():
    # MemoryCalc — синглтон, поэтому каждый раз возвращается один и тот же
    # объект. Чтобы тесты не влияли друг на друга, память очищаем вручную
    # перед каждым использованием. Область видимости — function (по умолчанию):
    # тесты должны быть изолированы друг от друга, поэтому каждый тест
    # получает "чистое" состояние памяти.
    calc = MemoryCalc()
    calc.memory.clear()
    return calc


@pytest.fixture
def memory_calc_with_value():
    # Отдельная фикстура для тестов, которым нужно заранее занесённое
    # значение в память (например, memo_minus, memory_top).
    # Область та же — function, по той же причине: изоляция тестов.
    # Отличий в scope от предыдущей фикстуры нет, разница только в
    # начальном состоянии памяти.
    calc = MemoryCalc()
    calc.memory.clear()
    calc.memory.append(10)
    return calc


@pytest.fixture(autouse=True)
def temp_log_file(tmp_path, monkeypatch):
    # Встроенная фикстура tmp_path создаёт временную папку на время
    # выполнения одного теста и pytest сам следит за её очисткой
    # (оставляет только несколько последних прогонов, старые удаляются
    # автоматически). monkeypatch подменяет путь к лог-файлу в модуле
    # calculator_logger, чтобы во время тестов калькулятор писал логи
    # именно туда, а не в основной calculator_log.txt проекта.
    temp_log = tmp_path / "calculator_log.txt"
    monkeypatch.setattr(calculator_logger, "LOG_FILE", temp_log)
    return temp_log