from abc import ABC, abstractmethod

__author__ = "Bilal El Uneis and Jieshu Wang"
__since__ = "June 2018"
__email__ = "bilaleluneis@gmail.com"

"""
Animal is an abstract class and I shouldn't be able to create instance of it, but in python there is no 
abstract keyword or feature that is part of the language construct, there is API that simulate such behaviour
by extending ABC class (Abstract Base Class).I also found that I could break it and create instance of it
unless I introduce an abstract method using abstractmethod decorator in this example.
"""


class Animal (ABC):

    def __init__(self, category=None):
        self.category = category
        super().__init__()

    @abstractmethod
    def speak(self):
        print("not sure what sound I should make!!")


class Dog (Animal):

    def __init__(self):
        super().__init__()
        self.category = "Canine"

    def speak(self):
        print("Wooof!!")


class Cat (Animal):

    def __init__(self):
        super().__init__()
        self.category = "Feline"

    def speak(self):
        print("Meaw!!")


class Rat (Animal):

    def __init__(self):
        super().__init__()
        self.category = "Rodent"

    def speak(self):
        print("Whatever a Rat says!!")


class NewlyDiscoveredAnimal (Animal):

    def __init__(self):
        super().__init__()
        self.category = "new category"

    def speak(self):
        super().speak()


# start of running code
if __name__ == "__main__":
    # animal = Animal() # if uncommented this will throw error, you cant create instance of abstract class
    collectionOfAnimals = [Cat(), Rat(), Dog(), NewlyDiscoveredAnimal()]
    for animal in collectionOfAnimals:
        if isinstance(animal, Animal):
            animal.speak()


