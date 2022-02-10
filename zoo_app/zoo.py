from datetime import datetime


class Zoo:

    def __init__(self, name):

        self.__name = name
        self.__city = 'Argentina'
        self.__operating_hours = '9 to 18'
        self.__animals = []

    def set_city(self, city_name):
        self.__city = city_name

    def set_operating_hours(self, operating_hours):
        self.__operating_hours = operating_hours

    def quantity_animals(self):
        return len(self.__animals)
    
    def add_animal(self, animal):
        self.__animals.append(animal)

    def remove_animal(self, animal_index):
        try:
            return self.__animals.pop(animal_index)
        except:
            raise Exception('The animal isn\'t in the zoo')

    def return_descriptions(self):
        all_animals_with_description = ''
        counter = 0

        for animal in self.__animals:
            all_animals_with_description += f'{counter}. {animal.species[0]} - {animal.name}: {animal.description}\n'
            counter += 1
        
        return all_animals_with_description

    def return_price(self, day):

        price_19_99 = [0, 1, 3, 4]
        price_9_99 = [2]
        price_25_99 = [5, 6]

        if day in price_19_99:
            return 19.99
        
        elif day in price_9_99:
            return 9.99
        
        elif day in price_25_99:
            return 25.99
        
        else:
            raise Exception('The day wasn\'t correct')

    @property
    def name(self):
        return self.__name

    @property
    def city(self):
        return self.__city
    
    @property
    def operating_hours(self):
        return self.__operating_hours
    

if __name__ == '__main__':

    garden = Zoo('Garden Zoo')

    garden.set_city('Jamaica')
    garden.set_operating_hours('11 to 22')

    print(garden.name)
    print(garden.city)
    print(garden.operating_hours)

    print(garden.return_price(datetime.today().weekday()))
    