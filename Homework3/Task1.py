# Задание 1. Задайте список из нескольких чисел. Напишите программу, которая найдёт сумму элементов списка, стоящих на нечётной позиции.
# Пример:
# - [2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9, ответ: 12.


# Дополнительное условие для решения: Сумму элементов ищем для нечетных индексов, при этом 0 - это всегда четное число.
# https://ru.wikipedia.org/wiki/%D0%A7%D1%91%D1%82%D0%BD%D0%BE%D1%81%D1%82%D1%8C_%D0%BD%D1%83%D0%BB%D1%8F#%D0%9F%D0%BE%D1%87%D0%B5%D0%BC%D1%83_%D0%BD%D0%BE%D0%BB%D1%8C_%D1%8F%D0%B2%D0%BB%D1%8F%D0%B5%D1%82%D1%81%D1%8F_%D1%87%D1%91%D1%82%D0%BD%D1%8B%D0%BC
from random import randint


def generated_list(n):
    list_gen = []
    for i in range(n):
        list_gen.append(randint(-n, n))
    return list_gen


def sum_elements_noneven_indexes(list_num):
    sum = 0
    for i in range(1, len(list_num), 2):
        sum += list_num[i]
    return sum


n = int(input('Введите число элементов списка (целое положительное число, больше 0): '))

if n > 0:
    list_numbers = generated_list(n)
    print(f'Список из {n} элементов: {list_numbers}')
    print(f'Сумма элементов для нечетных индексов = {sum_elements_noneven_indexes(list_numbers)}')
else:
    print(f'Введено некорректное значение: {n}. Необходимо ввести целое положительное число, больше 0')
