import random
import string

def generate_password(length):
    characters = string.ascii_letters + string.digits + "!@#$%"
    return "".join(random.choices(characters, k=length))

length = int(input("Enter password length: "))

if length >= 8:
    print("Generated Password:", generate_password(length))
else:
    print("Password length must be at least 8.")
