print(2, 3, 5)

# установить разделитель
print(2, 3, 5, sep='-')

# склеит строки
print('Hel', 'lo', sep='')

# чем заканчивать строку
print(1, end='_')
print(2, end='\n\n')
print('he', end='')
print('llo')

# Ввод параметрами
string = input('Enter a String... ')
print('You\'ve entered: "{}" '.format(string))
print('You\'ve entered: "', string, '"', sep='')

x = int(input('Enter x: '))
y = int(input('Enter y: '))
print('{}+{}={}'.format(x, y, x + y))

print('Press \"Enter\" key to exit...')
input()

