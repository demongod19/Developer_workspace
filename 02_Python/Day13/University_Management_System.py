class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display_info(self):
        print(f"Name: {self.name}, Age: {self.age}")
class Student(Person):
    def __init__(self, name, age, Branch, CGPA):
        super().__init__(name, age)
        self.Branch = Branch
        self.CGPA = CGPA    

    def display_info(self):
        super().display_info()
        print(f"============ Student Information  ============")
        print(f"Name: {self.name}, Branch: {self.Branch}, CGPA: {self.CGPA}")
class Teacher(Person):
    def __init__(self, name, age, subject, Salary):
        super().__init__(name, age)
        self.subject = subject
        self.Salary = Salary

    def display_info(self):
        super().display_info()
        print(f"============ Teacher Information  ============")
        print(f"Name: {self.name}, Subject: {self.subject}, Salary: {self.Salary}  ")
person1 = Person("Alice", 20)
student1 = Student("Alice", 20, "Computer Science", 3.8) 
teacher1 = Teacher("Bob", 40, "Mathematics", 50000)
person1.display_info()
student1.display_info()
teacher1.display_info()