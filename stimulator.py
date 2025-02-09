def atm_simulator():
    balance = 1000  # Starting balance
    print("Welcome to the ATM Simulator!")
    
    while True:
        print("\nOptions:")
        print("1. Check Balance")
        print("2. Deposit Money")
        print("3. Withdraw Money")
        print("4. Exit")
        
        choice = input("Enter choice: ")

        if choice == '1':
            print(f"Your balance is: ${balance}")
        elif choice == '2':
            amount = float(input("Enter amount to deposit: $"))
            if amount > 0:
                balance += amount
                print(f"${amount} deposited. New balance: ${balance}")
            else:
                print("Invalid amount. Please try again.")
        elif choice == '3':
            amount = float(input("Enter amount to withdraw: $"))
            if 0 < amount <= balance:
                balance -= amount
                print(f"${amount} withdrawn. New balance: ${balance}")
            else:
                print("Invalid amount or insufficient funds. Please try again.")
        elif choice == '4':
            print("Thank you for using the ATM. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

atm_simulator()
