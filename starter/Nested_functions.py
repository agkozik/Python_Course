# def outer_function():
#     def inner_function():
#         print("Inner function")
#     print("Outer function")
#     inner_function()
#
#
# outer_function()

# def print_var():
#     global var
#     var = "new global variable"
#     print(var)
#
#
# var = "global variable"
#
# print_var()

# variables flow


def outer_function ():
    x = 8

    def inner_function():
        # nonlocal x
        global x
        print(x)
        x = 10
    print(x)
    inner_function()
    print(x)


x = 0
print(x)
outer_function()
print(x)
#nonlocal: 0 8 8 10 0
#  global: 0 8 0 8 10