__author__ = "Bilal El Uneis"
__since__ = "April 2020"
__email__ = "bilaleluneis@gmail.com"

from abc import abstractmethod
from typing import Any, Optional, Callable, Union
from typing_extensions import Protocol
from unittest import TestCase, main

Number = Union[int, float]


class FunctionalInterface(Protocol):

    @abstractmethod
    def __call__(self) -> Optional[Any]: ...


class BinaryFunction(FunctionalInterface):

    def __init__(self, name: str, func: Callable[[Number, Number], Number]):
        self.__name = name
        self.__func = func

    @property
    def name(self) -> str:
        return self.__name

    def __call__(self, *args: Any, **kwds: Any) -> Optional[Any]:
        return self.__func(*args)


class IntAdder(Functional):

    def __init__(self, first: int, second: int):
        self.__first = first
        self.__second = second

    def __call__(self, *args: Any, **kwds: Any) -> Optional[Any]:
        return self.__first + self.__second


""" Unit Tests Utils """


def _add(x: int, y: int) -> int:
    return x + y


""" Tests """


class FunctionTypeTests(TestCase):

    def setUp(self) -> None:
        self.adder: Optional[BinaryFunction] = None

    def test_instance_with_lamda(self) -> None:
        self.adder = BinaryFunction("adder", lambda x, y: int(x) + int(y))
        self.assertEqual(self.adder(1, 2), 3)

    def test_instance_with_function(self) -> None:
        self.adder = BinaryFunction("adder", _add)
        self.assertEqual(self.adder(1, 2), 3)

    def test_int_adder(self) -> None:
        self.assertEqual(IntAdder(1, 2)(), 3)


if __name__ == '__main__':
    main()
