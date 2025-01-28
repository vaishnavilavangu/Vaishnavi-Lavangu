# Function to check the current balance
def check_balance(balance):
    print(f"Your current balance is: {balance}")

# Function to deposit money
def deposit(balance):
    amount = float(input("Enter the amount to deposit: "))  # Prompt user to enter deposit amount
    balance += amount  # Add deposit amount to balance
    print(f"Successfully deposited {amount}. Your new balance is: ${balance}")
    return balance  # Return updated balance

# Function to withdraw money
def withdraw(balance):
    amount = float(input("Enter the amount to withdraw: "))  # Prompt user to enter withdrawal amount
    if amount > balance:  # Check if there's sufficient balance
        print("Insufficient balance! Try again with a lesser amount.")
    else:
        balance -= amount  # Deduct withdrawal amount from balance
        print(f"Successfully withdrew ${amount}. Your new balance is: ${balance}")
    return balance  # Return updated balance

# Main function to simulate ATM operations
def atm_simulation():
    balance = 1000  # Initialize the account balance (can be changed as needed)
    
    while True:  # Infinite loop to continue ATM operations
        # Display available options to the user
        print("\nATM Menu:")
        print("1. Check Balance")
        print("2. Deposit Money")
        print("3. Withdraw Money")
        print("4. Exit")
        
        choice = input("Choose an option (1-4): ")  # Prompt user for choice
        
        if choice == '1':  # If the user chooses to check balance
            check_balance(balance)  # Call the check_balance function
        elif choice == '2':  # If the user chooses to deposit money
            balance = deposit(balance)  # Call the deposit function and update balance
        elif choice == '3':  # If the user chooses to withdraw money
            balance = withdraw(balance)  # Call the withdraw function and update balance
        elif choice == '4':  # If the user chooses to exit
            print("Thank you for using the ATM! Goodbye.")  # Exit message
            break  # Exit the loop and end the program
        else:
            print("Invalid choice! Please select a valid option.")  # Handle invalid option

# Run the ATM simulation
atm_simulation()
