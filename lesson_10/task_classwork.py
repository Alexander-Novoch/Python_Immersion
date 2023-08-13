class Animal:
    def __init__(self, name: str, color: str, size: float):
        self.name = name
        self.color = color
        self.size = size

    def show_unique(self):
        pass


class Fish(Animal):
    def __init__(self, name: str, color: str, size: float, max_depth: float):
        super().__init__(name, color, size)
        self.max_depth = max_depth

    def show_unique(self):
        print(self.max_depth)


class Bird(Animal):
    def __init__(self, name: str, color: str, size: float, habitat: str):
        super().__init__(name, color, size)
        self.habitat = habitat

    def show_unique(self):
        print(self.habitat)


class Cat(Animal):
    def __init__(self, name: str, color: str, size: float, hairy: bool):
        super().__init__(name, color, size)
        self.hairy = hairy

    def show_unique(self):
        print(self.hairy)


if __name__ == '__main__':
    fish = Fish('Morty', 'rasberry', 15.3, 12.5)
    bird = Bird("Kiwi", "white & red", 25.8, "forest")
    cat = Cat('Tom', 'black & white', 36.8, True)

    animals = (fish, bird, cat)
    for a in animals:
        a.show_unique()
