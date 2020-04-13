def divide(x, y):
    z = 0
    try:
        z = x / y

    except (ZeroDivisionError, TypeError, ValueError) as my_error:
        print("ERROR: Block Exception ", my_error)


    except Exception as my_name_error:
        print(type(my_name_error))

    else:
        print("Block Else: x = ", x, "y = ", y)

    finally:
        print("Block Finally: x = ", x, "y = ", y)
        print("---------------------------")


if __name__ == '__main__':
    divide(1, 0)
    divide(1, 2)
    divide('f', 2)
    divide(2.0, 2)