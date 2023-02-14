class Employee:
    companyName = "Apple"
    noOfEmployees = 0
    def __init__(self, name) -> None:
        self.name = name
        self.raise_amount = 0.02
        Employee.noOfEmployees += 1

    def showDetails(self):
        print(f"The name of the Employee is {self.name} and the raise amount i {self.noOfEmployees} sized {self.companyName} is {self.raise_amount}")


emp1 = Employee("Aniket")
emp1.raise_amount = 0.3
emp1.companyName = "Apple India"
emp1.showDetails()
# Employee.showDetails(emp1)

Employee.companyName = "Google"
print(Employee.companyName)

emp2 = Employee("Rohan")
emp2.companyName = "Nestle"
emp2.showDetails()