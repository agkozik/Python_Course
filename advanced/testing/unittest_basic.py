import unittest


def my_function(value):
    return value * 20


# наследование от unittest.TestCase
class MyTestCase(unittest.TestCase):

    def test_sum(self):
        self.assertEqual(2 + 2, 4)

    def test_multiply(self):
        self.assertTrue(2 * 4 == 8)

    def test_my_function(self):
        value = 100
        self.assertEqual(my_function(value), value * 20)

    def test_my_function_uncorrect(self):
        value = 100
        self.assertEqual(my_function(value), value * 10)
# запуск из консоли:
# C:\AND\Python_Course\advanced\testing>python -m unittest unittest_basic.py
# python -m unittest unittest_basic.py
