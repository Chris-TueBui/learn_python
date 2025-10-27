for char in enumerate('Helloooooo'):
    #gives you an index and the value at that index
    print(char)

for i, char in enumerate('HELLLLLOOOOO'):
    print(i, char)

for i, value in enumerate((1, 2, 3)):
    print(i, value)

#create a script to enumerate a list of number 1 to 10
#and I want to be told the index of the number 50 is
for i, value in enumerate(list(range(0, 100))):
    if (value == 50):
        print(i, value)

