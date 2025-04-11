import random
import string

def generate_password(length, use_uppercase, use_lowercase, use_numbers, use_special_chars):
    # Create a pool of characters based on user preferences
    character_pool = ""
    if use_uppercase:
        character_pool += string.ascii_uppercase
    if use_lowercase:
        character_pool += string.ascii_lowercase
    if use_numbers:
        character_pool += string.digits
    if use_special_chars:
        character_pool += string.punctuation

    # Ensure the pool is not empty
    if not character_pool:
        raise ValueError("You must select at least one character type!")

    # Generate a random password
    password = "".join(random.choice(character_pool) for _ in range(length))
    return password

# User input for customization
try:
    length = int(input("Enter password length: "))
    use_uppercase = input("Include uppercase letters? (yes/no): ").lower() == "yes"
    use_lowercase = input("Include lowercase letters? (yes/no): ").lower() == "yes"
    use_numbers = input("Include numbers? (yes/no): ").lower() == "yes"
    use_special_chars = input("Include special characters? (yes/no): ").lower() == "yes"

    # Generate and display the password
    generated_password = generate_password(length, use_uppercase, use_lowercase, use_numbers, use_special_chars)
    print(f"Your generated password is: {generated_password}")
except ValueError as e:
    print(f"Error: {e}")