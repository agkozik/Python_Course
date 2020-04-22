# # открытие уже СУЩЕСТВУЮЩЕГО файла для чтения
# my_file = open('../csv_data/my_file.txt')
# # вывод содержимого файла
# print(my_file.read())
# my_file.close()

# портабельный на разные операционные системы вариант прописывания
# пути к файлам:
# import os.path
# portable_path_to_file = os.path.join('..', 'csv_data', 'my_file.txt')
# my_file = open(portable_path_to_file)
# print(my_file.read())
# my_file.close()

# Упращение работы с использованием менеджера контекста:
# автозакрытие, даже если было исключение

# прочитать весь файл file.read()
# file.read(100) - прочитать заданное количество символов
# file.readline() чтение одной строки
# file.readlines() - список строк
# for line in file: - реализует итератор
#     pass
# file.readinto(arr) - чтение в массив

with open('../resources/my_file.txt') as file:
    print(file.read())

# file.writelines(lines) запись строк (в цикле вызывает метод write)
# file.write(csv_data) запись данных (символов или данных)

    # запись данных в файл при помощи функции print(*args, file='my_file.txt')
my_second_file = '../resources/my_second_file.txt'
    # читаем файл с помощью менеджера контекста, сохраняем содержимое в строку sec_file:
with open(my_second_file) as data:
    lines = data.readlines()
    # вставляем новую строку в нужную нам позицию (строка 1)
lines.insert(4, 'Новая вставленная строка\n')
    # снова открываем файл, т.к аттрибут 'w' удаляем всё что в нем было и записываем заново из строки lines в файл:
with open(my_second_file, 'w') as data:
    data.writelines(lines)

with open(my_second_file) as data:
    print(data.read())

# Объяснение как происходит использование менеджера контекста для автозакрытия, разблокирования ресурсов
# class My_manager(object):
#     def __init__(self):
#         self.resource = 11
#
#     def __enter__(self):
#         print('Enter def')
#         return self.resource
#
#     def __exit__(self, exc_type, exc_val, exc_tb):
#         print('Exit def')
#         if exc_type:
#             print('(Exception type: {})'.format(exc_type))
#
# # теперь используем My_manager как ресурс:
# with My_manager() as resource:
#     print('Do smth with resource:', resource)
#     #Enter def
#     #Do smth with resource: 11
#     #Exit def
# # теперь используем My_manager как ресурс с вызовом исключения:
# with My_manager() as resource:
#     print('Do smth with resource:', resource)
#     raise ValueError
#     #Enter def
#     #Do smth with resource: 11
#     #Exit def
#     #(Exception type: <class 'ValueError'>)


# получается будет выполнен код, а потом выдаст исключение (сахар, как finally)
# процесс выполнения такой:
#
# def my_with(manager, context_body):
#     resource = manager.__enter__()
#     exc_type, exc_value, exc_traceback = None , None, None
#     error = None
#     try:
#         context_body(resource)
#     except Exception as e:
#         exc_type, exc_value, exc_traceback = sys.exc_info()
#         error = e
#     finally:
#         manager.__exit__(exc_type, exc_value, exc_traceback)
#         if error:
#             raise error
#
# def context_body(resource)
#     print('Some action with resource: ', resource)
#     raise ValueError
#
# my_with(My_manager(), context_body)
