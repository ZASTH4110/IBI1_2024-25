# triangle.py
# Program to calculate and display the first ten triangular numbers

# Pseudocode:
# 1. Initialize a variable x to store the sum (triangular number).
# 2. Use a loop from 1 to 10 to calculate triangular numbers.
# 3. In each cycle, add the current number to x.
# 4. Print the current value of x after each addition.


x = 0

print("The first ten triangular numbers are:")

# Loop through numbers from 1 to 10
for i in range(1, 11):
    x += i  # Add current number to x
    print("n=" ,i,"  Tn =",x)  # Display the current triangular number
    