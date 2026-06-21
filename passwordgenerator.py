import random
import string

def generate_password(length):
    # Character sets
    letters = string.ascii_letters
    digits = string.digits
    symbols = string.punctuation

    # Combine all characters
    all_characters = letters + digits + symbols

    # Generate password
    password = ''.join(random.choice(all_characters) for _ in range(length))
    return password


# User input
try:
    length = int(input("Enter desired password length: "))

    if length <= 0:
        print("Please enter a positive number.")
    else:
        password = generate_password(length)
        print("\nGenerated Password:", password)

except ValueError:
    print("Invalid input! Please enter a number.")