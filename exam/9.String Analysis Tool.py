# Asks the user to input a string
string = input("Enter a string: ")

# Define a string containing all vowels (both uppercase and lowercase)
vowels = "aeiouAEIOU"

# Initialize counters for vowels, consonants, digits, and special characters
vcnt = 0  # Counter for vowels
ccnt = 0  # Counter for consonants
dcnt = 0  # Counter for digits
scnt = 0  # Counter for special characters

# Iterate through each character in the input string
for char in string:
    if char.isalpha():  # Check if the character is an alphabet
        if char in vowels:  # Check if the letter is a vowel
            vcnt += 1  # Increment the vowel counter
        else:
            ccnt += 1  # Increment the consonant counter
    elif char.isdigit():  # Check if the character is a digit
        dcnt += 1  # Increment the digit counter
    else:  # If it's neither a letter nor a digit, it must be a special character
        scnt += 1  # Increment the special character counter

# Reverse the input string
reversed_str = string[::-1]

# Display the analysis results
print(f"\nString Analysis:")  # Print a header for the results
print(f"Vowels: {vcnt}")  # Print the count of vowels
print(f"Consonants: {ccnt}")  # Print the count of consonants
print(f"Digits: {dcnt}")  # Print the count of digits
print(f"Special Characters: {scnt}")  # Print the count of special characters
print(f"Reversed String: {reversed_str}")  # Print the reversed version of the input string
