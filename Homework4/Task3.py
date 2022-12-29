# Задача 3. Задайте последовательность чисел.
# Напишите программу, которая выведет список неповторяющихся элементов исходной последовательности.

# Т.е. вывести только те элементы, которые заданы 1 раз, если элемент задан более 1 раза, то его не выводим.
import random


def get_list_number(n, min, max) -> list:
    number_list = [random.randint(min, max)]
    for i in range(1, n):
        number_list.append(random.randint(min, max))
    return number_list


def list_unique_numbers(source_list) -> list:
    unique_num_list = [source_list[0]]
    list_repeat = []
    for i in range(1, len(source_list)):
        for j in range(len(unique_num_list)):
            if source_list[i] == unique_num_list[j]:
                list_repeat.append(unique_num_list[j])
                break
            elif j == len(unique_num_list) - 1:
                unique_num_list.append(source_list[i])
    unique_num_list = list(set(unique_num_list) - set(list_repeat))
    print(f'Справочно: Список повторяющихся значений для исключения из результирующего списка: {list_repeat}')
    return unique_num_list


n = int(input(f'Задайте количество элементов последовательности (целое положительное число, например, 10): '))
list_source = get_list_number(n, 10, 20)
print(f'Исходная последовательность чисел: {list_source} ')
print(f'Итоговая последовательность чисел без повторов: {list_unique_numbers(list_source)}')
