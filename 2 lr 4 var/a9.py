def recursive_sum(n):
    if n <= 0:
        return 0
    return n + recursive_sum(n - 1)


def main():
    number = input("Введите положительное число: ")
    if number.isdigit():
        print(recursive_sum(int(number)))
    else:
        print("Введите целое положительное число.")


if __name__ == "__main__":
    main()