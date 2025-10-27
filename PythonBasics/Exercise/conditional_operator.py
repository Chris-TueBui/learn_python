isMagician = False
isExpert = True

#check if magician and expert: "You are a master magician"
#check if magician but not expert: "at least you are getting there"
#check if you are not a magician: "You need magic powers"

if isMagician and isExpert:
    print("You are a master magician")
elif isMagician and not isExpert:
    print("At least you are getting there")
elif not isMagician:
    print("You need magic powers")

print(True == 1) # --> true. Convert to truthy
print('' == 1) # --> False. Empty string is falsethy
print([] == 1) # --> False. Empty array is falsethy
print(10 == 10.0) # --> True. Convert to int or float
print([] == []) # --> True
print('1' == 1) # --> bad code. 2 different types.

print(True is 1) # --> False
print('' is 1) # --> False
print([] is 1) # --> False
print(10 is 10.0) # --> False
print([] is []) # --> False
print('1' is 1) # --> False

a = [1, 2, 3]
b = [1, 2, 3]
print(a is b) # --> False. Because for data structure, when it gets created, python stores in different location in memory
print(a == b) # --> False.

# ==: checks for equality. Check if the value equals. Convert to the same type
# is: checks the location in the memory if the 2 values are the same.