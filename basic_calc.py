from calculator_exceptions import CalculatorZeroDivisionError
from calculator_logger import log_operation, log_error


def validate_number(value):
    if isinstance(value, (int, float)):
        return value

    return 0


class BasicCalc:
    @staticmethod
    def add(first, second):
        first = validate_number(first)
        second = validate_number(second)

        result = first + second
        log_operation("add", [first, second], result)

        return result

    @staticmethod
    def subtract(first, second):
        first = validate_number(first)
        second = validate_number(second)

        result = first - second
        log_operation("subtract", [first, second], result)

        return result

    @staticmethod
    def multiply(first, second):
        first = validate_number(first)
        second = validate_number(second)

        result = first * second
        log_operation("multiply", [first, second], result)

        return result

    @staticmethod
    def divide(first, second):
        first = validate_number(first)
        second = validate_number(second)

        if second == 0:
            error = CalculatorZeroDivisionError("Division by zero")
            log_error("divide", [first, second], error)
            raise error

        result = first / second
        log_operation("divide", [first, second], result)

        return result


class MemoryCalc(BasicCalc):
    def __init__(self):
        self.memory = []

    def add(self, first, second=None):
        if second is None:
            second = self.memory_top

        first = validate_number(first)
        second = validate_number(second)

        result = first + second

        if self.memory:
            self.memory[-1] = result
        else:
            self.memory.append(result)

        log_operation("add", [first, second], result)

        return result

    def subtract(self, first, second=None):
        if second is None:
            second = self.memory_top

        first = validate_number(first)
        second = validate_number(second)

        result = first - second

        if self.memory:
            self.memory[-1] = result
        else:
            self.memory.append(result)

        log_operation("subtract", [first, second], result)

        return result

    def multiply(self, first, second=None):
        if second is None:
            second = self.memory_top

        first = validate_number(first)
        second = validate_number(second)

        result = first * second

        if self.memory:
            self.memory[-1] = result
        else:
            self.memory.append(result)

        log_operation("multiply", [first, second], result)

        return result

    def divide(self, first, second=None):
        if second is None:
            second = self.memory_top

        first = validate_number(first)
        second = validate_number(second)

        if second == 0:
            error = CalculatorZeroDivisionError("Division by zero")
            log_error("divide", [first, second], error)
            raise error

        result = first / second

        if self.memory:
            self.memory[-1] = result
        else:
            self.memory.append(result)

        log_operation("divide", [first, second], result)

        return result

    def memo_plus(self, value):
        value = validate_number(value)

        if len(self.memory) < 3:
            self.memory.append(value)

    def memo_minus(self):
        if self.memory:
            return self.memory.pop()

        return 0

    @property
    def memory_top(self):
        if self.memory:
            return self.memory[-1]

        return 0