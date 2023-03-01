class Animal:
    def __init__(self, name):
        self.name = name

    def show_details(self):
        print("Name:", self.name)

class Dog(Animal):
    def __init__(self, name, breed):
        super().__init__(name)
        self.breed = breed

    def show_details(self):
        super().show_details()
        print("Species: Dog")
        print("Breed:", self.breed)

class Cat(Animal):
    def __init__(self, name, color):
        super().__init__(name)
        self.color = color

    def show_details(self):
        super().show_details()
        print("Species: Cat")
        print("Color:", self.color)

d = Dog("Max", "Golder Retriever")
d.show_details()

c = Cat("Luna", "Black")
c.show_details()
