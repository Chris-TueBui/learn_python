# *args vs. **kwargs

#Can accept any number of position arguments.
def superFunc(*args):
    #args is a tuple in function.
    print(*args)
    print(args)
    return sum(args)

print(superFunc(1,2,3,4,5))

def superFunc1(*args, **kwargs):
    #kwargs is dictionary in function
    print(kwargs)
    total = 0
    for items in kwargs.values():
        total += items
    return sum(args) + total

print(superFunc1(1,2,3,4,5, num1=5, num2=10))

#Rule of ordering:
# params, *args, default parameters, **kwargs
def superFunc2(name, *args, i='hi', **kwargs):
    print(name)
    print(*args)
    print(i)
    print(kwargs)

print(superFunc2('Chris', 1,2,3,4,5, 'Bui', num1 = 5, num2=10))