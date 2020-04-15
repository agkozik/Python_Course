def print_matrix(matrix):
    for row in matrix:
        # '_'.join(['a','b','c']) //a_b_c
        print(' '.join(str(i) for i in row))


matrix = [[1] * 5]
print_matrix(matrix)
print('--------------')

# пять ссылок на один и тот же список в памяти
matrix = matrix * 5
print_matrix(matrix)

print('------ пять ссылок на один и тот же список в памяти, поэтому просто дубли--------')
matrix[1][3] = 777
print_matrix(matrix)
print(id(matrix[0]))
print(id(matrix[1]))
print('------ пять разных строк - объектов--------')

matrix = [[1] * 5]
matrix = [[1] * 5 for _ in range(5)]
print_matrix(matrix)
matrix[1][3] = 777
print(id(matrix[0]))
print(id(matrix[1]))
print_matrix(matrix)