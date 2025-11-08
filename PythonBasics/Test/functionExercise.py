#age = input("What's your age?: ")

#if int(age) < 18:
#    print("Sorry, you are too young to drive this car. Powering off")
#elif int(age) > 18:
#    print("Powering on. Enjoy the ride")
#elif int(age) == 18:
#    print("Congratulations on your first year of driving. Enjoy the ride!")

#1 
#Wrap the code above in a function called checkDriverAge(), Whenever you call this function, you will get prompted for age.

#2
#Instead of using the input(). Now, make the checkDriverAge() function accept an argument of age, so that if you enter:
#checkDriverAge(92)
#it returns "Power on. Enjoy the ride."
#also make it so that the default age is set to 0 if no argument is given

#1
def checkDriverAge():
    age = input("What's your age?: ")
    if int(age) < 18:
        print("Sorry, you are too young to drive this car. Powering off")
    elif int(age) > 18:
        print("Powering on. Enjoy the ride")
    elif int(age) == 18:
        print("Congratulations on your first year of driving. Enjoy the ride!")

checkDriverAge()

#2
def checkDriverAge1(age = 0):
    #age = input("What's your age?: ")
    if int(age) < 18:
        print("Sorry, you are too young to drive this car. Powering off")
    elif int(age) > 18:
        print("Powering on. Enjoy the ride")
    elif int(age) == 18:
        print("Congratulations on your first year of driving. Enjoy the ride!")

driverAge = input("What's your age?: ")
if driverAge == '':
    driverAge = 0
checkDriverAge1(driverAge)