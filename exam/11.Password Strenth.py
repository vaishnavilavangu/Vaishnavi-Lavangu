# Asks the user to enter a password
password = input("Enter a password: ")

# Initialize flags for different criteria
has_upper = False  # To check if the password contains at least one uppercase letter
has_lower = False  # To check if the password contains at least one lowercase letter
has_digit = False  # To check if the password contains at least one digit
has_special = False  # To check if the password contains at least one special character

# Iterate through each character in the password
for char in password:
    if char.isupper():  # Check if the character is an uppercase letter
        has_upper = True
    elif char.islower():  # Check if the character is a lowercase letter
        has_lower = True
    elif char.isdigit():  # Check if the character is a digit
        has_digit = True
    elif not char.isalnum():  # Check if the character is a special character
        has_special = True

# Check all conditions for a strong password
if len(password) >= 8 and has_upper and has_lower and has_digit and has_special:
    print("Password strength: Strong")  # If all conditions are met, the password is strong
else:
    print("Password strength: Weak")  # Otherwise, the password is weak
