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
        self.assertEqual(test_next.value, 5)

    # def test_get_next_order(self):
    #     test_get_next_order = Integer(5)
    #     test_dic = {1: 6, 2: 7, 3: 8, 4: 9}
    #     for i, j in test_dic:
    #         with self.subTest(i):
    #             self.assertEqual(test_get_next_order.next_order(i), j)

    def test_get_next_order(self):
        test_get_next_order = Integer(5)
        self.assertEqual(test_get_next_order.next_order(3), 8)
        self.assertEqual(test_get_next_order.value, 5)

    def test_add_two_integer(self):
        first_integer_instance = Integer(5)
        second_integer = 7
        addition = first_integer_instance + second_integer
        self.assertEqual(addition.value, 12)

    def test_iadd(self):
        iadd_instance = Integer(10)
        iadd_instance += 3
        self.assertEqual(iadd_instance, 13)


class OddNumberTest(TestCase):

    def setUp(self) -> None:
        print("\nOdd number unittest starts!")

    def tearDown(self) -> None:
        print("Odd number unittest end!")

    def test_input_odd_number(self):
        test_odd_number = OddNumber(5)
        self.assertEqual(test_odd_number.value, 5)

    def test_input_even_number(self):
        self.assertRaises(InputIsNotOddNumberException, OddNumber, 6)

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
        self.assertEqual(test_next_value.value, 7)

    def test_get_next_order(self):
        test_get_next_order = OddNumber(11)
        self.assertEqual(test_get_next_order.next_order(2), 15)

    def test_iadd(self):
        iadd_test_instance = OddNumber(15)
        second_number = 3
        iadd_test_instance += second_number
        self.assertEqual(iadd_test_instance, 21)


class EvenNumberTest(TestCase):

    def setUp(self) -> None:
        print("\nEven number unittest starts!")

    def tearDown(self) -> None:
        print("Even number unittest end!")

    def test_input_even_number(self):
        test_even_number = EvenNumber(4)
        self.assertEqual(test_even_number.value, 4)

    def test_input_odd_number(self):
        self.assertRaises(InputIsNotEvenNumberException, EvenNumber, 7)

    def test_input_float(self):
        self.assertRaises(InputIsFloatException, EvenNumber, 1.5)

    def test_input_other_type(self):
        other_type_testing_set = ["hello", True, 2 < 1, [1, 2]]
        for i in other_type_testing_set:
            with self.subTest(i):
                self.assertRaises(Exception, EvenNumber, i)

    def test_get_next(self):
        test_next_value = EvenNumber(8)
        self.assertEqual(test_next_value.next, 10)
        self.assertEqual(test_next_value.value, 8)

    def test_get_next_order(self):
        test_get_next_order = EvenNumber(10)
        self.assertEqual(test_get_next_order.next_order(2), 14)

    def test_iadd(self):
        iadd_test_instance = EvenNumber(20)
        second_number = 3
        iadd_test_instance += second_number
        self.assertEqual(iadd_test_instance, 26)


class PrimeNumberTest(TestCase):

    __test_prime_number_set = None

    @classmethod
    def setUpClass(cls) -> None:
        cls.__test_prime_number_set = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]
        cls.__test_none_prime_number_set = [1, 6, 4, 8, 9, 25, 88]

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

    def test_input_not_prime_number_sequence(self):
        for i in PrimeNumberTest.__test_none_prime_number_set:
            with self.subTest(i):
                self.assertRaises(InputIsNotPrimeNumberException, PrimeNumber, i)

    def test_get_next(self):
        test_next_value = PrimeNumber(7)
        self.assertEqual(test_next_value.next, 11)
        self.assertEqual(test_next_value.value, 7)

    def test_get_next_order(self):
        test_get_next_order = PrimeNumber(2)
        self.assertEqual(test_get_next_order.next_order(2), 5)

    def test_iadd(self):
        iadd_test_instance = PrimeNumber(17)
        second_number = 3
        iadd_test_instance += second_number
        self.assertEqual(iadd_test_instance, 29)


class OddPrimeNumberTest (TestCase):

    def setUp(self) -> None:
        print("\nOdd prime number unittest starts!")

    def tearDown(self) -> None:
        print("Odd prime number unittest ends!")

    def test_input_odd_prime_number(self):
        test_instance = OddPrimeNumber(3)
        self.assertEqual(test_instance.value, 3)

    # when passing 4, which is neither an odd nor a prime number,
    # it raises InputIsNotPrimeNumberException,
    # even though OddPrimeNumber inherits from OddNumber first,
    # because of the MRO, OddNumber init is called first, then
    # before OddNumber._validator been called, PrimeNumber init is called,
    # then Integer init, PrimeNumber._validator (where InputIsNotPrimeNumberException is raised).
    def test_input_even_number(self):
        self.assertRaises(InputIsNotPrimeNumberException, OddPrimeNumber, 4)

    # when passing 2, PrimeNumber._validator is passed, so it raises InputIsNotOddNumberException
    def test_input_2(self):
        self.assertRaises(InputIsNotOddNumberException, OddPrimeNumber, 2)