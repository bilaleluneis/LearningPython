
__author__ = "Bilal El Uneis and Jieshu Wang"
__since__ = "July 2018"
__email__ = "bilaleluneis@gmail.com"

from re import findall
from re import IGNORECASE

some_text = "Some text to test some concept about soMe stuff in sOmE way!"


def get_number_of_occurrence(text_to_find, content_to_search):
    list_of_occurrence = findall(text_to_find, content_to_search, IGNORECASE)
    return len(list_of_occurrence)


# start of running code
if __name__ == "__main__":
    number_of_occurrence = get_number_of_occurrence("some", some_text)
    print('the word some was found {} times in "{}" '.format(number_of_occurrence, some_text))

