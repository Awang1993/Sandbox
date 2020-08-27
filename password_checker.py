"""
CP1404 - Password Checker
"""

MIN_LENGTH = 5

user_password = input("Please enter password: ")
while len(user_password) < MIN_LENGTH:
    print("Please enter a password with at least {} characters".format(MIN_LENGTH))
    user_password = input("Please enter password: ")
for char in user_password:
    print("*", end="")
