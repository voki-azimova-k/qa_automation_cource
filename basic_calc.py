from calculator_exceptions import CalculatorZeroDivisionError
from calculator_logger import log_operation, log_error


def validate_number(value):
    if isinstance(value, (int, float)):
        return value

    return 0


class BasicCalc:
    _instances = {}

    def __new__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super().__new__(cls)

        return cls._instances[cls]

    @staticmethod
    def add(first, second=None):
        if second is None:
            result = sum(validate_number(item) for item in first)
            log_operation(operation="add", arguments=list(first), result=result)

            return result

        first = validate_number(first)
        second = validate_number(second)

        result = first + second
        log_operation(operation="add", arguments=[first, second], result=result)

        return result

    @staticmethod
    def subtract(first, second):
        first = validate_number(first)
        second = validate_number(second)

        result = first - second
        log_operation(operation="subtract", arguments=[first, second], result=result)

        return result

    @staticmethod
    def multiply(first, second):
        first = validate_number(first)
        second = validate_number(second)

        result = first * second
        log_operation(operation="multiply", arguments=[first, second], result=result)

        return result

    @staticmethod
    def divide(first, second):
        first = validate_number(first)
        second = validate_number(second)

        if second == 0:
            error = CalculatorZeroDivisionError("Division by zero")
            log_error(operation="divide", arguments=[first, second], error=error)
            raise error

        result = first / second
        log_operation(operation="divide", arguments=[first, second], result=result)

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

        log_operation(operation="add", arguments=[first, second], result=result)

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

        log_operation(operation="subtract", arguments=[first, second], result=result)

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

        log_operation(operation="multiply", arguments=[first, second], result=result)

        return result

    def divide(self, first, second=None):
        if second is None:
            second = self.memory_top

        first = validate_number(first)
        second = validate_number(second)

        if second == 0:
            error = CalculatorZeroDivisionError("Division by zero")
            log_error(operation="divide", arguments=[first, second], error=error)
            raise error

        result = first / second

        if self.memory:
            self.memory[-1] = result
        else:
            self.memory.append(result)

        log_operation(operation="divide", arguments=[first, second], result=result)

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


if __name__ == "__main__":
    first_calc = MemoryCalc()
    second_calc = MemoryCalc()

    print("Is it the same instance?", first_calc is second_calc)
    print("First calc id:", id(first_calc))
    print("Second calc id:", id(second_calc))
   