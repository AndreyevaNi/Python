# Задача № 3. Напишите программу, которая принимает на вход координаты точки (X и Y),
# причём X ≠ 0 и Y ≠ 0 и выдаёт номер четверти плоскости, в которой находится эта точка (или на какой оси она находится).
# Пример:
# - x=34; y=-30 -> 4
# - x=2; y=4-> 1
# - x=-34; y=-30 -> 3

x = int(input('Введите целое число, X= '))
y = int(input('Введите целое число, Y= '))
if x == 0 and y == 0:
    print(f'Введены некорректные значения. Нарушено условие X ≠ 0 и Y ≠ 0.')
elif x == 0:
    print(f'При X = {x}. Точка находится на оси абсцисс')
elif y == 0:
    print(f'При Y = {y}. Точка находится на оси ординат')
elif x > 0 and y > 0:
    print(f'При  X = {x} и Y = {y} точка находится в плоскости четверти 1')
elif x < 0 and y > 0:
    print(f'При X= {x} и Y = {y} точка находится в плоскости четверти 2')
elif x < 0 and y < 0:
    print(f'При  X = {x} и Y = {y} точка находится в плоскости четверти 3')
elif x > 0 and y < 0:
    print(f'При  X= {x} и Y = {y} точка находится в плоскости четверти 4')