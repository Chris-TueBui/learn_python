isOld = True
isLicense = True

# syntax: if condtion: 
#condition is a boolean expression. If it evaluates to True, the code block will be executed.
# If it evaluates to False, the code block will not be executed.
# indentation is important in Python. It indicates a block of code.
if isOld and isLicense: 
    print("You are old enough to drive")
elif isLicense:
    print("You can drive now")
else:
    print("You are not old enough to drive")

# Truthy and Falsy:
# bool(): by default is False
# In the above example, if isOld = 5, then under hood, python does bool(5) which is True.
# If isOld = 0, then under hood, python does bool(0) which is False.
# In the above example, if isOld = "", then under hood, python does bool("") which is False.
password = 123
username = "Johnny"

if password and username:
    print("You are logged in")
else:
    print("You are not logged in")

#Ternary operator
# syntax: condition_if_true if condition else condition_if_else

isFriend = True
canMessage = "message allowed" if isFriend else "not allowed to message"
print(canMessage)

#Short circuiting
is_friend = True
is_user = True
if is_friend and is_user:
    print("best friend")

if is_friend or is_user:
    print("best friend or user")

#Logical operators
# and: both conditions must be True
# or: at least one condition must be True
# >, <, >=, <=, ==, !=: comparison operators
# not: negates the boolean value
print(ord("a")) # ord() returns the Unicode code point of a character.
print(ord("A"))
#not keyword: negates the boolean value
# not is also a function. But we can write "not True" or "not False" to negate the boolean value.
