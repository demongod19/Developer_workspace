employee = {
    "id": 101,
    "name": "Pratik",
    "salary": 50000,
    "department": "Cybersecurity"
}
while True:
    print("1. Display Employee Details")
    print("2. Update Employee Salary")
    print("3. Change Employee Department")
    print("4. Exit")
    choice = input("Enter your choice: ")
    
    if choice == '1':
        print(f"Employee ID: {employee['id']}")
        print(f"Employee Name: {employee['name']}")
        print(f"Employee Salary: {employee['salary']}")
        print(f"Employee Department: {employee['department']}")
    elif choice == '2':
        new_salary = float(input("Enter new salary: "))
        employee['salary'] = new_salary
        print("Salary updated successfully.")
    elif choice == '3':
        new_department = input("Enter new department: ")
        employee['department'] = new_department
        print("Department updated successfully.")
    elif choice == '4': 
        print("Exiting the program.")
        break
    else:
        print("Invalid choice. Please try again.")