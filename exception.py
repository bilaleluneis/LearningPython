
__author__ = "Bilal El Uneis & Jieshu"
__since__ = "July 2018"
__email__ = "bilaleluneis@gmail.com"


def add_two_numbers(first_number, second_number):
    if isinstance(first_number, int) and isinstance(second_number, int):
        return first_number + second_number
    else:
        raise Exception("Parameters passed should be of type Integer only!")


def adder(number, another_number):
    try:
        return add_two_numbers(number, another_number)
    except Exception as adder_exception:
        print("ERROR: {}".format(adder_exception))


# Jieshu Wang
def validate_console_input_is_positive_number():
    input_number = input("Enter a positive number: ")
    try:
        if input_number.isdigit() and int(input_number) > 0:
            print("Value entered is a positive number .. Good Job!! ")
        else:
            raise Exception
    except Exception as exception:
        print("Value entered is not a positive number .. Try again !! {}".format(exception))

#Jieshu tries again. I know if-else can have the same effect without try-except. Is that what u mean?
def validate_console_input_is_positive_integer():
    input_integer = input("enter a positive integer: ")
    if input_integer.isdigit() and int(input_integer) > 0:
        print("This is a positive integer. Good Job.")
    else:
        print ("Value entered should be a positive integer. Try again!")

#Jieshu: there's a problem. If you enter a decimal number, say 2.1, it supposed to output "Value entered is a float...blabla," but it actually output the except.
def validate_console_input_is_positive_integer_2():
    input_integer_2 = input("enter a positive integer: ")
    try:
        if int(input_integer_2) > 0:
            print("Nice job!")
        elif float(input_integer_2) > 0:
            print("Value entered is a float, not an integer. Try again!")
        else:
            print("Number entered is not positive. Try again!")
    except:
        print ("Value entered is not a number. Try again!")



# start of running code
if __name__ == "__main__":
    valid_addition = adder(1, 2)
    print("calling adder() with values 1 and 2 passed as parameters resulted in {}".format(valid_addition))
    exception_thrown = adder(1.5, 2.5)  # this will print exception message
    validate_console_input_is_positive_number()
    validate_console_input_is_positive_integer()
    validate_console_input_is_positive_integer_2()
