
__author__ = "Jieshu Wang"
__since__ = "July 2018"
__email__ = "foundwonder@gmail.com"

from numpy import random as random_generator

# this is the better way to do this.. but will look at it later
# class TestListsForSorting:
#
#     def __init__(self, list_size, end_number):
#         self.already_sorted_list = list(range(list_size))
#         self.random_list = random_generator.randint(end_number, size=list_size)
#         self.reverse_sorted_list = self.already_sorted_list[::-1]


# Generate several lists to be sorted
def lists_generator(end_number, list_size):
    already_sorted_list = list(range(list_size))
    random_list = random_generator.randint(end_number, size=list_size)
    reverse_sorted_list = already_sorted_list[::-1]
    print("The first list to sort is already sorted: {}".format(already_sorted_list))
    print("The second list to sort is random: {}".format(random_list))
    print("The third list to sort is reversely sorted: {}".format(reverse_sorted_list))
    return already_sorted_list, random_list, reverse_sorted_list


# Check if a list is sorted correctly
def sorting_finished_check():
    counter = 0
    pass


def bubble_sort(list_to_be_sorted):
    list_sorted = list()
    sorting_finished = False
    while not sorting_finished:
        counter = 0
        for each_num in list_to_be_sorted:
            if list_to_be_sorted[counter] > list_to_be_sorted[counter + 1]:
                list_to_be_sorted.pop(counter)
                list_to_be_sorted.insert(counter + 1, each_num)
            counter = counter + 1





# start of running code
if __name__ == "__main__":
    # lists_for_testing = TestListsForSorting(15, 100)
    (sorted, random, reversed) = lists_generator(100, 15)
    bubble_sort(sorted)
    bubble_sort(random)