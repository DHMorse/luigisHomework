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
