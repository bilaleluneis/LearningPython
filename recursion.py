__author__ = "Bilal El Uneis and Jieshu Wang"
__since__ = "July 2018"
__email__ = "bilaleluneis@gmail.com"

from unittest import TestCase


def fibonacci(number):
    if number <= 1:
        print("Base Condition where number is < or = to 1 is met, returning {}".format(number))
        return number
    else:
        print("Recursive condition calling fibonacci({}) + fibonacci({})".format(number - 1, number - 2))
        return fibonacci(number - 1) + fibonacci(number - 2)


def fibonacci_for_test(number):
    if number <= 1:
        return number
    else:
        return fibonacci_for_test(number - 1) + fibonacci_for_test(number - 2)


class FibonacciTest(TestCase):
    fibonacci_sequence_1 = {0, 1, 1, 2, 3, 5, 8,
                            13, 21, 34, 55, 89, 144,
                            233, 377, 610, 987, 1597,
                            2584, 4181, 6765, 10946,
                            17711, 28657, 46368, 75025, 121393,
                            196418, 317811, 514229, 832040, 1346269,
                            2178309, 3524578, 5702887, 9227465,
                            14930352, 24157817, 39088169, 63245986, 102334155}

    fibonacci_sequence = [0, 1, 1, 2, 3, 5, 8]

    def setUp(self) -> None:
        self.fibonacci_sequence_instance = [0, 1, 1, 2, 3, 9, 8]
        self.length_instance = len(self.fibonacci_sequence_instance)
        print('\nStart test fibonacci function.')

    def tearDown(self) -> None:
        print('Test end!')

    for i in range(len(fibonacci_sequence)):
        def test_fibonacci(self):
            self.assertTrue(fibonacci_for_test(self.i) == self.fibonacci_sequence[self.i])

    def test_fibonacci_series(self):
        failures = []

        for i in range(len(self.fibonacci_sequence_instance)):
            fib_result = fibonacci(i)
            if fib_result != self.fibonacci_sequence_instance[i]:
                failures.append((i, fib_result, self.fibonacci_sequence_instance[i]))

        if len(failures) > 0:
            print("ERRORS:")
            for input_value, fib_result, expected_result in failures:
                print("input {} produced {} when expected was {}".format(input_value, fib_result, expected_result))

        self.failIf(len(failures) > 0)

    def test_fibonacci_3(self):
        for i in range(self.length_instance):
            with self.subTest(i):
                fib_result = fibonacci_for_test(i)
                expected_result = self.fibonacci_sequence_instance[i]
                self.assertEqual(fib_result, expected_result, "fib({}) = {} but expected {}".format(i, fib_result, expected_result))
                # self.assertTrue(fib_result == expected_result, "fib({}) = {} but expected {}".format(i, fib_result, expected_result))


# start of running code
if __name__ == "__main__":
    result = fibonacci(1)
    print("Final Result of is {}\n\n".format(result))

    result = fibonacci(4)
    print("Final Result of is {}\n\n".format(result))

    result = fibonacci(5)
    print("Final Result of is {}\n\n".format(result))

    result = fibonacci(9)
    print("Final Result of is {}".format(result))
