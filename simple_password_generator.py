import random
import string

print("Choose the length of your password:")
length = int(input())
if length == str or length <= 0:
    print("Please enter a valid number")

lowercase = string.ascii_lowercase
uppercase = string.ascii_uppercase
numbers = string.digits
symbols = "!@#$%^&*"

all_chars = lowercase + uppercase + numbers + symbols

password = ""

for i in range(length):
    password += random.choice(all_chars)
print(f"""Your password: 
{password}""")