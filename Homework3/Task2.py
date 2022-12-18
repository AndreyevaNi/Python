# Задача 2. Напишите программу, которая найдёт произведение пар чисел списка.
# Парой считаем первый и последний элемент, второй и предпоследний и т.д.
# Пример:
# - [2, 3, 4, 5, 6] => [12, 15, 16];
# - [2, 3, 5, 6] => [12, 15]
from random import randint


def generated_list(n):
    list_gen = []
    for i in range(n):
        list_gen.append(randint(-n, n))
    return list_gen


def product_pairs_numbers(list_num):
    list_product_pairs_numbers = []
    count = -1
    i = 0
    while i < len(list_num) / 2:
        list_product_pairs_numbers.append(list_num[i] * list_num[count])
        count -= 1
        i += 1
    return list_product_pairs_numbers


n = int(input('Введите число элементов списка (целое положительное число, больше 0): '))

if n > 0:
    list_numbers = generated_list(n)
    print(f'Список из {n} элементов: {list_numbers}')
    print(f'Список произведений пар чисел {product_pairs_numbers(list_numbers)}')

else:
    print(f'Введено некорректное значение: {n}. Необходимо ввести целое положительное число, больше 0')
