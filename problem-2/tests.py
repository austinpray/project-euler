import unittest
import EvenFibonacciNumbers


class TestEvenFib(unittest.TestCase):
    def test_base(self):
        # 1 1 2 3 5 8 13 21 34 55 89 144 233 377 610 987
        self.assertEqual(EvenFibonacciNumbers.sum_even_fib(55), 2+8+34)


if __name__ == '__main__':
    unittest.main()
