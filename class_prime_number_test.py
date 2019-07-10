__author__ = "Jieshu Wang"
__since__ = "July 2019"
__email__ = "foundwonder@gmail.com"

from class_odd_and_prime_number import *
from unittest import TestCase


class IntegerTest(TestCase):

    def setUp(self) -> None:
        print("\nInteger unittest starts!")

    def tearDown(self) -> None:
        print("Integer unittest end!")

    def test_integer(self):
        test_integer = Integer(3)
        self.assertEqual(test_integer.value, 3)

    def test_float(self):
        self.assertRaises(InputIsFloatException, Integer, 1.5)

    def test_get_next(self):
        test_next = Integer(5)
        self.assertEqual(test_next.next, 6)


class OddNumberTest(TestCase):

    def setUp(self) -> None:
        print("\nOdd number unittest starts!")

    def tearDown(self) -> None:
        print("Odd number unittest end!")

    def test_input_odd_number(self):
        test_odd_number = OddNumber(5)
        self.assertEqual(test_odd_number.value, 5)

    def test_input_even_number(self):
        self.assertRaises(InputIsEvenNumberException, OddNumber, 6)

    def test_input_float(self):
        self.assertRaises(InputIsFloatException, OddNumber, 1.5)

    def test_input_other_type(self):
        other_type_testing_set = ["hello", True, 2 < 1, [1, 2]]
        for i in other_type_testing_set:
            with self.subTest(i):
                self.assertRaises(Exception, OddNumber, i)

    def test_get_next(self):
        test_next_value = OddNumber(7)
        self.assertEqual(test_next_value.next, 9)


class PrimeNumberTest(TestCase):

    __test_prime_number_set = None

    @classmethod
    def setUpClass(cls) -> None:
        cls.__test_prime_number_set = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]
        cls.__test_none_prime_number_set = [6, 4, 8, 9, 25, 88]

    def setUp(self) -> None:
        print("\nPrime number unittest starts!")

    def tearDown(self) -> None:
        print("Prime number unittest end!")

    def test_input_prime_number(self):
        test_prime_number = PrimeNumber(28657)
        self.assertEqual(test_prime_number.value, 28657)

    def test_input_prime_number_sequence(self):
        for i in PrimeNumberTest.__test_prime_number_set:
            with self.subTest(i):
                self.assertEqual(PrimeNumber(i).value, i)

    def test_input_not_prime_number(self):
        self.assertRaises(InputIsNotPrimeNumberException, PrimeNumber, 6)

    def test_input_random_number_sequence(self):
        for i in PrimeNumberTest.__test_none_prime_number_set:
            with self.subTest(i):
                self.assertRaises(InputIsNotPrimeNumberException, PrimeNumber, i)

    def test_get_next(self):
        test_next_value = PrimeNumber(7)
        self.assertEqual(test_next_value.next, 11)
