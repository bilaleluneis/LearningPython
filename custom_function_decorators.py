
__author__ = "Bilal El Uneis"
__since__ = "June 2018"
__email__ = "bilaleluneis@gmail.com"


def simple_decorator(another_function):
    def wrapper_function():
        print("applying some decorator functionality!")
        return another_function()  # this will execute another_function
    return wrapper_function  # this will return reference to wrapper_function


@simple_decorator
def simple_function():
    print("simple function executed!")


# start of running code
if __name__ == "__main__":
    simple_function()
