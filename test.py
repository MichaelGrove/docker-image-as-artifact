import unittest

def sum(a, b):
    return a + b

class TestSum(unittest.TestCase):
    def test_sum_1_2(self):
        self.assertEqual(3, sum(1, 2))
    def test_sum_2_3(self):
        self.assertEqual(5, sum(2, 3))
    def test_sum_3_4(self):
        self.assertEqual(7, sum(3, 4))
    def test_sum_4_5(self):
        self.assertEqual(9, sum(4, 5))

if __name__ == '__main__':
    unittest.main()
