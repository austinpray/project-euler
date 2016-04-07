import unittest
import LargestPrimeFactor


class TestEvenFib(unittest.TestCase):
    def test_get_prime_factors(self):
        # The prime factors of 13195 are 5, 7, 13 and 29.
        self.assertCountEqual(LargestPrimeFactor.get_prime_factors(13195), [5, 7, 13, 29])

    def test_get_largest_prime_factors(self):
        self.assertEqual(LargestPrimeFactor.get_largest_prime_factors(13195), 29)

if __name__ == '__main__':
    unittest.main()
