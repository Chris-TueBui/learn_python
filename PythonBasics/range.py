print(range(100))

# exclude the last number
# if you dont need a variable in python, then use: _
for number in range (0, 10):
    print(number)

for _ in range(0, 10):
    print("here")

for _ in range(0, 10, 2):
    print(_) #-> the last one is how to jump

# -1 is do something in reverse. But then have to change the value in range(), the above goes from 0 to 10. 
# if want to use -1, then it has to be range(10, 0, -1):
for _ in range(0, 10, -1):
    print(_)

for _ in range(2):
    print(list(range(10))) # a quick way to create a list