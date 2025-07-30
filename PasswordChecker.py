username = input("Username: ")
password = input("Password:")
passwordLength = len(password)

passwordEncrypt = "*" * passwordLength ## the password is * times the length. 

print(f"{username}, password {passwordEncrypt} is {passwordLength} letters long")