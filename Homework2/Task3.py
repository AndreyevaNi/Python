# Задание 3. Задайте список из n чисел последовательности (1+1/n)**n и выведите на экран их сумму.

def list_elements(n):
    list = []
    for i in range(1, n + 1):
        list.append(round((1 + 1 / i) ** i, 4))
    return list


def sum(list):
    sum = 0
    for i in list:
        sum += i
    return round(sum, 4)


n = int(input('Введите целое положительное число N (больше 0): '))
if n > 0:
    list = list_elements(n)
    print(f'Последовательность: {list}')
    print(f'Сумма элементов последовательности: {sum(list)}')
else:
    print(f'Введено некорректное значение: {n}. Необходимо ввести целое положительное число, больше 0')
