class BasicCalc:
    @staticmethod
    def add(first, second):
        return first + second

    @staticmethod
    def subtract(first, second):
        return first - second

    @staticmethod
    def multiply(first, second):
        return first * second

    @staticmethod
    def divide(first, second):
        return first / second


class MemoryCalc(BasicCalc):
    def __init__(self):
        self.memory = []

    def add(self, first, second=None):
        if second is None:
            second = self.memory[-1]

        result = first + second

        if self.memory:
            self.memory[-1] = result
        else:
            self.memory.append(result)

        return result

    def subtract(self, first, second=None):
        if second is None:
            second = self.memory[-1]

        result = first - second

        if self.memory:
            self.memory[-1] = result
        else:
            self.memory.append(result)

        return result

    def multiply(self, first, second=None):
        if second is None:
            second = self.memory[-1]

        result = first * second

        if self.memory:
            self.memory[-1] = result
        else:
            self.memory.append(result)

        return result

    def divide(self, first, second=None):
        if second is None:
            second = self.memory[-1]

        result = first / second

        if self.memory:
            self.memory[-1] = result
        else:
            self.memory.append(result)

        return result

    def memo_plus(self, value):
        if len(self.memory) < 3:
            self.memory.append(value)

    def memo_minus(self):
        return self.memory.pop()

    @property
    def memory_top(self):
        return self.memory[-1]