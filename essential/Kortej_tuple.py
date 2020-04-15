#  Кортежи относятся к Неизменяемым типам данных.
#  Можно получить элемент по индексу, но изменить его нельзя:

my_tuple1 = tuple()
my_tuple1 = ()
my_tuple2 = (1,)
my_tuple3 = 1,
my_tuple4 = (1, 2, 'a string')
my_tuple5 = 1, 2, 'a string'
my_tuple6 = tuple(range(8))
print(my_tuple1)
print(my_tuple2)
print(my_tuple3)
print(my_tuple4)
print(my_tuple5)
print(my_tuple6)

# zip - объединение списков:
cities = ('NY', 'LA', 'Minsk')
population = (213, 431, 45)
my_list = list(zip(cities, population))
print(my_list)

# enumerate() создание нумерованных списков, с указанием начальной нумерации:
new_list = list((enumerate(cities, 7)))
print(new_list)  # [(7, 'NY'), (8, 'LA'), (9, 'Minsk')]

for city_index, city in enumerate(cities):
    print('Index=', city_index, ' is ', city)
# Index= 0  is  NY
# Index= 1  is  LA
# Index= 2  is  Minsk

# -----------------------enumerate Index = {}, Value = {}------------------------------
values = [5, 4, 3, 2]
for index, value in enumerate(values):
    print('Index = {}, Value = {}'.format(index, value))

# -----------------------------------------------------
a, b, c = 1, 2, 3
print(a)
a, b, c = 'qwe'
print(a)

# -----------------------------------------------------
head, *tail = range(5)
print(head)  # 0
print(tail)  # [1, 2, 3, 4]

*head, tail = range(5)
print(head)  # [0, 1, 2, 3]
print(tail)  # 4

first, second, *middle, last = range(10)
print(first)  # 0
print(second)  # 1
print(middle)  # [2, 3, 4, 5, 6, 7, 8]
print(last)  # 9

# -----------------------------------------------------
x = 2
y = 5
x, y = y, x
print('x=', x, 'y=', y)  # x= 5 y= 2


# --------------------реализация передачи множества параметров в функцию---------------------------------
def function(*args):
    # print(type(args)) #<class 'tuple'>
    print(args)


function(1, 2, 3)


# --------------------реализация передачи множества параметров в функцию, с обязательным одним параметром
def average(first, *numbers):
    sum_ = first + sum(numbers)  # 1 + 9 = 10
    return sum_ / (len(numbers) + 1)  # 10/4 = 2.5


print(average(1, 2, 3, 4))
