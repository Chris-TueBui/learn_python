def someRandomStuff():
    pass

#Method:
# To call it, use "."
# Has to be owned by soemthing.

'hello'.capitalize()
print('hello'.capitalize())


#Doc string:
def test(a):
    '''
    INFO: this function tests and prints param a
    This is like /**/ in java.
    '''
    print(a)

test('!!!')
help(test)
print(test.__doc__)

#scope: what variables do I have access to?
def someFunc():
    total = 100

#It checks in local function first, then check global, then check built in python function