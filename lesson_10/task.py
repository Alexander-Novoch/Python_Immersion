# Доработаем задания 5-6. Создайте класс-фабрику.
# Класс принимает тип животного (название одного из созданных классов) и параметры для этого типа.
# Внутри класса создайте экземпляр на основе переданного типа и верните его из класса-фабрики.


from enum import Enum
from task_classwork import Animal, Bird, Fish, Cat


class TypeAnimal(Enum):
    fish = Fish
    bird = Bird
    cat = Cat


class Factory:
    def __init__(self):
        pass

    def build_animal(self, type_animal: TypeAnimal, name: str, color: str, size: float, *args) -> TypeAnimal:
        return f'type - {type_animal}, name - {name}, color - {color}, size - {size}, unique - {str(*args)}'
        # return [{type_animal: [name, color, size, *args]}]
        # animal = type_animal.value(name, color, size, *args)
        # return animal


if __name__ == '__main__':
    animal_1 = Factory.build_animal(TypeAnimal.fish, TypeAnimal.fish.name, 'Larry', 'purpur', 25.6, 12)
    animal_2 = Factory.build_animal(TypeAnimal.bird, TypeAnimal.bird.name, 'Joe', 'grey', 15.9, 'forest')
    animal_3 = Factory.build_animal(TypeAnimal.cat, TypeAnimal.cat.name, 'Sally', 'white', 35.6, True)

    animals_of_factory = (animal_1, animal_2, animal_3)
    for a in animals_of_factory:
        print(a)
