#Employee management system
class Employee:
    def __init__(self, name, age, salary):
        self.name = name
        self.age = age
        self.salary = salary

    def display_info(self):
        print(f"========== Employee ==========")
        print(f"\n Name : {self.name}, \n Age: {self.age}, \n Salary: {self.salary} \n ====================")
class Manager(Employee):
    def __init__(self, name, age, salary, department):
        super().__init__(name, age, salary)
        self.department = department

    def display_info(self):
        super().display_info()
        print(f"========== Manager ==========")
        print(f"Department: {self.department} \n ====================")
print("**********   Employee Management System **********")
employee = Employee("Pratik", 30, 90000)
manager = Manager("Alice Johnson", 35, 100000, "Marketing")
employee.display_info()
manager.display_info()