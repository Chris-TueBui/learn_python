def someRandomStuff():
    pass

# Method:
# To call it, use "."
# Has to be owned by soemthing.


'hello'.capitalize()
print('hello'.capitalize())


# Doc string:
def test(a):
    '''
    INFO: this function tests and prints param a
    This is like /**/ in java.
    '''
    print(a)


test('!!!')
help(test)
print(test.__doc__)

# scope: what variables do I have access to?


def someFunc():
    total = 100

# It checks in local function first, then check global, then check built in python function


# Global keyword
total = 0


def count():
    # We can use something like this syntax:
    global total
    total += 1
    return total


def count1(total):
    total += 1
    return total


print(count())
print(count1(total))

# non-global keyword:
# refer to the parent local. Parent local meaning a function inside a function
# If in the example below, we dont use nonlocal, then the outer is still "local"


def outer():
    x = "local"

    def inner():
        nonlocal x
        x = "nonlocal"
        print("inner: ", x)

    inner()
    print("Outer: ", x)


outer()
