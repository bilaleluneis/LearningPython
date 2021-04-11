from __future__ import annotations

from typing import Any
from unittest import TestCase, main

__author__ = "Bilal El Uneis"
__since__ = "March 2021"
__email__ = "bilaleluneis@gmail.com"


def init(self: Any, name: str, age: int) -> None:
    type(self).count += 1
    self.__name = name
    self.__age = age


def info(self: Any) -> tuple[str, int]:
    return self.__name, self.__age


methods: dict[str, Any] = {
    '__init__': init,
    'get_info': info,
    'count': 0
}

User = type('User', (object,), methods)


class TypeTests(TestCase):

    def test_meta_type(self) -> None:
        user1 = User('Bilal', 30)
        self.assertTrue(user1.get_info() == ('Bilal', 30) and user1.count == 1)
        user2 = User('Jieshu', 20)
        self.assertTrue(user2.get_info() == ('Jieshu', 20) and user2.count == 2)


if __name__ == '__main__':
    main()
