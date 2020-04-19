# Встроенная функция mар ()  позволяет применить заданную в параметре функцию к каждому элементу последовательности.
# посчитать квдраты чисел из списка и вывести
from functools import reduce

values = [2, 1, 5, 8, 3, 2]
for square in map(lambda x: x ** 2, values):
    print(square, end=' ')

print()
# Функция  mар возвращает  объект,  поддерживающий  итерации.  Чтобы  превратить  его
# в список, возвращенный результат следует передать в функцию list().

# посчитать квдраты чисел из списка и сохранить в новый список
square = list(map(lambda x: x ** 2, values))
print(square)

# Функция  filter о позволяет выполнить  проверку элементов  последовательности
# Если  элемент в логическом контексте возвращает значение  False, то он не будет добавлен в возвращаемый результат

# сохранить из списка только значения больше нуля
values = [2, 0, -1, 1, 5, -8, 3, 2]
positive_figures = list(filter(lambda x: x > 0, values))
print(positive_figures)

# Функция reduced из модуля  functools применяет указанную функцию к парам элементов и накапливает результат
# в качестве параметров передаются два элемента: первый  элемент будет содержать результат  предыдущих  вычислений,
# а второй— значение  текущего  элемента.

# посчитаем произведение всех чисел из списка
values = [1, 2, 3, 4, 5]
multiply = reduce(lambda x, y: x * y, values)
print(multiply)

# сохранение результатов вычисления функций, которые не были изменены
# позволяет значительно ускорить вычисления с использованием рекурсии
from functools import lru_cache


@lru_cache(maxsize=None)
def fibonacci(n):
    if n == 1 or n == 2:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)


print(fibonacci(35))

# partial частично еприменение функции, использование не всех аргументов
from functools import partial


def add(x, y):
    return x + y


add_to_five = partial(add, 5)
print(add_to_five(3))

# реализовать собственный print в котором будет применяться необходимый параметр
print_use_comma_separator = partial(print, sep=', ')
print(1, 2, 3)
print_use_comma_separator(1, 2, 3)
