greeting = "Helloooooo"
print(greeting[0:len(greeting)])

quote = "To be or not to be"
print("UPPER METHOD " + quote.upper())
print("CAPITALIZE " + quote.capitalize())
print(quote.find("be"))
print(quote.replace("be", "me"))
print(quote) #<- String can only be override. In this case, when we do quote.replace we are not assigning to any variable. Hence it will print the original message

