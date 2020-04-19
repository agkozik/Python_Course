# itertools модуль содержащий фунции для работы с итератором
print('--------------- обычный цикл for, вложенный в другой цикл for ------')

for i in range(1, 3):
    for j in range(1, 3):
        print('{} x {} = {}'.format(i, j, i * j))

print('--------------- product - замена вложенного for---------------------')

from itertools import product

for i, j in product(range(1, 3), range(1, 3)):
    print('{} x {} = {}'.format(i, j, i * j))

print('--------------- chain - соединяет последовательно итераторы ---------------------')
from itertools import chain

for i in chain(range(1, 3), range(1, 4)):
    print(i)

print('--------------- комбинаторика - перебор различных комбинаций ---------------------')
from itertools import permutations, combinations, combinations_with_replacement

my_sequence_of_elements_as_string = 'ABC'
count_in_sequence = 2

print(list(permutations(my_sequence_of_elements_as_string, count_in_sequence)))
print(list(combinations(my_sequence_of_elements_as_string, count_in_sequence)))
print(list(combinations_with_replacement(my_sequence_of_elements_as_string, count_in_sequence)))

print('--------------- работа с последовательностью с проверкой условий:'
      ' takewhile (до того момента пока нет False) - drop while (начало после False) ---------------------')
from itertools import takewhile, dropwhile

values = [1, 4, 3, 5, 3, 2, 8]
predicate = lambda x: x < 5
print(values)
print('Takewhile:', end=" ")
for elem in takewhile(predicate, values):
    print(elem, end=" ")
print('Dropwhile:', end=" ")
for elem in dropwhile(predicate, values):
    print(elem, end=' ')
