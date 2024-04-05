from random import randint

player1 = input("Игрок 1, введите Ваше имя:")
player2 = input("Игрок 2, введите Ваше имя:")
rand = randint(1, 50)
your_number = int(input("Введите число"))
win = "Вы угадали число и выиграли!!!"
print(f'Начинаем игру, Вам нужно угадать число от ')
print(f'{player1} введите Ваше число: ')


def play():
    if your_number > rand:
        print("Загаданное число меньше!")
    elif your_number < rand:
        print("Загаданное число больше!")
    elif your_number == rand:
        print(win)
    return
