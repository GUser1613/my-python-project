def add(x, y):
    return x + y


def subtract(x, y):
    return x - y


def multiply(x, y):
    return x * y


def divide(x, y):
    if y == 0:
        return "Ошибка: деление на ноль!"
    return x / y


def main():
    choice = input("Выберите операцию (+, -, *, /): ")

    try:
        num1 = float(input("Введите первое число: "))
        num2 = float(input("Введите второе число: "))
    except ValueError:
        print("Ошибка: нужно вводить только числа!")
        return

    if choice == "+":
        result = add(num1, num2)
    elif choice == "-":
        result = subtract(num1, num2)
    elif choice == "*":
        result = multiply(num1, num2)
    elif choice == "/":
        result = divide(num1, num2)
    else:
        print("Ошибка: неизвестная операция!")
        return

    print("Результат:", result)


if __name__ == "__main__":
    main()