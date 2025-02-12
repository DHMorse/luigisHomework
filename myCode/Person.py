class Person:
    name: str = ''
    height: int = 0
    weight: int = 0
    mealSize: int = 0

    def __init__(self, name, height, weight, mealSize):
        self.name: str = name
        self.height: int = height
        self.weight: int = weight
        self.mealSize: int = mealSize

    def display(self):
        print(f'Name: {self.name}')
        print(f'Height: {self.height}')
        print(f'Weight: {self.weight}')

    def eat(self):
        self.weight += self.mealSize
