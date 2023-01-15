# Задача 2. Создайте программу для игры с конфетами человек против человека.
# Условие задачи: На столе лежит 2021 конфета.
#         Играют два игрока делая ход друг после друга. Первый ход определяется жеребьёвкой.
#         За один ход можно забрать не более чем 28 конфет. Все конфеты оппонента достаются сделавшему последний ход.
#         Сколько конфет нужно взять первому игроку, чтобы забрать все конфеты у своего конкурента?
# a) Добавьте игру против бота
# b) Подумайте как наделить бота ""интеллектом""

# Здесь вариант человек против человека:
from random import randint


def get_move(name):
    x = int(
        input(f"{name}, укажите количество конфет, которое возьмете от 1 до 28: "))
    while x < 1 or x > 28:
        x = int(input(f"{name}, введите корректное количество конфет: "))
    return x


def get_status(name, k, counter, value):
    print(
        f"Ход сделал {name},  взял {k} конфет, теперь у него {counter}. Осталось всего {value}.")


player1 = input("Введите имя первого игрока: ")
player2 = input("Введите имя второго игрока: ")
value = int(input("Введите количество конфет всего: "))
flag = randint(0, 2)  # Жребий
if flag:
    print(f"Первым ходит {player1}")
else:
    print(f"Первым ходит {player2}")

counter1 = 0
counter2 = 0

while value > 28:
    if flag:
        k = get_move(player1)
        counter1 += k
        value -= k
        flag = False
        get_status(player1, k, counter1, value)
    else:
        k = get_move(player2)
        counter2 += k
        value -= k
        flag = True
        get_status(player2, k, counter2, value)

if flag:
    print(f"Выиграл {player1}")
else:
    print(f"Выиграл {player2}")
