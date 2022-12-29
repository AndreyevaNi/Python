# Задача 5. Даны два файла, в каждом из которых находится запись многочлена.
# Задача - сформировать файл, содержащий сумму многочленов.


import random


def write_file(file_name, str_polynomial):
    with open(file_name, 'w') as data:
        data.write(str_polynomial)


def create_polynomial(number):
    lst = [random.randint(0, 100) for i in range(number + 1)]
    return lst


def create_str_polynomial(lst):
    lst = lst[::-1]
    wr = ''
    if len(lst) < 1:
        wr = 'x = 0'
    else:
        for i in range(len(lst)):
            if i != len(lst) - 1 and lst[i] != 0 and i != len(lst) - 2:
                wr += f'{lst[i]}x^{len(lst) - i - 1}'
                if lst[i + 1] != 0 or lst[i + 2] != 0:
                    wr += ' + '
            elif i == len(lst) - 2 and lst[i] != 0:
                wr += f'{lst[i]}x'
                if lst[i + 1] != 0 or lst[i + 2] != 0:
                    wr += ' + '
            elif i == len(lst) - 1 and lst[i] != 0:
                wr += f'{lst[i]} = 0'
            elif i == len(lst) - 1 and lst[i] == 0:
                wr += ' = 0'
    return wr


def get_degree_polynomial(num):
    if 'x^' in num:
        i = num.find('^')
        num = int(num[i + 1:])
    elif ('x' in num) and ('^' not in num):
        num = 1
    else:
        num = -1
    return num


def get_coefficient_polynomial(coef):
    if 'x' in coef:
        i = coef.find('x')
        coefficient = int(coef[:i])
    return coefficient


def parsing_polynomial(str_poly):
    str_poly = str_poly[0].replace(' ', '').split('=')
    str_poly = str_poly[0].split('+')
    lst = []
    len_poly = len(str_poly)
    k = 0
    if get_degree_polynomial(str_poly[-1]) == -1:
        lst.append(int(str_poly[-1]))
        len_poly -= 1
        k = 1
    i = 1
    ii = len_poly - 1
    while ii >= 0:
        if get_degree_polynomial(str_poly[ii]) != -1 and get_degree_polynomial(str_poly[ii]) == i:
            lst.append(get_coefficient_polynomial(str_poly[ii]))
            ii -= 1
            i += 1
        else:
            lst.append(0)
            i += 1
    return lst


k1 = int(input("Введите целое положительное число k для первого многочлена: "))
k2 = int(input("Введите целое положительное число k для второго многочлена: "))
coef1 = create_polynomial(k1)
coef2 = create_polynomial(k2)
write_file("Task5_FirstFile.txt", create_str_polynomial(coef1))
write_file("Task5_SecondFile.txt", create_str_polynomial(coef2))

with open('Task5_FirstFile.txt', 'r') as data:
    str_polynomial1 = data.readlines()
with open('Task5_SecondFile.txt', 'r') as data:
    str_polynomial2 = data.readlines()

lst1 = parsing_polynomial(str_polynomial1)
lst2 = parsing_polynomial(str_polynomial2)
temp1 = len(lst1)
if len(lst1) > len(lst2):
    temp1 = len(lst2)
lst_new = [lst1[i] + lst2[i] for i in range(temp1)]
if len(lst1) > len(lst2):
    temp2 = len(lst1)
    for i in range(temp1, temp2):
        lst_new.append(lst1[i])
else:
    temp2 = len(lst2)
    for i in range(temp1, temp2):
        lst_new.append(lst2[i])
write_file("Task5_ResultFile.txt", create_str_polynomial(lst_new))
with open('Task5_ResultFile.txt', 'r') as data:
    str_polynomial_result = data.readlines()
