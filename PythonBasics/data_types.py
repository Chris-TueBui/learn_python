# Fundamental data type:
#int, float, str bool, list, tuple, set, dict.

#Clases -> Custom types

#Specialize data types (special packages, modules, etc.)
#None

print(2+4)
print(2-4)
print(2*4)
print(2/4)
print(2%4)
print(2 ** 3) #2 to the power of 3
print(2 // 4) #round down the answer of division to int.

print(type(2+4))
print(type(2-4))
print(type(2*4))
print(type(2/4))
print(type(2%4))

##Complex data type. Beside int or flaot, there is complex too.
## BIN() returns binary number of the parameter
print(bin(5)) ## the answer contains 0b which indicates the binary number
# print(bin(10.5)) ##only integer
print(int('0b101', 2)) ## ,2 means base 2

# A str is simple a piece of text
'hi hello there!!!' # '' or "" is fine
print(type("hi hello there!!!"))
username = "supercode"
password = "supercoder"

longString = '''
WOW, 
THIS IS
A LONG
STRING
'''

print(longString)

# STRING CONCATENATION
print("hello " + " Chris")
# Cant do print("hello " + 5). String cant be operated with integer

print(type(str(500))) # -> str
print(type(int(str(500)))) # -> int