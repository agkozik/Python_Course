# def print_loop(numbers):
#     for i in range(numbers):
#         print(i)
#     print()
#
# n = int(input("Enter a number to start n-iterations: "))
# print_loop(n)


# def hello():
#     print("Hello, World!")
#
#
# def main():
#     hello()
#
#
# if __name__ == "__main__":
#     main()
#
#
# def add_numbers(first, second):
#     return first + second
#
#
# result = add_numbers(2, add_numbers(5, 7))
# print(result)
#
#
# x = add_numbers(1, 2)
# print(x)


# def function1(x):
#     if x < 0:
#         return x * 2
#     else:
#         return x * 3
#
#
# def main():
#     for i in range(-5, 5):
#         y = function1(i)
#         print("Value x = ", i, " Value y = ", y, sep='')
#
#
# main()


def print_info(name='Unknown', color='White', price=0):
    print("Name = ", name, sep="\t")
    print("Color =", color, sep="\t")
    print("Price =", price, sep="\t")


def main():
    print_info(price=5, name="Donald", color="red")
    print_info("Snow")


main()