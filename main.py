import re


def add(first, second=None):
    if second is None:
        result = 0
        for number in first:
            result += number
        return result

    return first + second


def subtract(first, second):
    return first - second


def multiply(first, second):
    return first * second


def divide(first, second):
    return first / second


operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide,
}

pattern = r"\d+(\.\d+)?[+\-*/]\d+(\.\d+)?"

while True:
    expression = input("Enter a mathematical expression: ")

    if re.fullmatch(pattern, expression):
        break

    print("Invalid input")

parts = re.split(r"([+\-*/])", expression)

first = float(parts[0])
operator = parts[1]
second = float(parts[2])

result = operations[operator](first, second)

print(result)