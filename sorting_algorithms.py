
__author__ = "Jieshu Wang"
__since__ = "July 2018"
__email__ = "foundwonder@gmail.com"

from numpy import random as random_generator

# Generate several lists to be sorted
def lists_generator(end_number, list_size):
    already_sorted_list = list(range(list_size))
    random_list = random_generator.randint(end_number, size=list_size).tolist()
    reverse_sorted_list = already_sorted_list[::-1]
    print("The first list to sort is already sorted: {}".format(already_sorted_list))
    print("The second list to sort is random: {}".format(random_list))
    print("The third list to sort is reversely sorted: {}".format(reverse_sorted_list))
    return already_sorted_list, random_list, reverse_sorted_list

# Check if a list is sorted correctly
def sorting_finished_check(list_to_check):
    index = 0
    check = True
    while index < len(list_to_check) - 1:
        if list_to_check[index] > list_to_check[index + 1] or check == False:
            check = False
        index = index + 1
    return check


def bubble_sort(list_to_be_sorted):
    sorting_finished = sorting_finished_check(list_to_be_sorted)
    while not sorting_finished:
        index = 0
        while index < len(list_to_be_sorted) - 1:
            if list_to_be_sorted[index] > list_to_be_sorted[index + 1]:
                sort_num = list_to_be_sorted[index]
                list_to_be_sorted.pop(index)
                list_to_be_sorted.insert(index + 1, sort_num)
            index = index + 1
        sorting_finished = sorting_finished_check(list_to_be_sorted)
    print("Result after sorting is {}".format(list_to_be_sorted))


# start of running code
if __name__ == "__main__":
    (sorted, random, reversed) = lists_generator(100, 10)
    bubble_sort(sorted)
    bubble_sort(random)
    bubble_sort(reversed)