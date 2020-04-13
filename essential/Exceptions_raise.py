# def main():
#     try:
        # бросаем новое исключение:
#         raise ValueError('value is incorrect')
#     except ValueError as error:
#         print('First block Exception:', error)
        # бросаем новое исключение:
#         raise
#
# try:
#     main()
# except ValueError:
#     print('Second try Block')

# - ---------------------------------------------------
a = 3
b = 0

try:
    result = a / b
except ZeroDivisionError as error:
    # бросаем новое исключение:
    raise ValueError('my message: ') from error
