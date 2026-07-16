# Day 13 - Python Notes
**Topic:** Inheritance in Python (OOP)

---

# 1. Inheritance

Inheritance allows one class to acquire the properties and methods of another class.

### Syntax

```python
class Parent:
    pass

class Child(Parent):
    pass
```

Advantages:
- Code Reusability
- Easy Maintenance
- Better Program Structure
- Supports Polymorphism

---

# 2. Types of Inheritance

## A) Single Inheritance

One child class inherits from one parent class.

```
Parent
   │
 Child
```

Example:

```python
class Animal:
    def sound(self):
        print("Animal makes sound")

class Dog(Animal):
    def bark(self):
        print("Dog barks")

dog = Dog()
dog.sound()
dog.bark()
```

Output

```
Animal makes sound
Dog barks
```

---

## B) Multilevel Inheritance

A class inherits from another child class.

```
Person
   │
Employee
   │
Manager
```

Example

```python
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display(self):
        print(self.name, self.age)

class Employee(Person):
    def __init__(self, name, age, salary):
        super().__init__(name, age)
        self.salary = salary

    def display(self):
        super().display()
        print(self.salary)

class Manager(Employee):
    def __init__(self, name, age, salary, department):
        super().__init__(name, age, salary)
        self.department = department

    def display(self):
        super().display()
        print(self.department)
```

Output

```
Charlie
40
80000
Sales
```

---

## C) Multiple Inheritance

One child class inherits from multiple parent classes.

```
Camera        MusicPlayer
      \        /
       Smartphone
```

Example

```python
class Camera:
    def take_photo(self):
        print("Photo Taken!")

class MusicPlayer:
    def play_music(self):
        print("Playing Music")

class Smartphone(Camera, MusicPlayer):
    pass

phone = Smartphone()
phone.take_photo()
phone.play_music()
```

Output

```
Photo Taken!
Playing Music
```

---

## D) Hierarchical Inheritance

Multiple child classes inherit from one parent class.

```
Employee
├── Developer
├── Designer
└── Tester
```

Example

```python
class Employee:
    def __init__(self, name):
        self.name = name

class Developer(Employee):
    pass

class Designer(Employee):
    pass

class Tester(Employee):
    pass
```

---

# 3. super() Function

Used to call the constructor or methods of the parent class.

Example

```python
class Parent:
    def __init__(self):
        print("Parent Constructor")

class Child(Parent):
    def __init__(self):
        super().__init__()
        print("Child Constructor")

c = Child()
```

Output

```
Parent Constructor
Child Constructor
```

---

# 4. Method Overriding

A child class provides its own implementation of a parent class method.

Example

```python
class Animal:
    def sound(self):
        print("Animal Sound")

class Dog(Animal):
    def sound(self):
        print("Dog Barks")

dog = Dog()
dog.sound() 
```

Output

```
Dog Barks
```

---

# 5. Real-Life Example

University Management System

```
            Person
           /      \
      Student    Teacher
```

Person
- Name
- Age

Student
- Branch
- CGPA

Teacher
- Subject
- Salary

---

# 6. Another Real-Life Example

Employee Management System

```
Employee
├── Developer
├── Designer
└── Tester
```

Developer
- Programming Language

Designer
- Design Tool

Tester
- Testing Framework

---

# 7. Important OOP Keywords

## self

Represents the current object.

Example

```python
self.name = name
```

---

## super()

Calls the parent class constructor or methods.

Example

```python
super().__init__(name, age)
```

---

## __init__()

Constructor used to initialize object attributes.

Example

```python
def __init__(self, name):
    self.name = name
```

---

## pass

Used as a placeholder when no code is required.

Example

```python
class Student:
    pass
```

---

# 8. Common Errors

### NameError

```python
NameError: Smartphone is not defined
```

Reason:
Object created before class definition was completed.

Solution:
Create the object after the class definition.

---

### No such file or directory

Reason:
Running the file from the wrong folder.

Solution

```powershell
cd Day13
python filename.py
```

---

# 9. Advantages of Inheritance

- Reuse existing code
- Reduce duplicate code
- Easy maintenance
- Better organization
- Supports code extension
- Makes programs scalable

---

# Interview Questions

### What is inheritance?

Inheritance is an OOP concept where one class acquires the properties and methods of another class.

---

### Why do we use super()?

To access the parent class constructor and methods.

---

### What are the four main types of inheritance in Python?

- Single Inheritance
- Multilevel Inheritance
- Multiple Inheritance
- Hierarchical Inheritance

---

### Difference between Method Overloading and Method Overriding?

Method Overloading
- Same method name with different parameters.
- Python does not support true method overloading.

Method Overriding
- Child class redefines a parent class method.
- Fully supported in Python.

---

# Summary

✅ Inheritance

✅ Single Inheritance

✅ Multilevel Inheritance

✅ Multiple Inheritance

✅ Hierarchical Inheritance

✅ super()

✅ Method Overriding

✅ Real-world OOP Projects

✅ University Management System

✅ Employee Management System

---

# Practice Programs Completed

1. Person → Employee → Manager
2. Camera + MusicPlayer → Smartphone
3. Employee → Developer, Designer, Tester
4. University Management System

---

**Day 13 Status:** ✅ Completed