import copy
class Item:
    def __init__(self):
        self.list = [1, 2, 3]
        self.number = 1


print('--------------copy-----------------------')
item1 = Item()
print('item1: ', item1.list, item1.number)
item2 = copy.copy(item1)
print('item2: ', item2.list, item2.number)

item2.list.append(4)
print('item1: ', item1.list, item1.number)
print('item2: ', item2.list, item2.number)

print('--------------deepcopy-----------------------')
item1 =Item()
item1 = Item()
print('item1: ', item1.list, item1.number)
item2 = copy.deepcopy(item1)
print('item2: ', item2.list, item2.number)

item2.list.append(4)
print('item1: ', item1.list, item1.number)
print('item2: ', item2.list, item2.number)

print('--------------random-------------------------')
import random
print(random.randint(1, 10))
print(random.choice(['first', 'second', 'third']))
print(random.sample(range(100), 2)) # выбрать 2 числа из 100: [44, 66]
obj = random.Random()
print(obj.randint(1, 100))
sys_random = random.SystemRandom()
print(sys_random.random())

print('--------------Вещественные числа-------------------------')
print(0.1+0.2)
from decimal import Decimal
print(Decimal('0.1')+Decimal('0.2'))

from fractions import Fraction
print(Fraction(1, 3))# 1/3
print(Fraction(1, 2) + Fraction(1, 2) )# 1/2 +1/2 = 2/2 = 1/1 = 1

print('--------------Date -Time-------------------------')
import datetime
now = datetime.datetime.now()
print(now)
print(datetime.datetime.now() - now)
some_day = datetime.datetime(year=2020, month=4, day=15, hour=23, minute=12, second=0)
print(some_day)
print(some_day + datetime.timedelta(days=2, hours=3))
print(some_day.strftime('%A,%d.%m.%y'))