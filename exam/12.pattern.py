n = int(input("Enter the number of rows for the pattern: "))#Takes the user input to know number of rows
rev=input("Do you want to print the pattern in reverse (yes/no): ")#takes string as input from user to know their option
if rev == 'yes':#checks the condition if the user wants to print the pattern in reverse
    for i in range(n, 0, -1):#If reverse is selected, iterate from n to 1 (inclusive) in reverse order
        print('*' * i)# Print '*' i times to create the reverse pattern
else:
    # If reverse is not selected, iterate from 1 to n (inclusive)
    for i in range(1, n + 1):
        print('*' * i)# Print '*' i times to create the normal pattern
