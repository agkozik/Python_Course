import unittest
import datetime

class MyTestCase(unittest.TestCase):

    def setUp(self):
        print('setUp --вызывается перед каждым методом')
        self.current = datetime.datetime.now()

    @classmethod
    def setUpClass(cls):
        print('setUpClass -вызывается 1 раз')
        cls.current_cls = datetime.datetime.now()

    def tearDown(self):
        print('tearDown -вызывается после каждого метода')

    @classmethod
    def tearDownClass(cls) -> None:
        print('teardownClass -вызывается 1 раз')

    def test_example1(self):
        print('test_example1:', self.current)
        print('test_example1:', self.current_cls)

    def test_example2(self):
        print('test_example2:', self.current)
        print('test_example2:', self.current_cls)
