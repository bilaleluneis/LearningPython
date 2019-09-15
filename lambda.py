from typing import Callable, Dict

__author__ = "Bilal El Uneis"
__since__ = "Sept 2019"
__email__ = "bilaleluneis@gmail.com"

math_operations: Dict[str, Callable[[int, int], int]] = {
    "+": lambda x, y: x + y,
    "-": lambda x, y: x - y,
}


def main():
    operator: str = "-"
    operation: Callable[[int, int], int] = math_operations[operator]
    x: int = 3
    y: int = 5
    print("result of {} operation on x ={} and y ={} is {}".format(operator, x, y, operation(x, y)))


# start of running code
if __name__ == "__main__":
    main()
