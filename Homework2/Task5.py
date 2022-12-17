# Задача 5. Реализуйте алгоритм перемешивания списка. (рандомно поменять местами элементы списка между собой).

from random import randint


def generate_list(n):
    list = []
    for i in range(n):
        list.append(randint(-n, n))
    return list


def shuffled_list(gen_list):
    for i in range(len(gen_list)):
        random_num = randint(i, n - 1)
        temp = gen_list[i]
        gen_list[i] = gen_list[random_num]
        gen_list[random_num] = temp
    return gen_list


n = int(input('Введите число элементов (целое положительное число, больше 0): '))
if n > 0:
    list_numbers = generate_list(n)
    print(list_numbers)
    print(shuffled_list(list_numbers))
else:
    print(f'Введено некорректное значение: {n}. Необходимо ввести целое положительное число, больше 0')
