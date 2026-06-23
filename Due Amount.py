# Program to calculate due amount after bill payment

# Taking inputs from the user
total_bill = float(input("Enter the total bill amount: "))
amount_paid = float(input("Enter the amount paid: "))

# Calculating due amount
due_amount = total_bill - amount_paid

# Displaying the result
if due_amount > 0:
    print(f"The customer still owes: {due_amount}")
elif due_amount == 0:
    print("The bill is fully paid. No due amount.")
else:
    print(f"Extra payment received: {-due_amount}")
