
__author__ = "Bilal El Uneis and Jieshu Wang"
__since__ = "July 2018"
__email__ = "bilaleluneis@gmail.com"


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


# Jieshu trying
def find_largest_number_example_jieshu():
    print('\nFind the largest number example:')
    largest_num_so_far = 0
    print('Initially, the largest number is ', largest_num_so_far)
    for the_num in (9, 41, 12, 3, 89, 16):
        if the_num > largest_num_so_far:
            largest_num_so_far = the_num
        print(the_num, 'the largest number so far is', largest_num_so_far)

    print('Finally, the largest number is ', largest_num_so_far)


def sum_up_example_jieshu():
    print('\nSum up example:')
    sum_so_far = 0
    print('Initially, the sum is ', sum_so_far)
    for the_num in (9, 41, 12, 3, 89, 16):
        sum_so_far = sum_so_far + the_num
        print(the_num, 'The sum so far is ', sum_so_far)

    print('The final sum is ', sum_so_far)


def average_example_jieshu():
    print('\nCalculate average example:')
    counter = 0
    sum_so_far = 0
    for the_num in (9, 41, 12, 3, 89, 16):
        counter = counter + 1
        sum_so_far = sum_so_far + the_num
        average_so_far = sum_so_far / counter
        print(the_num, ', the average so far is', average_so_far)

    print('the final average is ', average_so_far, ', approximately', round(average_so_far))


def average_example_jieshu_2(end_num):
    print('\nAverage calculation example 2:')
    counter = 0
    sum_so_far = 0
    average_so_far = 0
    for the_num in range(1, end_num):
        counter = counter + 1
        sum_so_far = sum_so_far + the_num
        average_so_far = sum_so_far / counter
        print(the_num, ', the average so far is', average_so_far)

    print('The final average is ', average_so_far, ', approximately', int(average_so_far))


def search_num_example_jieshu(end_num, search_num):
    print('\nSearch for the number of "', search_num, '" example:')
    found = False
    for the_num in range(0, end_num):
        if the_num == search_num:
            found = True
        print(the_num, found)
    if found:
        print('We found the number of {} here!'.format(search_num))
    else:
        print('The number of "', search_num, '" is not here.')


def find_in_list(number_to_find):
    number_found_in_list = None
    for a_number in [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]:
        if a_number == number_to_find:
            number_found_in_list = a_number
    print("\nNumber found in list is: ", number_found_in_list)


# start of running code
if __name__ == "__main__":
    if_example("Bilal")
    loop_example(20)
    if_example("Jieshu")
    find_largest_number_example_jieshu()
    sum_up_example_jieshu()
    average_example_jieshu()
    average_example_jieshu_2(18)
    search_num_example_jieshu(15, 23)
    search_num_example_jieshu(15, 5)
    find_in_list(10)
    find_in_list(9)
