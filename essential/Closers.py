# замыкания
def add(x):
    def do_add(y):
        return x + y
    return do_add


print(add(5)(3))

# частичное применение функции:
add_to_ten = add(10)
print(add_to_ten(2))


# эмуляция ООП при помощи замыкания:
def Person(name, age):
    def print_hello_person():
        print('Hello, {} '.format(name))

    def print_age():
        return age
    return {'print_hello':print_hello_person, 'get_age': print_age}

ivan = Person('Ivan', 18)
ivan['print_hello']() #Hello, Ivan
print(ivan['get_age']())


