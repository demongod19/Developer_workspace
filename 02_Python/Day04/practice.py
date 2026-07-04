age = int(input("Enter your age: "))
if age < 5:
    print("Free ticket!")
elif age>= 5 and age <=12:
    print("Child ticket: ₹100")
elif age >= 13 and age <= 59:
    print("Adult ticket: ₹200")
else:
    print("Senior citizen ticket: ₹120")