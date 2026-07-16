class Employee:
    def __init__(self, name, age, salary):
        self.name = name
        self.age = age
        self.salary = salary

    def display(self):
        print(f"Name: {self.name}, Age: {self.age}, Salary: {self.salary}")

class Developer(Employee):
    def __init__(self, name, age, salary, programming_language):
        super().__init__(name, age, salary)
        self.programming_language = programming_language

    def display(self):
        super().display()
        print(f"Programming Language: {self.programming_language}")
class Designer(Employee):
    def __init__(self, name, age, salary, design_tool):
        super().__init__(name, age, salary)
        self.design_tool = design_tool

    def display(self):
        super().display()
        print(f"Design Tool: {self.design_tool}")
class Tester(Employee):
    def __init__(self, name, age, salary, testing_framework):
        super().__init__(name, age, salary)
        self.testing_framework = testing_framework

    def display(self):
        super().display()
        print(f"Testing Framework: {self.testing_framework}")

developer1 = Developer("Alice", 30, 60000, "Python")
designer1 = Designer("Bob", 28, 55000, "Adobe XD")  
Tester1 = Tester("Charlie", 32, 50000, "Selenium")
developer1.display()
designer1.display() 
Tester1.display()