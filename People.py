# People.py

class Person:
    name = ""
    height = 0
    weight = 0
    meal_size = 0

    def __init__(self, name, height, weight, meal_size):
        self.name = name
        self.height = height
        self.weight = weight
        self.meal_size = meal_size

    def display(self):
        print("Name:", self.name)
        print("Height:", self.height)
        print("Weight:", self.weight)

    def eat(self):
        self.weight = self.weight + self.meal_size

p1 = Person("Jack Sprat", 70, 150, 1)
p2 = Person("Joan Sprat", 63, 240, 3)

p1.display()
p2.display()

p1.eat()
p2.eat()

p1.display()
p2.display()
