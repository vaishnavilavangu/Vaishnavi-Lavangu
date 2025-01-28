for i in range(1,101): #loop runs from 1 to 100
    if((i%3==0)and(i%5==0)): # to check the number divisible by both 3 and 5 
        print("FizzBuzz",end=" ") #prints Fizzbuzz if the condition satisfies
    elif(i%3==0):# to check the number divisible by  3 
        print("Fizz",end=" ")#prints Fizz if the condition satisfies
    elif(i%5==0):# to check the number divisible by 5 
        print("Buzz",end=" ")#prints buzz if the condition satisfies
    else:
        print(i,end=" ")#prints numbers other than mulitiple of both 3 and 5 