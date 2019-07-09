# author: Bilal El Uneis
# since: April 2018
# bilaleluneis@gmail.com

from enum import Enum, unique

"""
    Few interesting things I learned as I struggled with this
    first this is basically similar to what I did in LearningKotlin
    OperatorOverloading.kt.
    
    notice in Python when you declare the enum, they can have different
    values of different types and not forced to only stick to either Ints,String,Object
    of specific type, etc.
    
    the other thing that confused me and got me to spend time getting this to work
    is the fact when you say green = (blue, yellow) it creates object with name = green
    and value = tuple inside that tuple [0] = 'blue' as string and [1] = 'yellow' as string
    and not as enum, basically its like looking at the blue and yellow as pointer and you 
    pull the content of the memory!
    
    I still have mixed feelings about this language, but I can see how flexible it can be.
"""


@unique
class Constants(Enum):
    RASPBERRY_PI: str = "RP"
    TINKER_BOARD: str = "TB"
    BANANA_PI: str = "BP"  # if you change this to RP, you will get error because of the @unique decorator


class Colors(Enum):
    unknown_color = ()  # empty tuple
    blue = "blue"
    red = "red"
    yellow = "yellow"
    green = (blue, yellow)
    orange = (red, yellow)

    def __add__(self, other_color):
        for color in Colors:
            if color is Colors.unknown_color:
                continue
            elif color.value[0] is self.name and color.value[1] is other_color.name:
                return color
            elif color.value[1] is other_color.name and color.value[0] is self.name:
                return color

        return Colors.unknown_color  # exited loop and no match found


def main():
    print(Constants.RASPBERRY_PI)
    # uncomment bellow to see error !
    # Constants.RASPBERRY_PI = "BPI"
    what_color_am_i = Colors.red + Colors.yellow
    print(what_color_am_i)


# start of running code
if __name__ == "__main__":
    main()
