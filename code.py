# Basic Python Code Example

# Ask for user input
name = input("Enter your name: ")
age = int(input("Enter your age: "))

# Display greeting
print(f"Hello, {name}!")

# Conditional logic
if age >= 18:
    print("You are an adult.")
else:
    print("You are a minor.")

# Loop to count from 1 to 5
print("Counting from 1 to 5:")
for i in range(1, 6):
    print(i)

# Simple function
def greet_user(username):
    return f"Welcome, {username}!"

# Call function
message = greet_user(name)
print(message)
