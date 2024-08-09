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

###Booleans
#Boolean value can be True or False
#bool(0) is false and bool(1) is true
name = "Chris Bui"
is_cool = False
print(f"{name} is {is_cool}")
is_cool = True
print(name + " " + str(is_cool))
print(bool(0))
print(bool(1))


### NONE
weapons = None
print(weapons) #None

### Dictionary
# In another language, it's like hash map
# Data type and data structure.
# Has something like key-value pair. Denote as below
# It is un-ordered key-pair. Not near each other in memory
dictionary = {
    'a': 1,
    'b': 2,
    'x': 3
}
print(dictionary['b'])
print(dictionary)

dictionary1 = {
    'a': [1, 2, 3],
    'b': 'hello',
    'c': True
}
print(dictionary1['a'])
print(dictionary1['a'][1])

myList = [
    {
        'a': [1, 2, 3],
        'b': "hello",
        'c': True
    },
    {
        'a': [4, 5, 6],
        'b': 'hello',
        'c': True
    }
]

print(myList[0]['a'][2])

### WHEN TO USE LIST AND WHEN TO USE DICTIONARY
# list has order indexes
# dictionary has no order.
# Dictionary can store more elements then list. While list has a fixed size.
# List has index. While dictionary holds a lot more information.
# List store indexes and its value. Dictionary can be used to store the key and value pair.
# Dictionary value can be any data types

### DICTIONARY KEYS
# Keys have to immutable.
# List cant be key. Because list is mutable.
# Usually a key is something descriptive like a string
# Keys have to be unique. If 2 keys are the same, the latest overrides the first one.
dict2 = {
    123: [1, 2, 3],
    True: 'Hello',
}
print(dict2[123])
print(dict2[True])
print(dict2.get("age")) # Safe way to get a key if you're not sure if key exists in the dictionary or not.
print(dict2.get('age', 55)) # Grab the age from dictionary, if "age" does not exist, then use the value 55.

user2 = dict(name='JohnJohn')
print(user2)

print('basket' in user2)
print(123 in dict2)
print('age' in dict2.keys()) # goes through all the keys
print('age' in dict2.values()) # goes through all the values
print('age' in dict2.items()) # goes through all the items.
print(dict2.keys())

print(dict2.clear()) # clear() doesnt return anything

dict2 = user2.copy()

print(dict2.pop("name"))

#popitem() -> used to remove the last key-value pair.
print(dict2.update({"name": "chris bui"})) #update doesnt return anything
print(dict2)