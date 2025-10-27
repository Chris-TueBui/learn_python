for item1 in "zero to mastery":
    print(item1)

for item2 in [1, 2, 3, 4, 5]:
    print(item2)

for item3 in (1, 2, 3, 4, 5):
    print(item3)

# The last iteration where the loop assigns the value to item1, item2, item3 the last time, you can still use it outside of loop
print(item1)
print(item2)
print(item3)

for item in (1, 2, 3, 4, 5):
    for x in ['a', 'b', 'c']:
        print(item, x)

print(x)

#iterable: can be list, dictionary, typle, set, string, etc.
# iterated: one by one check each item in the collection

users = {
    'name': 'Golem',
    'age': 5006,
    'canSwim': False,
}
    
for item in users.items():
    print(item)

for item in users.values():
    print(item)

for item in users.keys():
    print(item)

for item in users.items():
    key, value = item # -> key will get the key, and value will get the value
    print(key, value) # -> another way to do this.

#better way:
for k, v in users.items():
    print(k, v)

# EXERCISE:
#counter: sum the total of the list
myList = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
sum = 0
for num in myList:
    sum += num
print(sum)


while True:
    string = input('say something: ')
    print(string)
    break;