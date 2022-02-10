from datetime import datetime

from .zoo import Zoo
from .giraffe import Giraffe
from .giant_tortoise import GiantTortoise
from .crocodile import Crocodile


class ZooApp:

    def __init__(self):
        self.__zoo = None
        self.__started = True
        self.__option = None
        self.__today = datetime.today().weekday()

    def start(self):
        while self.__option != '10':
            self.__get_inputs()
            self.__do_updates()
            self.__do_outputs()

    def __get_inputs(self):
        if self.__started:
            self.__zoo_name = input('What\'s the name of the zoo? ')

        if self.__option == 0:
            self.__option = input('What\'s your move? ')

        if self.__option == '1':
            self.__city = input('City Name: ')
        
        if self.__option == '2':
            self.__hours = input('From, to: ')
        
        if self.__option == '3':
            self.__animal = input('1. Giraffe\n2. Crocodile\n3. Giant Tortoise\nPlease, type the number of the animal to add: ')
            self.__name = input('Name: ')
            self.__num_legs = input('Legs: ')
            self.__gender = input('Gender: ')

            if self.__animal == '1':
                self.__meters = input('Meters: ')
            elif self.__animal == '2':
                self.__teeths = input('Teeths: ')
            elif self.__animal == '3':
                self.__age = int(input('Age: '))
            else:
                return

        if self.__option == '4':
            if self.__zoo.quantity_animals() == 0:
                print()
                print('There are not any animals yet.')
                print()
                return
            print(self.__zoo.return_descriptions())
            self.__animal_remove = int(input('Type the number of the animal to remove: '))
    

    def __do_updates(self):
        if self.__started:
            self.__zoo = Zoo(self.__zoo_name)
            self.__started = False
            self.__option = 0
        
        if self.__option == '1':
            self.__zoo.set_city(self.__city)
            self.__option = 0

        if self.__option == '2':
            self.__zoo.set_operating_hours(self.__hours)
            self.__option = 0

        if self.__option == '3':
            if self.__animal == '1':
                self.__giraffe = Giraffe(self.__name, self.__num_legs, self.__gender, self.__meters)
                self.__zoo.add_animal(self.__giraffe)
                self.__option = 0

            elif self.__animal == '2':
                self.__crocodile = Crocodile(self.__name, self.__num_legs, self.__gender, self.__teeths)
                self.__zoo.add_animal(self.__crocodile)
                self.__option = 0

            elif self.__animal == '3':
                self.__gian_tortoise = GiantTortoise(self.__name, self.__num_legs, self.__gender, self.__age)
                self.__zoo.add_animal(self.__gian_tortoise)
                self.__option = 0

        if self.__option == '4':
            if self.__zoo.quantity_animals() == 0:
                self.__option = 0
                return
            try:
                self.__zoo.remove_animal(self.__animal_remove)
                self.__option = 0
            except Exception as e:
                print(e)
                self.__option = 0
                return

        if self.__option == '5':
            return

        if self.__option == '10':
            return

        else:
            if self.__option == 0:
                return
            self.__option = 'Error'

    def __do_outputs(self):
        if self.__option == 'Error':
            print()
            print('We found an error while processing your answer, please, try again')
            print()
            self.__option = 0

        if self.__option == '5':
            print(self.__zoo.return_descriptions())
            self.__option = 0

        if self.__option != '10':
            print()
            print(f'**************** Zoo {self.__zoo.name} ****************')
            print()
            print(f'Zoo hours: {self.__zoo.operating_hours}')
            print(f'Zoo city: {self.__zoo.city}')
            print(f'Today\'s price: ${self.__zoo.return_price(self.__today)}')
            print()
            print('-----> These are the available options:')
            print()
            print('1. Set the city (if you are not in ARG).')
            print('2. Set the operating hours (if those are not 9 to 18).')
            print('3. Add an animal to the Zoo.')
            print('4. Remove an animal of the Zoo.')
            print('5. See all animals and descriptions')
            print('10. Quit')
            print()
