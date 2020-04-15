# -------------------множества не содержат повторяющихся значений, не содержат индексов
# -------------------и при выводе не гарантируют порядок вывода элементов
# empty_set = set()
# print(empty_set)
#
# empty_set = frozenset()
# print(empty_set)
#
# my_set = {1, 3, 2, 5}
# my_frozen_set = frozenset([1, 2, 5, 7])
#
# my_set = {x** 3 for x in range(5)}
# print(my_set)
first_set = {5, 2, 1, 8, 3, 10}
second_set = {1, 2, 3, 4, 5, 6, 10}
print(first_set)
print(second_set)
# -----------------------------------  & Пересечение: элементы, которые являются общими ------------------------------
print(first_set & second_set, 'Пересечение: элементы, которые являются общими для first_set и second_set')
# Проверка на наличие общих значений
print(first_set.isdisjoint(second_set))

# -----------------------------------  Объединение: все элементы, которые есть и в 1м и во 2м ------------------------
print(first_set | second_set, '1й способ Объединение: все элементы, которые есть и в 1м и во 2м')
print(first_set.union(second_set), '2й способ Объединение: все элементы, которые есть и в 1м и во 2м')
print(first_set.union([1, 2, 3, 4, 5, 6, 10]))

# -----------------------------------  Разница множеств:  оставить значения которые есть в 1м и нет во втором --------
print(first_set, '-', second_set, ' = ', first_set - second_set)
print(second_set, '-', first_set, '=', second_set - first_set)
print(first_set.difference(second_set))

# -----------------------------------  Симметрическая разница:  уникальные из 1го и из 2го----------------------------
print(first_set ^ second_set)
print(second_set ^ first_set)

# -----------------------------------  Сравнение > < <= >= -----------------------------------------------------------
print({1, 2, 3} < {1, 2, 3})

print({1, 2} <= {1, 2, 3})
print({1, 2}.issubset({1, 2, 3}))

print({1, 2, 3} >= {1, 2})
print({1, 2, 3}.issuperset({1, 2}))

# -----------------------------------  Работа с Set ------------------------------------------------------------------
print(first_set)
first_set.add(5)  # такой элемент уже есть, он не добавится
print(first_set)

first_set.add(15)
print(first_set)

first_set.remove(5)  # при удалении несуществующего значения - выкидывает исключение
print(first_set)

first_set.discard(15)
print(first_set)

first_set.discard(15)  # при удалении несуществующего значения - ничего не делает
print(first_set)

temp = first_set.copy()
print(temp)
print(type(first_set))
print(type(temp))
print(id(first_set))
print(id(temp))

print(temp.pop())  # возвращает произвольный элемент из коллекции и Удаляет его
print(temp)

temp.clear()
print(temp)

temp.update(second_set)  # добавляет указанные элементы
print('Temp ', temp)
print('First set ', first_set)

temp.difference_update(first_set)
print('Temp ', temp)

temp.update(range(0, 4))
print(temp)

# ------------------------------------------- {} == {} ----------------------------------------------------------------
print({1, 2, 3} == {3, 2, 1})
print({1, 2, 3} == {1, 2, 5})

# но типы не проверяются:
print({1, 2, 3} == frozenset([1, 2, 3]))
print({1, 2} in {frozenset([9]), frozenset([7, 8]), frozenset([1, 2])})  # {1, 2} == frozenset([1, 2])

# ---------------------------------------------------------------------------------------------------------------------
str1 = input('Введите первую строку: ')
str2 = input('Введите вторую строку: ')
common = set(str1) & set(str2)
print('Общие символы: ', common, 'Количество общих символов: ', len(common))
for i in common:
    print(i)
print()

print('\n'.join(common))
print()

set1 = set(str1)
set2 = set(str2)
print('\n'.join(set1.intersection(set2)))
print()