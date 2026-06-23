# Program to validate age and check even/odd

def check_age():
    try:
        age = int(input("Enter your age: "))

        # Check if age is valid
        if age < 0 or age > 150:
            print("Error: Invalid age entered. Please enter a realistic age.")
        else:
            print(f"Age entered is: {age}")

            # Check if age is even or odd
            if age % 2 == 0:
                print("The age is EVEN.")
            else:
                print("The age is ODD.")

    except ValueError:
        print("Error: Please enter a valid integer for age.")

# Call the function
check_age()
