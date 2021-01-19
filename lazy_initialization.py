__author__ = "Bilal El Uneis & Jieshu Wang"
__since__ = "January 2021"
__email__ = "bilaleluneis@gmail.com, foundwonder@gmail.com"

from typing import Dict, Callable
from functools import lru_cache


def func_with_two_params(param_1: int, param_2: int) -> int:
    return param_1 + param_2


param_1_dict: Dict[str, int] = {"1": 1, "2": 2, "3": 3}
param_2_dict: Dict[str, int] = {"100": 100, "200": 200}

new_dict: Dict[str, Callable] = {}


def generate_func_call_dict(param_1s: Dict[str, int], param_2s: Dict[str, int]) -> Dict[str, Callable]:
    global new_dict
    new_dict = {}
    for key_1, item_1 in param_1s.items():
        for key_2, item_2 in param_2s.items():
            result_key = f'{key_1}_{key_2}'
            new_dict[result_key] = lambda: f"{item_1 + item_2}"
    return new_dict


class MyCallable:
    def __init__(self, i: int):
        self.__i = i

    def __call__(self) -> int:
        return self.__i + 100


def gen() -> Dict[str, MyCallable]:
    a_dict = {}
    for i in range(10):
        a_dict[f'{i}'] = MyCallable(i)
    return a_dict


if __name__ == "__main__":
    result = gen()
    print(result['1']())
    print(result['2']())


