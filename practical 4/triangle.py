# 1. Initialize a variable x to store the result.(ensure x = 0)
# 2. Write a formula that describes the relationship between the previous triangle and the next triangle.（Tn = Tn-1 + n）
# 3. In each cycle, add the current number to x.（x += i）
# 4. Print the current value of x after each addition.（x = Tn)(n=i)
x = 0

print("The first ten triangular numbers are:")

# Loop through numbers from 1 to 10
for i in range(1, 11):
    x += i  # Add current number to x
    print("n=" ,i,"  Tn =",x)  # Display the current triangular number
    