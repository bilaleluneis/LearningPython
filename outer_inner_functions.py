
__author__ = "Bilal El Uneis"
__since__ = "June 2018"
__email__ = "bilaleluneis@gmail.com"


def print_message(message):

    def message_printer():
        print(message)

    return message_printer()


def return_message(message):

    def message_printer():
        print(message)

    return message_printer


def simple_function():
    print("just a simple function")


# example of what will become a decorator @
def decorator_function(another_function):
    def wrapper_function():
        return another_function()  # this will execute another_function
    return wrapper_function  # this will return reference to wrapper_function


# start of running code
if __name__ == "__main__":

    print_message("printing Hi Bilal!")
    returned_message = return_message("returning Hi Bilal!")
    returned_message()
    decorator = decorator_function(simple_function)
    decorator()


