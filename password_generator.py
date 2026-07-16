# Project 3: Random Password Generator
# DecodeLabs Industrial Training Kit

import random
import string

# Ask the user how long they want their password to be
# Keep asking until they enter a valid positive number
length = int(input("Enter the desired password length: "))

while length <= 0:
    print("Password length must be a positive number greater than 0.")
    length = int(input("Enter the desired password length: "))

# Combine letters (upper + lower case) and numbers into one pool of characters
characters = string.ascii_letters + string.digits

# Build the password by picking random characters from the pool
password = ""
for i in range(length):
    password = password + random.choice(characters)

# Show the result to the user
print("Your generated password is:", password)