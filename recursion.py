
__author__ = "Bilal El Uneis and Jieshu Wang"
__since__ = "July 2018"
__email__ = "bilaleluneis@gmail.com"


def fibonacci(number):
    if number <= 1:
        print("Base Condition where number is < or = to 1 is met, returning {}".format(number))
        return number
    else:
        print("Recursive condition calling fibonacci({}) + fibonacci({})".format(number - 1, number - 2))
        return fibonacci(number - 1) + fibonacci(number - 2)


# start of running code
if __name__ == "__main__":

    result = fibonacci(1)
    print("Final Result of is {}\n\n".format(result))

    result = fibonacci(4)
    print("Final Result of is {}\n\n".format(result))

    result = fibonacci(5)
    print("Final Result of is {}\n\n".format(result))

    result = fibonacci(9)
    print("Final Result of is {}".format(result))
