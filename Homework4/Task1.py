# Задача 1. Вычислить число c заданной точностью d
# Пример:
# - при $d = 0.001, π = 3.141.$    $10^{-1} ≤ d ≤10^{-10}$
import math

from decimal import Decimal


def decimal_num(number, precision):
    number_dec = number.quantize(Decimal(precision))
    return number_dec


number = Decimal(input("Введите число: "))
d = Decimal(input('Задайте точность в формате 0.001: '))
print(f'Результат: {decimal_num(number, d)}')
