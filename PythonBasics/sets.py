#SET
#set is simply unordered collection of unique objects
# EVERY OBJECTS HAVE TO BE UNIQUE
mySet = {1, 2, 3, 4, 5}
print(mySet) # {1, 2, 3, 4, 5}

mySet2 = {1, 2, 3, 4, 5, 5} # Duplicates are ignored
print(mySet2) # {1, 2, 3, 4, 5}

mySet.add(100)
mySet.add(2) # Adding an element to the set
print(mySet) # {1, 2, 3, 4, 5, 100}

myList = [1 ,2 ,3, 4, 4, 5, 6, 5]
#Junior code
mySetFromList = set() #Use set() to create an empty set

for item in myList:
    mySetFromList.add(item)

print(f"My Set From List {mySetFromList}")

#Senior code
mySetFromList1 = set(myList) # Create a set from a list

#Set object doesnt support indexing
mySet2 = {1, 2, 3, 4, 5}
print(1 in mySet2) # True. Use "in" to check if an element is in the set
print(len(mySet2)) # Returns the number of elements in the set
#convert set to list:
mySet2List = list(mySet2) # Convert set to list

mySet3 = mySet.copy()
print(f"My Set 3: {mySet3}") # {1, 2, 3, 4, 5, 100}

mySet3.clear() # Clear the set. The return is "set()"

#FUNCTIONS
# difference() returns a new set with elements in the first set that are not in the second set
# discard() removes an element from the set if it is a member. If not, it does nothing
# difference_update() removes all elements of another set from this set
# intersection() returns a new set with elements common to the two sets
# isdisjoint() returns True if two sets have a null intersection
# issubset() returns True if another set contains this set
# issuperset() returns True if this set contains another set
# union() returns a new set with elements from both sets

my_set = {1, 2, 3, 4, 5}
your_set = {4 ,5, 6, 7, 8, 9, 10}

# difference: 
# Find the difference between two sets
#print(my_set.difference(your_set)) # {1, 2, 3}

# discard:
# return None if the element is not in the set.
# It modifies the original set.
#print(my_set.discard(3))
#print(my_set) # {1, 2, 4, 5}
#print(my_set.discard(your_set))

# difference_update:
# Modifies the original set by removing elements found in another set. Return None.
#my_set.difference_update(your_set) # Removes all elements of your_set from my_set. I.E, removes 4, 5
#print(my_set) # {1, 2, 3}

# intersection:
# Moves the common elements between two sets into a new set. Returns a new set.
#print(my_set.intersection(your_set)) # {4, 5}
# another way to do intersection is using the ampersand operator &
# print(my_set & your_set) # {4, 5}

# isdisjoint:
# checks if two sets have COMMON elements. Returns True or False. Returns True if there is no common elements between two sets.
print(my_set.isdisjoint(your_set)) # Returns False because there are common elements (4, 5) between two sets.
print(my_set.isdisjoint(your_set)) # Returns True if there is no common elements between two sets.

#UNION:
#United 2 sets together. Returns a new set with elements from both sets. But remove duplicates.
#print(my_set.union(your_set)) # Returns a new set with elements from both sets. {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
#Another way to do union is using the pipe operator |
#print(mySet | your_set)

#issubset:
my_set1 = {1, 2}
print(my_set1.issubset(my_set)) # Returns True because my_set1 is a subset of my_set
print(my_set.issubset(my_set1)) # Returns False because my_set is not a subset of my_set1.

#issuperset:
print(my_set.issuperset(my_set1)) # Returns True because my_set is a superset of my_set1
print(my_set1.issuperset(my_set)) # Returns False because my_set1 is not a superset of my_set.

