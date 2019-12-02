__author__ = "Bilal El Uneis"
__since__ = "July 2019"
__email__ = "bilaleluneis@gmail.com"

from typing import TypeVar, SupportsInt, Type

T = TypeVar("T", int, bool)


def main():
    int_var: T = int(1)
    boolean_var: T = bool(0)
    string_var: T = "duh"
    string_float: T = float(2.0)


# start of running code
if __name__ == "__main__":
    main()
