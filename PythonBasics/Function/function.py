# "def": declaration of function.

def sayHello():
    print("Hellooo")

sayHello()

#Interpreter goes line by line. So calling function must be below defining function.

picture = [
    [0, 0, 0, 1, 0, 0, 0],
    [0, 0, 1, 1, 1, 0, 0],
    [0, 1, 1, 1, 1, 1, 0],
    [1, 1, 1, 1, 1, 1, 1],
    [0, 0, 0, 1, 0, 0, 0],
    [0, 0, 0, 1, 0, 0, 0]
]
def showTree():
    for insideList in picture:
        result = ""
        for value in insideList:
            if (value == 0):
                result += " "
            else:
                result += "*"
        print(result)

showTree()


def sayHello1(name, emoji):
    print(f"Hello {name} {emoji}")

sayHello1("Chris", "LOL")

#arguments: are used as the actual value we provide to the function.
#parameters: are used when we define the function.
#position matters in the above Called positional.

#Keyword arguments:
#Not worry about position.
#THIS IS BAD PRACTICE.
sayHello1(emoji="LOL", name="Bibi")

#Default parameters:
#Define when declaring the function.
def sayHello2(name = "Darth Varder", emoji = "LOL"):
    print(f"Hello {name} {emoji}")

sayHello2()
sayHello2("timmy")

def sum(num1, num2):
    num1 + num2

print(sum(4, 5)) # <-- None.

def sum1(num1, num2):
    return num1 + num2;

print(sum1(4, 5))

#Function should only do 1 thing and should return something.

