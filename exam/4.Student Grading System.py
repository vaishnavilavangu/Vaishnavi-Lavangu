#Function to calculate student grade
def calculate_grade(percentage):
    if percentage >= 90:#checks if percentage is greater than or equal to 90
        return "A"
    elif percentage >= 75:#checks if percentage is greater than or equal to 75
        return "B"
    elif percentage >= 50:#checks if percentage is greater than or equal to 50
        return "C"
    elif percentage >=35:#checks if percentage is greater than or equal to 35
        return "D"
    else:
        return "Fail" 

# Main program
#Take name as input from the user
name = input("Enter the student's name: ")
marks = [] #Declare an empty list
#Takes 5 subject marks as input from the user
for i in range(1, 6):
    mark = float(input(f"Enter marks for subject {i} out of 100: "))
    marks.append(mark) #appends the marks entered in the marks list
total = sum(marks) #calculates the sum of all subjects
percentage = (total/ 500) * 100 #calulates the percentage
grade = calculate_grade(percentage)#calls the function calculate_grade

#Displays the Stusents grade
print("\n Student Grading system ")
print(f"Name: {name}")
print(f"Total Marks: {total}/500")
print(f"Percentage: {percentage:.2f}%")
print(f"Grade: {grade}")
