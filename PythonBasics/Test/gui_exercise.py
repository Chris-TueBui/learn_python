#Exercise
# If '0', then shows nothing. If '1', then shows *
picture = [
    [0, 0, 0, 1, 0, 0, 0],
    [0, 0, 1, 1, 1, 0, 0],
    [0, 1, 1, 1, 1, 1, 0],
    [1, 1, 1, 1, 1, 1, 1],
    [0, 0, 0, 1, 0, 0, 0],
    [0, 0, 0, 1, 0, 0, 0]
]

#Solution 1
for insideList in picture:
    result = ""
    for value in insideList:
        if (value == 0):
            result += " "
        else:
            result += "*"
    print(result)

#solution 2
i = 0
while i < len(picture):
    line = picture[i]
    for index in line:
        if (index == 0):
            print(" ", end='')
        else:
            print("*", end='')
    print('')
    i+=1;

#solution 3
fill = "*"
empty = " "
for row in picture:
    for value in row:
        if (value): # truthy variable.
            print(fill, end='')
        else:
            print(empty, end='')
    print("")

#Exercise. Check duplicate in list:
someList = ['a', 'b', 'c', 'b', 'd', 'm', 'n', 'n']
# someList.sort()
# listRange = range(len(someList))
# for i in listRange:
#     if (i == len(someList)-1):
#         break;
#     if (someList[i] == someList[i+1]):
#         print(someList[i])

duplicate = []
for item in someList:
    if (someList.count(value) > 1):
        if value not in duplicate:
            duplicate.append(value)
            
print(duplicate)
