# Отображения объект предоставляющий доступ к ключам - значениям. Это словарь - dictionary
my_dict = {'name': ' John', 'age': 21, 'city': 'NY'}
print(my_dict)
my_dict = dict(one=1, two=2)
print(my_dict)


def named_args_function(**key_value):
    print(key_value)


named_args_function(a=1, b=2)


def position_and_named_args_function(*args, **key_valueargs):
    print(args)
    print(key_valueargs)


position_and_named_args_function(2, 3, 4, a=1, b=7)

# -------------------------------------------------------------------------------------------------------------------
print(1, 2, sep='_____', end='\n**********************\n')
options = {'sep': '_____',
           'end': '\n**********************\n'}
print(1, 2, **options)
