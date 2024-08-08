li = [1, 2, 3, 4, 5]
li2 = ["a", "b", "c"]
li3 = [1, 2, "a", "b", True, False, 1.2, 1.5]

amazonCart = [
    "notebooks", 
    "sunglasses", 
    "toys",
    "grapes"]
print(amazonCart[0])

### LIST SLICING
print(amazonCart)
# print(amazonCart[0:2:2])
amazonCart[0] = "laptop" #List is mutable. Meaning, it can change unlike String.
print(amazonCart[1:3])
print(amazonCart)

new_cart = amazonCart; 
new_cart = amazonCart[:] # Create a copy using slicing. And these 2 points to different objects in memory
new_cart[0] = "gum"
print(new_cart) # ["gum", "sunglasses", "toys", "grapes"]
print(amazonCart) # ["gum", "sunglasses", "toys", "grapes"]

### MATRIX
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

print(matrix[0][1]) 

### LIST METHOD
basket = [1, 2, 3, 4, 5]
print(len(basket))

new_list = basket.append("Chris Bui")
# If I do print new_list right here, the result is None because the append() doesnt return a new list.

# Adding
# basket.insert(3, "Chris bui")
# new_list = basket.extend([100])

# print(basket) 
# print(new_list)

#Removing
# basket.pop() # Removing the object at the last index. Pop does return whatever the object was removed.
# basket.remove("Chris bui") # Removing the specified object
# newest_list = basket.clear()
# print(newest_list)
# print(basket)

listStr = ["a", "b", "c", "d", "e"]

# print(listStr.index("d", 0, 1))
print("d" in listStr)
print("i" in "Hi my name is Ian")
print(listStr.count("a")) # Count how many times the letter appears.

list1 = ["a", "s", "r", "t", "o", "n"]
# list1.sort()
sortedList = sorted(list1) # Create a new array but sorted 
reverseList = list1[:]
reverseList.reverse()
# print(list1)
print(sortedList) 
print( reverseList)