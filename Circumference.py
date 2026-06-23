import math

# Function to calculate circumference
def circumference(radius):
    return 2 * math.pi * radius

# Taking input from the user
r = float(input("Enter the radius of the circle: "))

# Calling the function
c = circumference(r)

# Displaying the result
print(f"The circumference of the circle with radius {r} is: {c}")
