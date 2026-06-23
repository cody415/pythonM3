import os

# Define shutdown function
def shutdown():
    choice = input("Do you really want to shutdown your computer? (yes/no): ").lower()
    if choice == "yes":
        print("Shutting down...")
        # Uncomment the line below to actually shutdown (Windows)
        # os.system("shutdown /s /t 1")
        # For Linux/Mac, use:
        # os.system("shutdown now")
    else:
        print("Shutdown cancelled.")

# Call the function
shutdown()
