n=int(input("enter a number: "))#Take input as a number to print its multiplication table
r=int(input("enter the range: "))#Take input range to print its multiplication table till its range
#loop runs from 1 to specified range by the user
for i in range(1,r+1):
    print(f"{n} * {i} = {n*i}") #prints the table to the specified range
    
    
