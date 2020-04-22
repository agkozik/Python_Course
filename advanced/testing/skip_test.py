import datetime
import sys
import unittest.mock


class MyTestCase(unittest.TestCase):
    # прорустить тест, который недописан
    @unittest.skip('Skipped message: Test Skip')
    def test_i_want_it_to_skip(self):
        self.fail('Will not be run')

    # пропустить тест, который не должен запускаться в данное время
    @unittest.skipIf(datetime.datetime.now().hour in [2, 14, 20], 'Skipped message: too late')
    def test_just_skip_if(self):
        self.fail('Will not be run')

    # пропустить тест, который не для данной ос
    @unittest.skipUnless(sys.platform.startswith('darwin'), 'Skipped message: MacOs required')
    def test_only_mac(self):
        self.assertEqual(1, 1)
    # ожидаемое падение
    @unittest.expectedFailure
    def test_expected_failure(self):
        self.assertEqual(1, 2)


@unittest.skip('SkipTestCase Class')
class SkipTestCase(unittest.TestCase):
    def test_test(self):
        self.fail('error')