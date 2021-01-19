__author__ = "Bilal El Uneis"
__since__ = "April 2020"
__email__ = "bilaleluneis@gmail.com"

from typing import Tuple
from unittest import TestCase, main


class Function:

    def __init__(self, x: int, y: int, z: int) -> None:
        self.__x: int = x
        self.__y: int = y
        self.__z: int = z

    def __call__(self, multiplier: int = 1) -> Tuple[int, int, int]:
        return multiplier * self.__x, multiplier * self.__y, multiplier * self.__z

    @property
    def z(self) -> int:
        return self.__z

    @z.setter
    def z(self, new_z: int) -> None:
        self.__z = new_z


class CallableTests(TestCase):

    def test_1(self) -> None:
        self.assertEqual(Function(1, 2, 3)(), (1, 2, 3))

    def test_2(self) -> None:
        f = Function(1, 2, 3)
        self.assertTrue(f(), (1, 2, 3))
        self.assertTrue(f(2), (2, 4, 6))

        f.z = 4
        self.assertTrue(f(), (1, 2, 4))


if __name__ == '__main__':
    main()
