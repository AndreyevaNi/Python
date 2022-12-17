# Задача 1. Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.
# Пример:
# - 6782 -> 23
# - 0,56 -> 11

def sum_numbers(number):
    sum = 0
    for i in number:
        if i != '.':
            sum = sum + int(i)
    return sum


number = float(input('Введите вещественное число с разделителем ".": '))
print(sum_numbers(str(number)))
