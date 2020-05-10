import unittest
import add


class TestAddModule(unittest.TestCase):
    def test_add_func(self):
        self.assertEqual(add.add_two_values(5, 5), 10)
        self.assertEqual(add.add_two_values(10, 10), 20)
        self.assertEqual(add.add_two_values(15, 15), 30)
        self.assertEqual(add.add_two_values(25, 15), 40)

    def test_add_func_fail(self):
        # self.assertEqual(add.add_two_values(5, 5), 15)
        self.assertEqual(add.add_two_values(5, 5), 10)
