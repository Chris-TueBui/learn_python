# print("Chris Bui")
# s = input("Your name ")
# print("Hello %s" %s)

### ESCAPE SEQUENCE
# Using back slash just like how java does it
# \t add a tab
# \n new line
weather = "It\'s sunny";
weather1 = "\t It\'s \"kinda of\" sunny \n Hope you have a good day!"
print(weather)
print(weather1)

### FORMATTED STRING
name = input("Please enter your name here: ")
age = 24

print("Hi %s" %name)
print("Hi: " + name)
print(f"Hi {name}. You're {age}")
# Within the {} you can specify the index in format starting with 0.
print("Hi {}. You're {}".format(name, age))
print("Hi {new_name}. You're {new_age}".format(new_name="new name", new_age="new_age"))

### STRING INDEXES
selfish = "me me me"
###        01234567
print(selfish[0])
#Format to start and stop taking the indexes: [start:stop]. You can specify something like [1::] <- take all from 1, [:5] <- take from the first to the fifth.
#stepover: [start:stop:stepover]. 
### STRING SLICING
print(selfish[0:2])
print(selfish[0:7:2])
print(selfish[1::2])
print(selfish[-1]) #<- the minus sign mean take from the end index.
print(selfish[::-1])
