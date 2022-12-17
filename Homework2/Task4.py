# Задача 4. Задайте список из N элементов, заполненных числами из промежутка [-N, N].
# Найдите произведение элементов на указанных позициях.
# Позиции хранятся в отдельном списке( пример n=4, lst1=[4,-2,1,3] - список на основе n, а позиции элементов lst2=[3,1].

from random import randint


def generated_list(n):
    list = []
    for i in range(n):
        list.append(randint(-n, n))
    return list


def get_positions(n):
    list_pos = []
    for i in range(2):
        list_pos.append(randint(0, n - 1))
    return list_pos


n = int(input('Введите число N (целое положительное число, больше 0): '))
if n > 0:
    list_numbers = generated_list(n)
    print(f'Список из {n} элементов: {list_numbers}')
    list_positions = get_positions(n)
    print(f'Список индексов элементов для последующего перемножения: {list_positions}')
    product_elements_in_positions = list_numbers[list_positions[0]] * list_numbers[list_positions[1]]
    print(f'Произведение элементов на заданных позициях: {product_elements_in_positions}')
else:
    print(f'Введено некорректное значение: {n}. Необходимо ввести целое положительное число, больше 0')
