import re
import basic_calc


operations = {
    "+": basic_calc.BasicCalc.add,
    "-": basic_calc.BasicCalc.subtract,
    "*": basic_calc.BasicCalc.multiply,
    "/": basic_calc.BasicCalc.divide,
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
