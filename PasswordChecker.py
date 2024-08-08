username = input("Username: ")
password = input("Password:")
passwordLength = len(password)

passwordEncrypt = "*" * passwordLength

print(f"{username}, password {passwordEncrypt} is {passwordLength} letters long")