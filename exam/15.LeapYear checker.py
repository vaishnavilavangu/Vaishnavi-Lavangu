def leap_year(y):#function that calculates the given year is leap year or not.
    # A year is a leap year if it is divisible by 4, but not by 100, unless it is divisible by 400
    if (y % 4 == 0 and y % 100 != 0) or (y % 400 == 0):
        return True#returns true if it is a leap year
    else:
        return False#returns false if it is not a leap year
while True:#Loop runs until the user enters years and exits when user enters 0
    y=int(input("Enter a year to check if it's a leap year or '0' to exit: "))
    if(y==0):
        break#comes out of the loop if user enters 0 as input
     # Call the leap_year function to check if the year is a leap year
    if leap_year(y):
        print(f"{y} is a leap year.")#print if the year is leap year 
    else:
        print(f"{y} is not a leap year.")#print if the year is not leap year 
