#Arthur Poon
#MPCS 50101 2,1 Intro to Programming Monday Section
#Problem 3


#ask for input password

password_input = input("Enter a password: ")



# Logic for security checks:
# Have at least 12 characters
# Contains both numbers and letters
# Contains at least one of the following characters: !,@,#,$,%
# Contains at least one capital letter and one lower-case letter

if len(password_input)>=12 and password_input.isalnum() == True and any(password_character in password_input for password_character in ["!","@","#","$","%"]) and not password_input.islower() and not password_input.isupper():
    print("This is a strong password :)")
else:
    print("This is not a strong password :(   ")