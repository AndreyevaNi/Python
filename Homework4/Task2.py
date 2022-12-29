# Задача 2. Задайте натуральное число N. Напишите программу, которая составит список простых множителей числа N.

def get_prime_multipliers(num):
    list_multiplier = []
    temp_num = num
    if num > 1:
        flag_repeat = True
        while flag_repeat:
            flag_repeat = False
            for i in range(2, num + 1):
                if num % i == 0:
                    list_multiplier.append(i)
                    num = int(num / i)
                    flag_repeat = True
                    break
    return list_multiplier


number = int(input('Введите положительное целое число N: '))
if number > 1:
    print(f'Простые множители числа {number} : {get_prime_multipliers(number)}')
elif number == 1:
    print(f'Простые множители числа {number} - [1]')
else:
    print(f'Введите корректно число (положительное число больше 0)')
