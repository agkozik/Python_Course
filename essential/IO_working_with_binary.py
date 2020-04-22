import random
# генерация 1000 случайных целых чисел в интервале -1000000, 1000000
# сохранение их в список
# numbers = []
# for line in range(1000):
#     numbers.append(random.randint(-1000000, 1000000))
# или
# numbers = [random.randint(-1000000, 1000000) for _ in range(1000)]
#
# # запись в текстовый файл данных значений
# with open('../csv_data/text_file.txt', 'w') as csv_data:
#     for i in numbers:
#         csv_data.write('{}\n'.format(i))
#
# # запись в бинарный файл данных значений
# import array
#
# numbers_array = array.array('i', numbers)
# print(numbers)
# print(numbers_array)
# with open('../csv_data/bin_file.bin', 'wb') as binary_file:
#     binary_file.write(numbers_array)

# считывание данных из текстового файла
with open('../resources/text_file.txt') as text_file:
    numbers = [int(line) for line in text_file]
print(numbers)

# считывание бинарного файла:
import array
import os.path

file_name = '../resources/bin_file.bin'
    # определяем длину файла
file_size2 = os.path.getsize(file_name)
count = file_size2//array.array('i').itemsize # itemsize - Длина в байтах одного элемента массива во внутреннем представлении
    # создаем массив из count целочисленных переменных
numbers = array.array('i', (0 for _ in range(count)))
# numbers = [i for i in range(count)] - это список

    # считываем бинарный файл в массив:
with open(file_name, 'rb') as binary_file:
    binary_file.readinto(numbers)

print(numbers)







