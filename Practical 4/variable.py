# Storing the commute times for the bus-based option
a = 15  # Walking time to the bus stop (minutes)
b = 75  # Bus journey time (1 hr 15 mins = 75 mins)
c = a + b  # Total time for bus-based commute

# Storing the commute times for the car-based option
d = 90  # Driving time to the car park (1 hr 30 mins = 90 mins)
e = 5   # Walking time from the car park (minutes)
f = d + e  # Total time for car-based commute

# Comparing the two commute methods
# The bus-based commute takes c minutes, while the car-based commute takes f minutes
# Checking which is quicker
if c < f:
    quicker_method = "Bus"
else:
    quicker_method = "Car"
print("The quicker method is:", quicker_method)

# The quicker method is the bus-based commute if c < f, otherwise the car-based commute
# In this case: c = 90 mins, f = 95 mins, so the bus is quicker.

# Boolean variable setup
X = True
Y = False

# Encoding 'both X and Y' as a Boolean variable
W = X and Y

# Truth table for W:
# X    | Y    | W = X and Y
# -------------------------
# True | True  | True
# True | False | False
# False | True  | False
# False | False | False

# The truth table confirms that W correctly represents the AND operation
