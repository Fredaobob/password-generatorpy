import string
import random
import os

def generate_password(length, include_uppercase, include_numbers, include_symbols):
    characters = string.ascii_lowercase
    if include_uppercase:
        characters += string.ascii_uppercase
    if include_numbers:
        characters += string.digits
    if include_symbols:
        characters += string.punctuation

    password = ''.join(random.choice(characters) for _ in range(length))
    return password

def save_password(password):
    file_path = os.path.join(os.getcwd(), 'generated_passwords.txt')
    with open(file_path, 'a') as file:
        file.write(password + '\n')
    print(f"Password saved to {file_path}")

def main():
    print("Welcome to the Password Generator!")
    length = int(input("Enter the length of the password: "))
    include_uppercase = input("Include uppercase letters? (y/n): ").lower() == 'y'
    include_numbers = input("Include numbers? (y/n): ").lower() == 'y'
    include_symbols = input("Include symbols? (y/n): ").lower() == 'y'

    password = generate_password(length, include_uppercase, include_numbers, include_symbols)
    print(f"Generated Password: {password}")

    save_password_option = input("Would you like to save the password to a file? (y/n): ").lower() == 'y'
    if save_password_option:
        save_password(password)

if __name__ == "__main__":
    main()

