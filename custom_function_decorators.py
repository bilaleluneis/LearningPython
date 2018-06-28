
__author__ = "Bilal El Uneis"
__since__ = "June 2018"
__email__ = "bilaleluneis@gmail.com"


def simple_decorator(another_function):
    def wrapper_function():
        print("simple_decorator functionality applied!")
        return another_function()  # this will execute another_function
    return wrapper_function  # this will return reference to wrapper_function


def another_decorator(another_function):
    def wrapper_function():
        print("another_decorator functionality applied!")
        return another_function()
    return wrapper_function


@simple_decorator
def simple_function():
    print("simple function executed!")


@simple_decorator
@another_decorator
def another_function_example():
    print("another function example executed!")


# start of running code
if __name__ == "__main__":
    simple_function()
    another_function_example()
