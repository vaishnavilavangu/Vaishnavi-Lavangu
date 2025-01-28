
numbers = input("Enter a list of numbers separated by space: ").split()#takes the input as numbers and splits them
#Declare 2 empty Lists 
onums = []
enums= []
for i in numbers:
    if int(i) % 2 == 0:#checks if the number is even
        enums.append(i)#appends the number into evennumbers list
    else:#if condition fails pushes it into oddnumbers list
        onums.append(i)
print("Odd numbers:", onums)#prints the oddnumbers list
print("Even numbers:", enums)#prints the evennumbers list
