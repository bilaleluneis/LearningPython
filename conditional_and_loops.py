
__author__ = "Bilal El Uneis"
__author__ = "Jieshu"
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

    print()
    print('Find the largest number example:')
    largest_num_so_far = 0
    print('Initially, the largest number is ', largest_num_so_far)
    for the_num in (9, 41, 12, 3, 89, 16):
        if the_num > largest_num_so_far:
            largest_num_so_far = the_num
        print(the_num, 'the largest number so far is', largest_num_so_far)

    print('Finally, the largest number is ', largest_num_so_far)


def sum_up_example_jieshu():

    print()
    print('Sum up exmple:')
    sum_so_far = 0
    print('Initially, the sum is ', sum_so_far)
    for the_num in (9, 41, 12, 3, 89, 16):
        sum_so_far = sum_so_far + the_num
        print(the_num, 'The sum so far is ', sum_so_far)

    print('The final sum is ', sum_so_far)


def average_example_jieshu():

    print()
    print('Calculate average example:')
    counter = 0
    sum_so_far = 0
    for the_num in (9, 41, 12, 3, 89, 16):
        counter = counter + 1
        sum_so_far = sum_so_far + the_num
        average_so_far = sum_so_far / counter
        print(the_num, ', the average so far is', average_so_far)

    print('the final average is ', average_so_far, ', approximately', round(average_so_far))


def average_example_jieshu_2(end_num):

    print()
    print('Average calculation example 2:')
    counter = 0
    sum_so_far = 0
    average_so_far = 0
    for the_num in range(1, end_num):
        counter = counter + 1
        sum_so_far = sum_so_far + the_num
        average_so_far = sum_so_far / counter
        print(the_num, ', the average so far is', average_so_far)

    print('The final average is ', average_so_far, ', approximately', int(average_so_far))


# start of running code
if __name__ == "__main__":

    if_example("Bilal")
    loop_example(20)
    if_example("Jieshu")
    find_largest_number_example_jieshu()
    sum_up_example_jieshu()
    average_example_jieshu()
    average_example_jieshu_2(18)
