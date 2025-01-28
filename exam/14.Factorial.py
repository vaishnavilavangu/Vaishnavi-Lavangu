num=int(input("Enter a number: "))#takes input from the user
if(num < 0):#checks the condition if the etered number is less than 0.
    print("Invalid number as it is an negative number")#if condition is true then prints Invalid number
else:
    fact=1#declare a variable that hold value 1
    for i in range(1,num+1): # runs loop from 1 to given number
        fact=fact*i #Multiply the current value of `fact` by the loop counter `i` to calculate the factorial
        i=i+1 #Increment the loop counter
    print(fact)#prints calculated factorial