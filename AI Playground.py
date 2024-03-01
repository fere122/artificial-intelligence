#Programer: Mr. Lange
#Date:2.29.2024
#Program: AI Playground

print("This will be a place for me to play with programming using AI technology\n")

import hashlib
import getpass

def hash_password(password):
    # Using SHA-256 for hashing, you can choose a different algorithm if needed
    hashed_password = hashlib.sha256(password.encode()).hexdigest()
    return hashed_password

def main():
    # Get password securely without echoing it
    password = getpass.getpass("Enter your password: ")

    # Print asterisks for each character entered
    hashed_input = '*' * len(password)
    print("Hashed Input:", hashed_input)

    # Hash the password
    hashed_password = hash_password(password)

    # Print the hashed password
    print("Hashed Password:", hashed_password)

if __name__ == "__main__":
    main()

