from abc import ABC


class Animal(ABC):

    def __init__(self, name, num_legs, gender):
        self.species = []
        self.__name = name
        self.__num_legs = num_legs
        self.__gender = gender

    @property
    def description(self):
        return f'{self.__name} is {self.__gender} and has {self.__num_legs} legs.'

    @property
    def name(self):
        return self.__name
