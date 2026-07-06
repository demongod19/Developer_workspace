balance = 50000 
while True:
    print("***********Welcome to ATM************")
    print("1. Check Balance")
    print("2. Withdraw Money")
    print("3. Deposit Money")
    print("4. Exit")
    print("*************************************")
    
    choice = int(input("Enter your choice: "))
    
    if choice == 1:
        print(f"Your balance is: {balance}")
    elif choice == 2:
        amount = int(input("Enter amount to withdraw: "))
        if amount > balance:
            print("Insufficient balance")
        else:
            balance -= amount
            print(f"You have withdrawn {amount}. Your new balance is: {balance}")
    elif choice == 3:
        amount = int(input("Enter amount to deposit: "))
        balance += amount
        print(f"You have deposited {amount}. Your new balance is: {balance}")
    elif choice == 4:
        print("Thank you for using the ATM. Goodbye!")
        break
    else:
        print("Invalid choice. Please try again.")