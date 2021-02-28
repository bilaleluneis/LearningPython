__author__ = "Bilal El Uneis"
__since__ = "April 2020"
__email__ = "bilaleluneis@gmail.com"

from functools import wraps
from typing import Callable
from unittest import TestCase, main


def no_arg_decorator(function: Callable[[], str]) -> Callable[[], str]:
    @wraps(function)
    def wrapper() -> str:
        print(f'before calling {function.__name__}')
        return function()

    return wrapper


@no_arg_decorator
def greet() -> str:
    return "Hello"


class _ArgDecorator:
    def __init__(self, func: Callable[[], str], msg: str):
        self.func = func
        self.msg = msg

    def __call__(self) -> str:
        print(f'message is {self.msg}')
        return self.func()


def arg_decorator(msg: str) -> Callable[[Callable[[], str]], _ArgDecorator]:
    def wrapper(func: Callable[[], str]) -> _ArgDecorator:
        return _ArgDecorator(func, msg)
    return wrapper


# def arg_decorator(message: str) -> Callable[[Callable[[], str]], str]:
#     def internal_decorator(function: Callable[[], str]) -> str:
#         print(message)
#         return no_arg_decorator(function)()
#
#     return internal_decorator


@arg_decorator('Good morning')
def greet_again() -> str:
    return "Hello"


class DecoratorTests(TestCase):

    def test_decortor(self) -> None:
        print(greet_again())
        self.assertEqual(1, 1)


if __name__ == '__main__':
    main()
