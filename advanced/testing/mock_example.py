import time
import unittest.mock
from unittest.mock import patch


def sum_two_numbers(a, b):
    time.sleep(2)
    return a + b


class MyTestCase(unittest.TestCase):
    # тест с заглушкой
    @patch('mock_example.sum_two_numbers', return_value=5)
    def test_with_mock_sum_two_numbers(self, mocked):
        expected = 5
        self.assertEqual(mocked(2, 3), expected)

    # тест без заглушки
    def test_without_mock(self):
        self.assertEqual(5, sum_two_numbers(2, 3))

    @patch('mock_example.sum_two_numbers')
    def test_sum_two_numbers_called_with(self, mocked_sum):
        sum_two_numbers(10, 20)  # вызов заглушки
        self.assertTrue(mocked_sum.called)  # проверка был ли вызов функции
        self.assertEqual(mocked_sum.call_count, 1)  # проверка количества вызовов функции
        mocked_sum.assert_called_with(10, 20)
        # обнулить вызовы функции
        mocked_sum.reset_mock()

        mocked_sum.assert_not_called()

    @patch('mock_example.sum_two_numbers')
    def test_mock_call(self, mocked_sum):
        sum_two_numbers(1, 2)
        sum_two_numbers(3, 4)
        sum_two_numbers(5, 6)
        # проверка был ли вызов любой из функций
        mocked_sum.assert_any_call(3, 4)

