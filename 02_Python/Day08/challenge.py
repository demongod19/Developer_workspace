numbers = []
numbers.append(int(input("Enter a number: ")))
numbers.append(int(input("Enter another number: ")))
if numbers[0] > numbers[1]:
    print(f"The first number {numbers[0]} is greater than the second number {numbers[1]}.")
else:
    print(f"The second number {numbers[1]} is greater than the first number {numbers[0]}.")