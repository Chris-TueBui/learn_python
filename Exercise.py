import datetime

birthYear = input("What year were you born? ")
age = datetime.date.today().year - int(birthYear)
print(f"Your age is {age}")