import math

# Program to calculate sin, cos, and tan

# Taking angle input from the user (in degrees)
angle_deg = float(input("Enter the angle in degrees: "))

# Convert degrees to radians (since math functions use radians)
angle_rad = math.radians(angle_deg)

# Calculate values
sin_val = math.sin(angle_rad)
cos_val = math.cos(angle_rad)

# Handle tan separately to avoid division by zero
try:
    tan_val = math.tan(angle_rad)
except:
    tan_val = "Undefined (cos = 0)"

# Display results
print(f"sin({angle_deg}) = {sin_val:.4f}")
print(f"cos({angle_deg}) = {cos_val:.4f}")
print(f"tan({angle_deg}) = {tan_val}")
