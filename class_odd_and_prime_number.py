__author__ = "Jieshu Wang"
__since__ = "July 2019"
__email__ = "foundwonder@gmail.com"


class InputIsFloatException(Exception):
    pass


class Integer(object):

    def __init__(self, number):
        self._validator(number)
        self.__number = number

    @property
    def value(self):
        return self.__number

    @property
    def next(self):
        return self._get_next()

    def _validator(self, number_to_validate) -> None:
        if type(number_to_validate) is int:
            return  # int so just return .. no need to check further
        elif type(number_to_validate) is float:
            raise InputIsFloatException("Input is a float, not an integer. Try again!")
        else:
            raise Exception("Error: Unknown type.")

    def _get_next(self):

        try_another = True
        next_number = self.value
        while try_another:
            try:
                next_number += 1
                self._validator(next_number)
                try_another = False
            except Exception:
                continue

        result = next_number
        return result


class InputIsEvenNumberException(Exception):
    pass


class OddNumber(Integer):

    def __init__(self, number):
        super().__init__(number)

    def _validator(self, number_to_validate) -> None:
        super()._validator(number_to_validate)
        remainder = super().value % 2
        if remainder == 1:
            return
        else:
            raise InputIsEvenNumberException("Input is an even number, not an odd number. Try again.")

    # def _get_next(self) -> int:
    #     i = self.__number + 1
    #     while i > self.__number:
    #         try:
    #             self._validator()
    #             return i
    #         except Exception:
    #             i += 1

    # TODO: pick better name
    def sequence_generator(self, start, end) -> []:
        pass


# Below is about prime number


class InputIsNotPrimeNumberException(Exception):
    pass


class PrimeNumber(object):

    def __init__(self, number):
        self.__validator(number)
        self.__number = number

    @property
    def value(self):
        return self.__number

    @property
    def next(self):
        return self.__get_next()

    def __validator(self, number_to_validate):
        if type(number_to_validate) is int:
            if number_to_validate > 1:
                for i in range(2, int(number_to_validate / 2) + 1):
                    if number_to_validate % i == 0:
                        raise InputIsNotPrimeNumberException("Input is not a prime number.")

                return number_to_validate
            else:
                raise InputIsNotPrimeNumberException("Input is not a prime number.")
        elif type(self.__number) is float:
            raise InputIsFloatException("Input is a float, not an integer. Try again.")
        else:
            raise Exception("Error: Unknown type inputted.")

    def __get_next(self):
        i = self.__number + 1
        while i > self.__number:
            try:
                PrimeNumber(i)
                return i
                break
            except Exception:
                i += 1

    def prime_number_sequence_generator(self):
        pass
