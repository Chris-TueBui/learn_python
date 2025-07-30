# Tuple
# Like list. But unlike list, tuple is immutable.
# Meaning, it cannot change. It is fixed.
# Use brackets to define a tuple.
# cant sort tuple. Or reverse tuple.
myTuple = (1, 2 ,3 ,4 ,5)
print(myTuple[0])
print(5 in myTuple) 

#Benefit:
# If you dont want to change the list, you can use tuple.
# It tells other programers and they know it should not change.
# Makes thing easier
# Makes code more predictable.
# Faster than list
# Drawbacks:
# Less flexible
# Cant sort, cant reverse.

#Basically a list just multiple tuples together.
#Tuple cant be used as value in dictionary.
#Tuple can be used as key in dictionary.
user = {
    (1, 2): [1, 2, 3],
    'basket': 'hello',
    'age': 30
}
print(user[(1, 2)]) # Access the value of the key (1, 2) in the dictionary user.
# Cant use print(user[0]) because 0 is not a key in the dictionary user.

new_tuple = myTuple[1:2] # new_tuple = (2,)
# When slicing a tuple, it returns a new tuple.
# Tuple only has 1 element, tend to have a comma at the end.
x, y = myTuple[0:2] # x = 1, y = 2
x, y *other = myTuple[0:4] # x = 1, y = 2, other = (3, 4, 5)    
#*other type is list type in this case

#Tuple only has 2 methods: count() and index()
print(myTuple.count())
print(myTuple.count(3)) # Returns the number of occurrences of the value 3 in the tuple.
print(myTuple.index(3)) # Returns the index of the first occurrence of the value 3 in the tuple.
print(len(myTuple)) # Returns the number of elements in the tuple.
