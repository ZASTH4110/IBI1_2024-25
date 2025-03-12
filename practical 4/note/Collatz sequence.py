x = input("x(i) = ") 
i = float(x)
if i%1 == 0:
    if i%2 == 0:
        i = i/2
    elif i%2 == 1:
        i = 3*i + 1
    print ("x(i+1) =",i)
else:
    print("x is not an integer")
