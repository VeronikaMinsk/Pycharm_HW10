# Доработаем задачи 5-6. Создайте класс-фабрику.
# ○ Класс принимает тип животного (название одного из созданных классов)
# и параметры для этого типа.
# ○ Внутри класса создайте экземпляр на основе переданного типа и
# верните его из класса-фабрики.



class Animal:
    def __init__(self, name):
        self.name = name

    def animal_name(self):
        return f'Имя: {self.name}'


class Fish(Animal):
    def __init__(self, name, depth):
        super().__init__(name)
        self.depth = depth

    def get_info(self):
        return f'Глубина обитания: {self.depth} m'


class Bird(Animal):
    def __init__(self, name, wingspan):
        super().__init__(name)
        self.wingspan = wingspan

    def get_info(self):
        return f'Размах крыльев: {self.wingspan} sm'

class Dog(Animal):
    def __init__(self, name, withers_height):
        super().__init__(name)
        self.withers_height = withers_height

    def get_info(self):
        return f'Высота холки: {self.withers_height} sm'

class Reptile(Animal):
    def __init__(self, name, length):
        super().__init__(name)
        self.length = length

    def get_info(self):
        return f'Длина тела: {self.length} m'


class AnimalFactory:

    def create_animal(animal_type, name, *args):
        if animal_type == 'Fish':
            return Fish(name, *args)
        elif animal_type == 'Bird':
            return Bird(name, *args)
        elif animal_type == 'Dog':
            return Dog(name, *args)
        elif animal_type == 'Reptile':
            return Reptile(name, *args)
        else:
            raise ValueError(f"Unsupported animal type: {animal_type}")

if __name__ == '__main__':
    animal_factory = AnimalFactory

    fish = animal_factory.create_animal('Fish', 'Som', 5)
    bird = animal_factory.create_animal('Bird', 'Parrot', 10)
    dog = animal_factory.create_animal('Dog', 'Mops', 25)
    reptile = animal_factory.create_animal('Reptile', 'Anaconda', 3)

    print(fish.animal_name())
    print(fish.get_info())
    print(bird.animal_name())
    print(bird.get_info())
    print(reptile.animal_name())
    print(reptile.get_info())
    print(dog.animal_name())
    print(dog.get_info())
