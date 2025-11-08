#Take in a list

def highest_even(*args):
    highestEven = -1
    #args[0] is getting the value in the list below.
    for item in args[0]:
        if item % 2 == 0 and item > highestEven:
            highestEven = item
    return highestEven

def highestEven(list):
    evens = []
    for item in list:
        if item % 2 == 0:
            evens.append(item)
    return max(evens)

print(highest_even([10,1,2,3,4,8,11]))
print(highestEven([10,1,2,3,4,8,11]))