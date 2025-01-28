# Function to check if a number is prime
def is_prime(num):
    # If the number is less than or equal to 1, it's not prime
    if num <= 1:
        return False
    # Check divisors from 2 to the square root of the number inclusively
    for i in range(2, int(num**0.5) + 1):
        # If the number is divisible by any i, it's not prime
        if num % i == 0:
            return False
    # If no divisors are found, the number is prime
    return True

# Take the start of the range as input from the user
num1 = int(input("Enter start of the range: "))

# Take the end of the range as input from the user
num2 = int(input("Enter end of the range: "))

# Print the list of prime numbers
print(f"Prime numbers between {num1} and {num2}:")

# Loop through all numbers in the range [num1, num2]
for num in range(num1, num2 + 1):
    # Check if the current number is prime
    if is_prime(num):
        # Print the prime number, separated by a space
        print(num, end=" ")
