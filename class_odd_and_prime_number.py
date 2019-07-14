__author__ = "Bilal El Uneis & Jieshu Wang"
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

    # @property
    def next_order(self, next_order):
        return self._get_next_order(next_order)

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

    def _get_next_order(self, order):
        i = 1
        next_number = self.value
        while i <= order:
            try_another = True
            while try_another:
                try:
                    next_number += 1
                    self._validator(next_number)
                    try_another = False
                except Exception:
                    continue
            i += 1
            result = next_number
        return result


class InputIsNotOddNumberException(Exception):
    pass


class OddNumber(Integer):

    def __init__(self, number):
        super().__init__(number)

    def _validator(self, number_to_validate) -> None:
        super()._validator(number_to_validate)
        remainder = number_to_validate % 2
        if remainder == 1:
            return
        else:
            raise InputIsNotOddNumberException("Input is an even number, not an odd number. Try again.")

    # TODO: pick better name
    def sequence_generator(self, start, end) -> []:
        pass


class InputIsNotEvenNumberException(Exception):
    pass


class EvenNumber(Integer):

    def __init__(self, number):
        super().__init__(number)

    def _validator(self, number_to_validate) -> None:
        super()._validator(number_to_validate)
        remainder = number_to_validate % 2
        if remainder == 0:
            return
        else:
            raise InputIsNotEvenNumberException("Input is an odd number, not an even number. Try again.")


class InputIsNotPrimeNumberException(Exception):
    pass


class PrimeNumber(Integer):

    def __init__(self, number):
        super().__init__(number)

    def _validator(self, number_to_validate):
        super()._validator(number_to_validate)
        if number_to_validate > 1:
            for i in range(2, int(number_to_validate / 2) + 1):
                if number_to_validate % i == 0:
                    raise InputIsNotPrimeNumberException("Input is not a prime number.")
            return
        else:
            raise InputIsNotPrimeNumberException("Input is not a prime number.")

    def prime_number_sequence_generator(self):
        pass


class OddPrimeNumber(OddNumber, PrimeNumber):

    def __init__(self, number):
        super().__init__(number)


class Number:

    def __init__(self, number):
        self.odd: OddNumber = None
        self.even: EvenNumber = None
        self.prime: PrimeNumber = None
        self.number: [Integer] = [self.odd, self.even, self.prime]
        for a_number in self.number:
            try:
                a_number = type(a_number)(number)
            except Exception:
                pass

        try:
            self.odd = OddNumber(number)
        except Exception:
            pass
        try:
            self.even = EvenNumber(number)
        except Exception:
            pass
        try:
            self.prime = PrimeNumber(number)
        except Exception:
            pass
        self.__number = number

    @property
    def value(self):
        return self.__number


    # except Exception as exception:
    #     if type(exception) in exception_list:
    #         self.__number = number
    #         # it stops initializing
    #     else:
    #         raise Exception("Input is not valid. Try again.")



        # exception_list = []
        # for super_class in list(Number.__bases__):
        #     try:
        #         super_class.__init__(self, number)
        #         # exception_scope = super_class.__name__
        #         # exception_name = "InputIsNot{}Exception".format(exception_scope)
        #     except Exception as exception_name:
        #         exception_list.append(exception_name)
