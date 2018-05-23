password = raw_input("Enter your password you wish to enhance: ")
enhanced_password = ""

password.lower()

for letter in password:
    if letter == "a":
        enhanced_password += "@"
    elif letter == "s":
        enhanced_password += "$"
    elif letter == "e":
        enhanced_password += "3"
    else:
        enhanced_password += letter
    
print enhanced_password