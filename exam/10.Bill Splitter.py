# Ask the user to enter the total bill amount
total_bill = float(input("Enter the total bill amount: "))

# Ask the user to enter the number of people to split the bill
num_people = int(input("Enter the number of people: "))

# Ask the user to enter the tip percentage
tip_percentage = float(input("Enter the tip percentage: "))

# Calculate the total tip amount by multiplying the bill with the tip percentage divided by 100
tip_amount = (total_bill * tip_percentage) / 100

# Calculate the total amount including the tip
total_amount = total_bill + tip_amount

# Divide the total amount equally among the number of people
amount_per_person = total_amount / num_people

# Display the results
print(f"\nTotal bill amount (including tip): {total_amount:.2f}")
print(f"Each person needs to pay: {amount_per_person:.2f}")
