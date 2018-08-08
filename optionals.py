
__author__ = "Bilal El Uneis"
__since__ = "August 2018"
__email__ = "bilaleluneis@gmail.com"

from typing import Optional


def get_index(value_to_find_index: int, the_list_to_search: [int]) -> Optional[int]:
    counter = 0
    for value in the_list_to_search:
        if value == value_to_find_index:
            return counter
        counter += 1
    return None


def main():
    list_to_search = [1, 2, 3, 5, 8, 9, 0, 20, 90]
    first_search = get_index(value_to_find_index=10, the_list_to_search=list_to_search)
    second_search = get_index(value_to_find_index=9, the_list_to_search=list_to_search)
    print("got {} when searching for {} in {}".format(first_search, 10, list_to_search))
    print("got {} when searching for {} in {}".format(second_search, 9, list_to_search))
    pass


# start of running code
if __name__ == "__main__":
    main()  # from now on, this is how I will do it, so that I can scope same named vars and not expose them outside!
