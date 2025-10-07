import random


def guess_number():
    number = random.randint(1, 100)
    attempts = 0
    while True:
        user_input = input("Введите число от 1 до 100: ")
        if not user_input.isdigit():
            print("Введите целое число.")
            continue
        guess = int(user_input)
        attempts += 1
        if guess < number:
            print("Загаданное число больше.")
        elif guess > number:
            print("Загаданное число меньше.")
        else:
            print(f"Поздравляем! Вы угадали число за {attempts} попыток.")
            break


if __name__ == "__main__":
    guess_number()