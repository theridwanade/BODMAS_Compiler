import unittest
def add(a, b):
    return a + b

class TestMathOps(unittest.TestCase):
    def test_add(self):
        self.assertEqual(add(2, 3), 5)

    def test_add2(self):
        self.assertEqual(add(2, 4), 5)


if __name__ == '__main__':
    unittest.main()
