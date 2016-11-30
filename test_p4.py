import unittest
from p4 import greeter

class TestGreeter(unittest.TestCase):

    def setUp(self):
        self.a = 5
        self.ls = [3, 3]

    def test_greet_me(self):
        self.assertEqual(greeter('Tomi'), 'Hello, Tomi!')

    def test_greet_nobody(self):
        self.assertEqual(greeter(''), 'Hello, Mr Nobody!')

    def test_greet_variable(self):
        self.assertRaises(TypeError, self.a, greeter)

    def test_greet_list(self):
        self.assertRaises(TypeError, self.ls, greeter)

if __name__ == '__main__':
    unittest.main()
