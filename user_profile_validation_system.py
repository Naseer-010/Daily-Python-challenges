print("User Profile Validation System")

name = input("Your Name: ")
Email = input("Email: ")
Mobile = input("Mobile: ")
age = int(input("Your Age: "))

valid = True

if " " not in name or name[0] == " " or name[-1] == " ":
    valid = False

if "@" not in Email or Email.count("@") != 1 or Email[0] == "@" or Email[-1] == "@" or " " in Email:
    valid = False

try:
    int(Mobile)
    mobile_digits = True
except ValueError:
    mobile_digits = False

if len(Mobile) != 10 or not mobile_digits or Mobile[0] == "0":
    valid = False

if age < 18 or age > 60:
    valid = False

if valid:
    print("User Profile is Valid")
else:
    print("User Profile is Invalid")