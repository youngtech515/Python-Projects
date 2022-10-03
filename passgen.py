import string
import random
import sys

all_chars = string.printable[:-6]
len_pass = input("How long should the password be? ")

try:
    len_pass = int(len_pass)
except ValueError:
    print("Invalid password length")
    sys.exit(1)

password = ''
for _ in range(len_pass):
    password += random.choice(all_chars)
print(f"Your password is: {password}")