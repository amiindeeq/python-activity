import random
import string

def generate_password(length):
    characters = string.ascii_letters + string.digits + string.punctuation  # Alphanumeric and symbolic characters
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

# Usage example
password_length = 12
generated_password = generate_password(password_length)
print("Generated Password:", generated_password)