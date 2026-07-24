# Day 14 - Polymorphism & Abstraction in Python

## Topics Covered

- Polymorphism
- Method Overriding
- Duck Typing
- Abstraction
- Abstract Classes
- Abstract Methods
- `ABC`
- `@abstractmethod`

---

# 1. Polymorphism

Polymorphism means **"many forms."**

It allows the same method name to behave differently depending on the object using it.

## Example

```python
class Dog:
    def sound(self):
        print("Dog barks")


class Cat:
    def sound(self):
        print("Cat meows")


dog = Dog()
cat = Cat()

dog.sound()
cat.sound()
```

Output:

```text
Dog barks
Cat meows
```

Both classes have the same method:

```python
sound()
```

But the behavior is different.

---

# 2. Polymorphism with Shapes

We practiced polymorphism using:

- Circle
- Rectangle
- Triangle

Each class had the same `draw()` method.

```python
class Circle:
    def draw(self):
        print("Drawing a Circle")


class Rectangle:
    def draw(self):
        print("Drawing a Rectangle")


class Triangle:
    def draw(self):
        print("Drawing a Triangle")
```

Create objects:

```python
circle = Circle()
rectangle = Rectangle()
triangle = Triangle()

circle.draw()
rectangle.draw()
triangle.draw()
```

Output:

```text
Drawing a Circle
Drawing a Rectangle
Drawing a Triangle
```

---

# 3. Polymorphism Using a Loop

Instead of calling each object separately:

```python
shapes = [
    Circle(),
    Rectangle(),
    Triangle()
]

for shape in shapes:
    shape.draw()
```

The same line:

```python
shape.draw()
```

produces different behavior depending on the object.

This is an important example of polymorphism.

---

# 4. Method Overriding

Method overriding happens when a child class provides its own implementation of a method that already exists in the parent class.

Example:

```python
class Animal:
    def sound(self):
        print("Animal makes a sound")


class Dog(Animal):
    def sound(self):
        print("Dog barks")


dog = Dog()

dog.sound()
```

Output:

```text
Dog barks
```

The child class `Dog` overrides the `sound()` method of `Animal`.

---

# 5. Why Method Overriding?

Method overriding allows child classes to have their own behavior while still using inheritance.

Example:

```text
Animal
   |
   +-- Dog   → bark
   |
   +-- Cat   → meow
   |
   +-- Cow   → moo
```

All animals can have a `sound()` method, but each animal produces a different sound.

---

# 6. Duck Typing

Duck typing is an important concept in Python.

Python mainly cares about whether an object supports the required operation or method rather than requiring a particular class type.

Example:

```python
class Duck:
    def speak(self):
        print("Quack")


class Human:
    def speak(self):
        print("Hello")


def make_speak(obj):
    obj.speak()


duck = Duck()
human = Human()

make_speak(duck)
make_speak(human)
```

Output:

```text
Quack
Hello
```

Both objects work because both contain:

```python
speak()
```

---

# 7. Duck Typing Example

Another example:

```python
class Bird:
    def fly(self):
        print("Bird is flying")


class Airplane:
    def fly(self):
        print("Airplane is flying")


def start_flying(obj):
    obj.fly()


bird = Bird()
plane = Airplane()

start_flying(bird)
start_flying(plane)
```

Output:

```text
Bird is flying
Airplane is flying
```

---

# 8. Abstraction

Abstraction means hiding unnecessary implementation details and exposing only the essential functionality.

For example:

When we drive a car, we use:

```text
Start
Accelerator
Brake
Steering
```

We don't need to understand every internal engine operation to drive it.

That is similar to abstraction.

---

# 9. Abstract Class

An abstract class is a class designed mainly to act as a blueprint for other classes.

Python provides abstract classes using:

```python
ABC
```

from the `abc` module.

Import:

```python
from abc import ABC, abstractmethod
```

---

# 10. Abstract Method

An abstract method defines a method that subclasses are required to implement before they can be instantiated.

Example:

```python
from abc import ABC, abstractmethod


class Vehicle(ABC):

    @abstractmethod
    def start(self):
        pass
```

`Vehicle` tells its child classes:

> You must provide a `start()` implementation.

---

# 11. Implementing an Abstract Class

```python
from abc import ABC, abstractmethod


class Vehicle(ABC):

    @abstractmethod
    def start(self):
        pass


class Car(Vehicle):

    def start(self):
        print("Car Started")


class Bike(Vehicle):

    def start(self):
        print("Bike Started")
```

Create objects:

```python
car = Car()
bike = Bike()

car.start()
bike.start()
```

Output:

```text
Car Started
Bike Started
```

---

# 12. Can We Create an Abstract Class Object?

Normally, an abstract class with unimplemented abstract methods cannot be instantiated.

Wrong:

```python
vehicle = Vehicle()
```

This produces a `TypeError` because `start()` is abstract.

Correct:

```python
car = Car()
```

The child class implements the required method.

---

# 13. Polymorphism + Abstraction

Abstraction and polymorphism can work together.

```python
from abc import ABC, abstractmethod


class Vehicle(ABC):

    @abstractmethod
    def start(self):
        pass


class Car(Vehicle):

    def start(self):
        print("Car Started")


class Bike(Vehicle):

    def start(self):
        print("Bike Started")


class Bus(Vehicle):

    def start(self):
        print("Bus Started")
```

Now:

```python
vehicles = [
    Car(),
    Bike(),
    Bus()
]

for vehicle in vehicles:
    vehicle.start()
```

Output:

```text
Car Started
Bike Started
Bus Started
```

Same:

```python
vehicle.start()
```

Different behavior = **Polymorphism**

---

# 14. Polymorphism vs Method Overriding

## Polymorphism

Same interface/method name can produce different behavior for different objects.

Example:

```python
shape.draw()
```

Could draw:

```text
Circle
Rectangle
Triangle
```

## Method Overriding

A child class replaces an inherited method with its own implementation.

Example:

```text
Animal.sound()
        ↓
Dog.sound()
```

---

# 15. Abstraction vs Encapsulation

These concepts should not be confused.

## Abstraction

Focuses on:

> What should the object do?

It hides unnecessary implementation details.

## Encapsulation

Focuses on:

> How should access to an object's data be controlled?

We will study encapsulation in more detail later.

---

# Practice Programs

## Practice 1 - Method Overriding

```text
Animal
   |
  Dog
```

Method:

```python
sound()
```

---

## Practice 2 - Polymorphism

Classes:

```text
Circle
Rectangle
Triangle
```

Common method:

```python
draw()
```

---

## Practice 3 - Duck Typing

Classes:

```text
Bird
Airplane
```

Common method:

```python
fly()
```

---

## Practice 4 - Abstraction

Abstract class:

```text
Vehicle
```

Child classes:

```text
Car
Bike
Bus
```

Required method:

```python
start()
```

---

# Mini Project - Banking System

Abstract Parent:

```text
Account
```

Child Classes:

```text
Account
   |
   +-- SavingsAccount
   |
   +-- CurrentAccount
```

Important methods:

```python
deposit()
withdraw()
show_balance()
```

Concepts used:

- Classes
- Objects
- Inheritance
- Abstraction
- Polymorphism
- Method Overriding

---

# Interview Questions

## Q1. What is Polymorphism?

Polymorphism means one interface or method name can have different behaviors depending on the object.

---

## Q2. What does Polymorphism mean?

It means:

```text
Many Forms
```

---

## Q3. Give an example of Polymorphism.

```python
circle.draw()
rectangle.draw()
triangle.draw()
```

The method is `draw()`, but each object performs a different action.

---

## Q4. What is Method Overriding?

Method overriding occurs when a child class provides its own implementation of a method inherited from its parent.

---

## Q5. What is Duck Typing?

Duck typing means Python focuses on whether an object supports the required operation or method rather than requiring a specific class type.

---

## Q6. What is Abstraction?

Abstraction hides unnecessary implementation details and exposes essential functionality.

---

## Q7. What is an Abstract Class?

An abstract class is a class designed to provide a common blueprint or interface for subclasses.

---

## Q8. What is an Abstract Method?

An abstract method is a method declared with:

```python
@abstractmethod
```

Subclasses must implement it before they can be instantiated.

---

## Q9. Which module is used for abstraction in Python?

```python
abc
```

Example:

```python
from abc import ABC, abstractmethod
```

---

## Q10. Can we create an object of an abstract class?

Not if it still contains unimplemented abstract methods.

---

# Important Syntax

## Abstract Class

```python
from abc import ABC, abstractmethod


class Parent(ABC):

    @abstractmethod
    def method(self):
        pass
```

---

## Child Implementation

```python
class Child(Parent):

    def method(self):
        print("Implemented")
```

---

# What I Learned Today

Today I learned about Polymorphism and Abstraction in Python.

I understood how the same method name can behave differently for different objects.

I also learned Method Overriding, where a child class provides its own implementation of a parent method.

I learned about Duck Typing and how Python can work with different objects as long as they provide the required method.

Finally, I learned about Abstract Classes and Abstract Methods using the `abc` module.

---

# One New Thing I Discovered

The same line of code:

```python
obj.method()
```

can perform completely different operations depending on which object `obj` refers to.

This makes programs flexible and reusable.

---

# Commands Used Today

```bash
python practice1.py
python practice2.py
python practice3.py
python practice4.py

git add .
git commit -m "Day 14: Learned Polymorphism and Abstraction"
git push
```

---

# Day 14 Progress

- [x] Polymorphism
- [x] Method Overriding
- [x] Duck Typing
- [x] Abstraction
- [x] Abstract Classes
- [x] Abstract Methods
- [x] `ABC`
- [x] `@abstractmethod`
- [x] Polymorphism Practice

---

# OOP Progress So Far

```text
Day 11 → Classes & Objects        ✅
Day 12 → Inheritance              ✅
Day 13 → Types of Inheritance     ✅
Day 14 → Polymorphism/Abstraction ✅
Next   → Encapsulation
```

**Day 14 Status: ✅ Completed**