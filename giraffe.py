from animal import Animal


class Giraffe(Animal):
    
    def __init__(self, name, num_legs, gender, meters):
        Animal.__init__(self, name, num_legs, gender)
        self.__meters = meters
        self.__set_specie()
        
    def compare_height(self, giraffe):
        return f'The giraffe {self.name} has {self.__meters} meters, and the giraffe {giraffe.name} has {giraffe.meters} meters.'

    @property
    def meters(self):
        return self.__meters

    def __set_specie(self):
        self.species.append('Giraffe')

if __name__ == '__main__':

    jirafa = Giraffe('greg', 4, 'Male', 5)
