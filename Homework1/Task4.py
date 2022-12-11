# Напишите программу, которая по заданному номеру четверти,
# показывает диапазон возможных координат точек в этой четверти (x и y).

quater_number = int(input('Введите целое положительное число - номер четверти: '))
if quater_number == 1:
    print(f'В четверти {quater_number}: x > 0 y > 0')
elif quater_number == 2:
    print(f'В четверти {quater_number}: x < 0 y > 0')
elif quater_number == 3:
    print(f'В четверти {quater_number}: x < 0 y < 0')
elif quater_number == 4:
    print(f'В четверти {quater_number}: x > 0 y < 0')
else:
    print(f'Указанной четверти {quater_number} не существует.')

