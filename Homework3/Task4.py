# Задача 4. Напишите программу, которая будет преобразовывать десятичное число в двоичное.
# Пример:
# - 45 -> 101101
# - 3 -> 11
# - 2 -> 10

def converting_decimal_to_binary(dec_number):
    bin_number = ''
    while dec_number > 0:
        bin_number = str(dec_number % 2) + bin_number
        dec_number = dec_number // 2
    return bin_number


n = int(input('Введите целое положительное число, больше 0: '))
if n > 0:
    print(f'Результат преобразования десятичного числа в двоичное: {n} -> {converting_decimal_to_binary(n)}')
else:
    print(f'Введено некорректное значение: {n}. Необходимо ввести целое положительное число, больше 0')
