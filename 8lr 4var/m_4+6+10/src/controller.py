from .calculator import Calculator
from .view import show_result, show_error

def run():
    try:
        a = int(input("Введите a: "))
        b = int(input("Введите b: "))
        op = input("Операция (+, -, *, /): ")

        calc = Calculator()

        if op == "+":
            result = calc.add(a, b)
        elif op == "-":
            result = calc.subtract(a, b)
        elif op == "*":
            result = calc.multiply(a, b)
        elif op == "/":
            result = calc.divide(a, b)
        else:
            show_error("Неизвестная операция")
            return

        show_result(result)

    except ValueError as e:
        show_error(str(e))

if __name__ == "__main__":
    run()
