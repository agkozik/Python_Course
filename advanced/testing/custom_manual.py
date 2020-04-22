def concat(x, y):
    return '{} {}'.format(x, y)


def sum_3_elem(a, b, c):
    return a + b + c


def multiply_3_elem(a, b, c):
    return a * b * c


def test_concat():
    assert concat(1, 2) == '1 2'
    assert concat(10, 20) == '10 20 '


def test_sum_3_elem():
    assert sum_3_elem(0, 1, 2) == 3
    assert sum_3_elem(0, 2, 3) == -5
    assert sum_3_elem(-1, 1, -5) == -5


def test_multiply_3_elem():
    assert multiply_3_elem(1, 2, 3) == 6
    assert multiply_3_elem(-10, 2, 3) == 60


test_function = [
    test_concat,
    test_sum_3_elem,
    test_multiply_3_elem
]
if __name__ == '__main__':
    for func in test_function:
        try:
            func()
        except Exception as e:
            print('Failed: {} => {}: {}'.format(func, type(e), e))
