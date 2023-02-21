class Employee:
    def __init__(self, name) -> None:
        self.name = name

    def __len__(self):
        i = 0
        for c in self.name:
            i = i + 1
        return i
    
    def __str__(self) -> str:
        return f"The Name of the Emplyee is {self.name}"

    def __repr__(self) -> str:
        return f"The Name of the Emplyee is {self.name} repr"

    def __call__(self):
        print("Hey I am good")