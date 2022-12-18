# Задача 5.  Задайте число. Составьте список чисел Фибоначчи , в том числе для отрицательных индексов [Негафибоначчи].
# Пример:
# - для k = 8 список будет выглядеть так: [-21 ,13, -8, 5, −3, 2, −1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21]

def get_list_negafibonacci_fibonacci(number):
    negafibonacci_num = [1, -1]
    fibonacci_num = [1, 1]
    for i in range(2, number):
        list_fibonacci = fibonacci_num[i - 1] + fibonacci_num[i - 2]
        fibonacci_num.append(list_fibonacci)
        list_negafibonacci = negafibonacci_num[i - 2] - negafibonacci_num[i - 1]
        negafibonacci_num.append(list_negafibonacci)
    negafibonacci_num.reverse()
    fibonacci_num.insert(0, 0)
    negafibonacci_num.extend(fibonacci_num)
    return negafibonacci_num


n = int(input('Введите целое положительное число , больше 1: '))
if n > 1:
    print(
        f'Список чисел Фибоначчи, в том числе для отрицательных индексов: {n} -> {get_list_negafibonacci_fibonacci(n)}')
else:
    print(f'Введено некорректное значение: {n}. Необходимо ввести целое положительное число, больше 1')
