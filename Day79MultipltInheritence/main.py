class Employee:
    def __init__(self, name) -> None:
        self.name = name

    def show(self):
        print(f"The name is {self.name}")

class Dancer:
    def __init__(self, dance) -> None:
        self.dance = dance

    def show(self):
        print(f"The dance is {self.dance}")

class DancerEmployee(Employee, Dancer):
    def __init__(self, name, dance) -> None:
        self.name = name
        self.dance = dance


o = DancerEmployee("Shivani", "Kathak")
print(o.name)
print(o.dance)
o.show() # This is because Employee class is written earlier then Dancer
print(DancerEmployee.mro()) # Method Resolution Order