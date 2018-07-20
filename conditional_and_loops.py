
__author__ = "Bilal El Uneis"
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
        if counter == 1000:
            break


# start of running code
if __name__ == "__main__":

    if_example("Bilal")
    loop_example(20)
    if_example("Jieshu")
