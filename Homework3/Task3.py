# Задача 3. Задайте список из вещественных чисел. Напишите программу, которая найдёт разницу между
# максимальным и минимальным значением дробной части элементов.
# Пример:
# - [1.1, 1.2, 3.1, 5, 10.01] => 0.19

# ***********************Дополнительное ограничение, которое используется при решении******************************
# минимальное значение ищем только для вещественных чисел, у целых чисел дробной части нет, поэтому они не учитываются.
from random import randint


def generated_list(n):
    list_gen = []
    for i in range(n):
        list_gen.append(round(randint(0, n) / n + n, 2))
    return list_gen


def fractional_part_difference(list_num):
    fractional_part_max_min = []
    for i in range(len(list_num)):
        if list_num[i] % 1 != 0:
            fractional_part_max_min.append(list_num[i] % 1)
    return max(fractional_part_max_min) - min(fractional_part_max_min)


n = int(input('Введите число элементов списка (целое положительное число, больше 0): '))
if n > 0:
    list_numbers = generated_list(n)
    print(f'Список из {n} элементов: {list_numbers}')
    print(f'Разница между максимальной и минимальной дробной частью составляет: '
          f'{fractional_part_difference(list_numbers):.2f}')

else:
    print(f'Введено некорректное значение: {n}. Необходимо ввести целое положительное число, больше 0')
