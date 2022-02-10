from .animal import Animal


class GiantTortoise(Animal):
    
    def __init__(self, name, num_legs, gender, age):
        Animal.__init__(self, name, num_legs, gender)
        self.__age = age
        self.__set_specie()

    def define_age(self):
        if self.__age < 50:
            return 'young'
        elif self.__age > 50 and self.__age < 100:
            return 'middle-age'
        else:
            return 'old'

    def __set_specie(self):
        self.species.append('Giant Tortoise')