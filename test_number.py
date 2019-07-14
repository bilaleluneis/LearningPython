from unittest import TestCase
from class_odd_and_prime_number import Number


class TestNumber(TestCase):

    def test_number_init(self):
        valid_number = Number(5)
        self.assertEqual(valid_number.value, 5)
