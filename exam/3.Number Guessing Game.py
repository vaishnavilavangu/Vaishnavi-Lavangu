import random  # Importing the random module to generate a random number

# Generate a random number between 1 and 100
number = random.randint(1, 100)

# Variable to keep track of the number of attempts
attempts = 0

# Display a message
print("I have chosen a number between 1 and 100. Can you guess it?")

# Start an infinite loop to allow the user to keep guessing
while True:
    try:
        #Ask the user to input their guess
        user = int(input("Enter your guess: "))

        # Increment the attempts counter
        attempts += 1

        # Check if the guessed number is too low
        if user < number:
            print("Too Low! Guess again.")
        # Check if the guessed number is too high
        elif user > number:
            print("Too High! Guess again.")
        # If the guessed number matches the random number
        else:
            print(f"Congratulations! You guessed it in {attempts} attempts.")
            break  # Exit the loop since the user guessed correctly
    except ValueError:
        # Handle invalid input that cannot be converted to an integer
        print("Invalid input! Please enter a number in range.")
