import unittest


def sum_two_values(a, b):
    return a + b


def power(x, n):
    return x ** n


def concat_values(*args):
    result = ''
    for item in args:
        result += str(item)
    return result


def desc(x, y):
    if x == 0:
        raise ValueError('x should be equal 0')
    return y / x


class MyTestCase(unittest.TestCase):
    def test_sum_two_values(self):
        value1 = 10
        value2 = 20
        expected_result = value1 + value2
        result = sum_two_values(value1, value2)
        self.assertEqual(expected_result, result)

    def test_power(self):
        number = 2
        pow_number = 32
        result = power(number, pow_number)
        self.assertEqual(result, number ** pow_number)

    def test_concat_values(self):
        values = [1, 2, 3, 4, 5]
        result = concat_values(*values)
        self.assertEqual(result, '12345')

    def test_desk(self):
        x = 1
        y = 5
        result = desc(x, y)
        self.assertEqual(result, y / x)

    # проверка на вызов исключения
    def test_desc_with_zero(self):
        with self.assertRaises(ValueError):
            desc(0, 20)
