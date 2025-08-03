import random
import string

def generate_code(length=7):
    characters = string.ascii_letters + string.digits  # a-z, A-Z, 0-9
    return ''.join(random.choices(characters, k=length))

# Example usage
code = generate_code()
print("Generated code:", code)
