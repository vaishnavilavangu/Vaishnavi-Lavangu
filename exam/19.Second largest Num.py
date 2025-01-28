# Asks the user to input a list of numbers, separated by spaces
numbers = list(map(int, input("Enter a list of numbers separated by spaces: ").split()))

# Check if the list has at least two unique numbers
if len(numbers) < 2:
    print("At least two numbers are required to find the second largest.")
else:
    unique_numbers = list(set(numbers)) # Remove duplicates by converting the list to a set
    # Check if there are at least two unique numbers after removing duplicates
    if len(unique_numbers) < 2:
        print("All numbers are the same. No second largest exists.")
    else:
        # Sort the unique numbers in descending order
        unique_numbers.sort(reverse=True)
        
        # The second largest number is at index 1
        sl = unique_numbers[1]
        
        # Display the second largest number
        print(f"The second largest number is: {sl}")
