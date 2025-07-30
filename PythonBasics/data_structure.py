li = [1, 2, 3, 4, 5]
li2 = ["a", "b", "c"]
li3 = [1, 2, "a", "b", True, False, 1.2, 1.5]

amazonCart = [
    "notebooks", 
    "sunglasses", 
    "toys",
    "grapes"]
print(amazonCart[0])

##how to reverse
#syntax: list[start:end:step] 
#for step: negative means reverse the list
#for step: postive means normal order.
#if not provided, it will take the whole list.
#if step is not provided, it will take the whole list, default step is 1.
print(amazonCart[::-1]) # Reverse the list
print(amazonCart[::-2]) # Reverse the list with step 2

### LIST SLICING
print(amazonCart)
print(amazonCart[0:2:2]) # Slicing from index 0 to 2, with step 2. In this case, exclude index 2.
amazonCart[0] = "laptop" #List is mutable. Meaning, it can change unlike String.
print(amazonCart[1:3])
print(amazonCart)

new_cart = amazonCart; 
new_cart = amazonCart[:] # Create a copy using slicing. And these 2 points to different objects in memory
new_cart[0] = "gum"
print(new_cart) # ["gum", "sunglasses", "toys", "grapes"]
print(amazonCart) # ["laptop", "sunglasses", "toys", "grapes"]

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
basket.insert(3, "Chris bui")
new_list = basket.extend([100]) # .extend does not return a new list.

#I can also use insert(): has to specify the index.
basket.insert(0, "Chris Bui") # Insert at index 0
#I can also use extend(): has to specify the list.
basket.extend(["Chris Bui", "Chris Bui 123"]) # Extend the list with multiple elements

#pop: pop() removes the last element in the list.
basket.pop() # Removing the object at the last index. Pop does return whatever the object was removed.
#if pop has an index, it will remove the object at that index.
basket.pop(0) # Removing the object at index 0.
basket.remove("Chris Bui") # Removing the specified object


print("Basket: " + str(basket)) 
print("New list: " + str(new_list))

#Removing
# basket.pop() # Removing the object at the last index. Pop does return whatever the object was removed.
# basket.remove("Chris bui") # Removing the specified object
# newest_list = basket.clear()
# print(newest_list)
# print(basket)

listStr = ["a", "b", "c", "d", "e"]

print(listStr.index("d", 0, 1))
#index() returns the index of the first occurrence of the specified value.
#index() can take 2 optional parameters: start and end. It will search for the value in the specified range.
print(listStr.index("d", 0, 5)) # Search for "d" from index 0 to index 5.
print("d" in listStr) #true if "d" is in the list, false otherwise.
print("i" in "Hi my name is Ian")
print(listStr.count("a")) # Count how many times the letter appears.

list1 = ["a", "s", "r", "t", "o", "n"]
# list1.sort()
#sort() sorts the list in place and returns None. Modiefies the original list.
#sorted() creates a new sorted list from the elements of any iterable. Does not modify the original list
sortedList = sorted(list1) # Create a new array but sorted 
reverseList = list1[:] # Create a new list.
reverseList.reverse()
# print(list1)
print(sortedList) 
print(reverseList)


print(list(range(1, 100))) #starts from 1 to 99. Exclude whatever is at the end.
print(list(range(100))) #starts from 0 to 99. Exclude whatever is at the end.
#range can also take a step parameter.
print(list(range(1, 100, 2))) #starts from 1 to 99, with step 2. Exclude whatever is at the end.
#range can also take a negative step parameter.
print(list(range(100, 1, -2))) #starts from 100 to 2, with step -2. Exclude whatever is at the end. 

#join() String concatenation of string and a list
sentence = "!"
new_sentence = sentence.join(["Hi", "my", "name", "is", "jojo"])
print(sentence) # Hi!my!name!is!jojo. 
print(" ".join(["Hi", "my", "name", "is", "JOJO"])) # Hi my name is JOJO

# LIST UNPACKING
basket_new = [1, 2, 3, 4, 5, 6, 7, 8, 9]
a, b, c = [1, 2, 3]
print(a) # 1
print(b) # 2
print(c) # 3

a1, b1, c1, *other = basket_new
print(other) # 4, 5, 6, 7, 8, 9
a2, b2, c2, *other, d = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(d) # 9
print(other) #[4, 5, 6, 7, 8]

