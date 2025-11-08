# := 
# Assigns values to variables as part of a larger expression.
a = 'helloooooooo'
if (len(a) > 10):
    print(f"too long {len(a)} elements")

#Avoid repeating
#In the example above, we calculate the len twice.
# Assigns variable n to whatever the len of a 
if (n := len(a)) > 10:
    print(f"too long {n} elements")

while ((n := len(a)) > 1):
    print(n)
    a = a[:-1]