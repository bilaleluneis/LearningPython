
__author__ = "Bilal El Uneis and Jieshu Wang"
__since__ = "July 2018"
__email__ = "bilaleluneis@gmail.com"

from numpy import random as random_generator


def if_example(name):
    if name == "Jieshu":
        for x in name:
            if x == "s":
                continue
            print(x)
    else:
        print("Check failed!")


def loop_example(counter):
    while counter > 0:
        print(counter)
        counter = counter + 1
        if counter == 100:
            break


def find_largest_number_example(end_num, num_size):
    find_largest_number_list = random_generator.randint(end_num, size=num_size)
    print('\nExample: Find the largest number in the list {}:'.format(find_largest_number_list))
    largest_num_so_far = None
    print('Initially, the largest number is {}'.format(largest_num_so_far))
    for the_num in find_largest_number_list:
        if largest_num_so_far is None or the_num > largest_num_so_far:
            largest_num_so_far = the_num

        print('{}, the largest number so far is {}'.format(the_num, largest_num_so_far))

    print('Finally, the largest number is {}'.format(largest_num_so_far))


def sum_up_example(end_num, num_size):
    sum_up_example_list = random_generator.randint(end_num, size=num_size)
    print('\nExample: Sum up the number in the list of {}:'.format(sum_up_example_list))
    sum_so_far = 0
    print('Initially, the sum is {}'.format(sum_so_far))
    for the_num in sum_up_example_list:
        sum_so_far = sum_so_far + the_num
        print('{}, The sum so far is {}'.format(the_num, sum_so_far))

    print('The final sum is {}'.format(sum_so_far))


def average_example(end_num, num_size):
    average_example_list = random_generator.randint(end_num, size=num_size)
    print('\nExample: Calculate average of the number in the list of {}:'.format(average_example_list))
    counter = 0
    sum_so_far = 0
    average_so_far = 0
    for the_num in average_example_list:
        counter = counter + 1
        sum_so_far = sum_so_far + the_num
        average_so_far = sum_so_far / counter
        print('{}, the average so far is {}'.format(the_num, average_so_far))

    print('the final average is {}, approximately {}'.format(average_so_far, int(average_so_far)))


def search_num_example(end_num, search_num):
    print('\nSearch for the number of "{}" example:'.format(search_num))
    found = False
    for the_num in range(0, end_num):
        if the_num == search_num:
            found = True
        print(the_num, found)
    if found:
        print('We found the number of {} here!'.format(search_num))
    else:
        print('The number of {} is not here.'.format(search_num))


def find_in_list(number_to_find):
    number_found_in_list = None
    for a_number in [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]:
        if a_number == number_to_find:
            number_found_in_list = a_number
    print("\nNumber found in list is: {}".format(number_found_in_list))


# start of running code
if __name__ == "__main__":
    if_example("Bilal")
    loop_example(20)
    if_example("Jieshu")
    find_largest_number_example(100, 8)
    sum_up_example(50, 8)
    average_example(80, 10)
    search_num_example(15, 23)
    search_num_example(15, 5)
    find_in_list(10)
    find_in_list(9)
