# 1. Define a function to calculate the nth triangular number.
# 2. Use a loop to calculate and print the first ten triangular numbers.
# 3. Ensure that the output matches the expected values.

# Function to calculate the nth triangular number
def triangular_number(n):
    # A triangular number is the sum of numbers from 1 to n
    return n * (n + 1) // 2  # Using the formula T(n) = n * (n + 1) / 2

# Print the first ten triangular numbers
print("The first ten triangular numbers are:")
for i in range(1, 11):  # Loop from 1 to 10
    print("n=" ,i," Tn = ", triangular_number(i))
    #Display the calculated triangular number