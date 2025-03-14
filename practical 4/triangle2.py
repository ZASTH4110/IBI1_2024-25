# 1. Initialize a variable x to store the result.(ensure x = 0)
# 2. Write a formula that  expresses the general term formula for Tn（Tn = n * (n + 1) / 2）
# 3. In each cycle, add the current number to x.（x += i）
# 4. Print the current value of x after each addition.（x = Tn)(n=i)

# Function to calculate the nth triangular number
def triangular_number(n):
    # A triangular number is the sum of numbers from 1 to n
    return n * (n + 1) // 2  # Using the formula T(n) = n * (n + 1) / 2

# Print the first ten triangular numbers
print("The first ten triangular numbers are:")
for i in range(1, 11):  # Loop from 1 to 10
    print("n=" ,i," Tn = ", triangular_number(i))
    #Display the calculated triangular number