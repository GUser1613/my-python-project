def squares_dict(n: int):
    return {i: i**2 for i in range(1, n + 1)}


def main():
    number = int(input("Введите число: "))
    print(squares_dict(number))


if __name__ == "__main__":
    main()