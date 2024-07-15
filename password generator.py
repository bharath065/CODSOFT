import random
import string

passlength = int(input("Enter the length needed for your password: "))
if passlength < 1:
    print("Password's length should be at least 1.")
else:
    print("Invalid input. Please enter a valid number.")
characters = string.ascii_letters + string.digits + string.punctuation
password = ''.join(random.choice(characters) for _ in range(passlength))
print("Generated password:",password)
