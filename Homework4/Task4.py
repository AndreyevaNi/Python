# Задача 4. Задана натуральная степень k. Сформировать случайным образом список коэффициентов (значения от 0 до 100)
# многочлена и записать в файл многочлен степени k.
# Пример:
# - k=2 => 2*x² + 4*x + 5 = 0 или x² + 5 = 0 или 10*x² = 0

from random import randint
import random


def get_polynomial(degree_num):
    coefficient_list = []
    for i in range(degree_num):
        coefficient_list.append(randint(0, 100))

    result_polynomial = ''
    i = 0
    j = 0
    while degree_num > 0:
        if coefficient_list[i] != 0:
            result_polynomial += (f'{coefficient_list[i]}x^{degree_num}{random.choice(["+", "-"])}')
        degree_num -= 1
        i += 1
    if coefficient_list[-1] != 0:
        result_polynomial += (f'{coefficient_list[-1]}=0')
    else:
        result_polynomial += ('=0')
    return result_polynomial


k = int(input('Введите целое положительное число k: '))

with open('Task4_Result.txt', 'w', encoding='utf8') as file:
    file.write(f'Результат: {get_polynomial(k)}')
print('Результат смотри в файле: Task4_Result.txt')
