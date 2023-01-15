# Задача 4. Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.
# Входные и выходные данные хранятся в отдельных текстовых файлах.

def write_file(file_name, str_):
    with open(file_name, 'w') as data:
        data.write(str_)


def compression_text(file_name):
    with open(file_name, 'r') as data:
        txt = data.read()
    count = 1
    result = ''
    for i in range(len(txt) - 1):
        if txt[i] == txt[i + 1]:
            count += 1
        else:
            result = result + str(count) + txt[i]
            count = 1
    if count > 1 or (txt[len(txt) - 2] != txt[-1]):
        result = result + str(count) + txt[-1]

    write_file("Task4_ForCompression.txt", result)
    return result


def decompression_text(file_name):
    with open(file_name, 'r') as data:
        txt = data.read()
    result = ""
    i = 0
    j = 0
    while (i <= len(txt) - 1):
        num = int(txt[i])
        char = txt[i + 1]
        for j in range(num):
            result = result + char
            j = j + 1
        i = i + 2
    return result


text = input("Введите текст для выполнения сжатия: ")
write_file("Task4_ForDeCompression.txt", text)
print(f"Текст после сжатия: {compression_text('Task4_ForDecompression.txt')}")
print(f"Текст после восстановления: {decompression_text('Task4_ForCompression.txt')}")
