# Take inputs from user of their salary,age,credit score
salary=float(input("Enter your salary: "))
age=int(input("Enter your age: "))
cscore=int(input("Enter your credit score: "))

if age < 21: #check if user's age is bellow 21
    print("Loan Rejected: Age must be 21 or older.") 
elif age > 65:#check if user's age is greater than 65
    print("Loan Rejected: Age must be 65 or younger.")
elif salary < 25000:# check if user's salary is less than 25000
    print("Loan Rejected: Salary must be at least 25,000.")
elif cscore < 650:# check if the user's credit score is less than 650
    print("Loan Rejected: Credit score must be 650 or higher.")
else: #if non of the above conditions is true then the loan gets approved
    print("Loan Approved!")
