# What does this piece of code do?
# Answer:Roll two dice until they show the same number, count how many tries it takes and record it in the variable progress.

# Import libraries
# randint allows drawing a random number,
# e.g. randint(1,5) draws a number between 1 and 5
from random import randint


# ceil takes the ceiling of a number, i.e. the next higher integer.
# e.g. ceil(4.2)=5
from math import ceil

progress=0
while progress>=0:
# These two lines of code repeat indefinitely until the condition is met and the loop is exited.
	progress+=1
	# Add 1 to the progress counter， Record how many times the loop has been executed
	first_n = randint(1,6)
	second_n = randint(1,6)
	# Simulate the number of points on two dice
	# Draw a random number between 1 and 6 for the first and second dice
	if first_n == second_n:
		# If the numbers are the same, print the number of attempts and break the loop
		print(progress)
		break
