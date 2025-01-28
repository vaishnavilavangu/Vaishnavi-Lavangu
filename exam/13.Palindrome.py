def is_palindrome(val): #A function that checks the given number or string is palindrome or not
    return str(val) == str(val)[::-1] # Convert the value to a string and compare it with its reverse
while True:
    #teakes the user input continuesly until the input is '0' 
    user = input("Enter a string or number to check if it's a palindrome or type '0' to quit: ")
    # Check if the user input is '0' (case-insensitive), which indicates they want to quit
    if user.lower() == '0':
        break #exit the loop
    if is_palindrome(user):#calls the function palindrome
        print(f"{user} is a palindrome.") #prints the numbers is a palindrome, if the function returns true 
    else:
        print(f"{user} is not a palindrome.")#prints the numbers is not a palindrome, if the function returns false
