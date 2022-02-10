from animal import Animal


class Crocodile(Animal):
    
    def __init__(self, name, num_legs, gender, teeth):
        Animal.__init__(self, name, num_legs, gender)
        self.__teeth = teeth
        self.__set_specie()

    def favourite_food(self):
        return f'My favourite food is HUMAN and I eat them with my {self.__teeth} theets.'

    def __set_specie(self):
        self.species.append('Crocodile')
    
