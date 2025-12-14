import json
import re
import random
import string
def caesar_encrypt(text, shift):
    encrypted_text = ""
    for char in text:
        if char.isalpha():
            shifted = ord(char) + shift
            if char.islower():
                if shifted > ord('z'):
                    shifted -= 26
            elif char.isupper():
                if shifted > ord('Z'):
                    shifted -= 26
            encrypted_text += chr(shifted)
        else:
            encrypted_text += char
    return encrypted_text
def caesar_decrypt(text, shift):
    return caesar_encrypt(text, -shift)
def is_strong_password(password):
    if len(password) < 8:
        return False
    if not re.search(r"[A-Z]", password):
        return False
    if not re.search(r"[a-z]", password):
        return False
    if not re.search(r"[0-9]", password):
        return False
    if not re.search(r"[!@#$%^&*(),.?\":{}|<>]", password):
        return False
    return True
def generate_password(length):
    characters = string.ascii_letters + string.digits + "!@#$%^&*()"
    return "".join(random.choice(characters) for _ in range(length))
encrypted_passwords = []
websites = []
usernames = []

encrypted_passwords = []
websites = []
usernames = []

def add_password():
    website = input("Enter website: ")
   username = input("Enter username: ")
   choice = input("Generate strong password? (y/n): ")
   if choice.lower() == "y":
       password = generate_password(12)
       print("Generated password:", password)
   else:
       password = input("Enter password: ")
       if not is_strong_password(password):
           print("Warning: Password is weak!")
   encrypted = caesar_encrypt(password, 3)
   websites.append(website)
   usernames.append(username)
   encrypted_passwords.append(encrypted)
   print("Password added successfully!")
    Add a new password to the password manager.

    This function should prompt the user for the website, username,  and password and store them to lits with same index. Optionally, it should check password strengh with the function is_strong_password. It may also include an option for the user to
    generate a random strong password by calling the generate_password function.

    Returns:
        None
    """

# Function to retrieve a password 
def get_password():
       website = input("Enter website to retrieve password: ")
   if website in websites:
       index = websites.index(website)
       username = usernames[index]
       encrypted = encrypted_passwords[index]
       decrypted = caesar_decrypt(encrypted, 3)
       print("Username:", username)
       print("Password:", decrypted)
   else:
       print("Website not found.")
    Retrieve a password for a given website.

    This function should prompt the user for the website name and
    then display the username and decrypted password for that website.

    Returns:
        None
    """

# Function to save passwords to a JSON file 
def save_passwords():
   vault = []
   for i in range(len(websites)):
       vault.append({
           "website": websites[i],
           "username": usernames[i],
           "password": encrypted_passwords[i]
       })
   with open("vault.txt", "w") as file:
       json.dump(vault, file)
   print("Passwords saved successfully!")
    Save the password vault to a file.

    This function should save passwords, websites, and usernames to a text
    file named "vault.txt" in a structured format.

    Returns:
        None
    """

    Returns:
        None
    """

# Function to load passwords from a JSON file 
def load_passwords():
    try:
        with open("vault.txt", "r") as file:
            vault = json.load(file)
        websites.clear()
        usernames.clear()
        encrypted_passwords.clear()
        for entry in vault:
            websites.append(entry["website"])
            usernames.append(entry["username"])
            encrypted_passwords.append(entry["password"])
        print("Passwords loaded successfully!")
    except FileNotFoundError:
        print("No saved password file found.")
     """
    Load passwords from a file into the password vault.

    This function should load passwords, websites, and usernames from a text
    file named "vault.txt" (or a more generic name) and populate the respective lists.

    Returns:
        None

  # Main method
def main():
# implement user interface 

  while True:
    print("\nPassword Manager Menu:")
    print("1. Add Password")
    print("2. Get Password")
    print("3. Save Passwords")
    print("4. Load Passwords")
    print("5. Quit")
    
    choice = input("Enter your choice: ")
    
    if choice == "1":
        add_password()
    elif choice == "2":
        get_password()
    elif choice == "3":
        save_passwords()
    elif choice == "4":
        passwords = load_passwords()
        print("Passwords loaded successfully!")
    elif choice == "5":
        break
    else:
        print("Invalid choice. Please try again.")

# Execute the main function when the program is run
if __name__ == "__main__":
    main()
