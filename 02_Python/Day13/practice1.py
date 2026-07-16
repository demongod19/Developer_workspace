class person:
     def __init__(self, name, age):
            self.name = name
            self.age = age
     def display(self):
        print(f"Name: {self.name}, Age: {self.age}")

class Employee(person):
    def __init__(self, name, age, salary):
        super().__init__(name, age)
        self.salary = salary

    def display(self):
        print(f"Name: {self.name}, Age: {self.age}, Salary: {self.salary}")

class Manager(Employee):
    def __init__(self, name, age, salary, department):
        super().__init__(name, age, salary)
        self.department = department

    def display(self):
        super().display()
        print(f"Department: {self.department}")

person1 = person("Alice", 30)
employee1 = Employee("Bob", 25, 50000)
manager1 = Manager("Charlie", 40, 80000, "Sales")

person1.display()
employee1.display()
manager1.display()