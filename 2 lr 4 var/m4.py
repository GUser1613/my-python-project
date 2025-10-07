def gcd(a: int, b: int):
    while b:
        a, b = b, a % b
    return a


def main():
    x = int(input("Введите первое число: "))
    y = int(input("Введите второе число: "))
    print(f"НОД чисел {x} и {y} равен {gcd(x, y)}")


if __name__ == "__main__":
    main()