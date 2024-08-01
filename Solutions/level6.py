import bcrypt

# Function to hash a password


def hash_password(password):
    # Generate a salt for hashing
    salt = bcrypt.gensalt()
    # Hash the password using bcrypt and the generated salt
    hashed = bcrypt.hashpw(password.encode('utf-8'), salt)
    # Return the hashed password
    return hashed

# Function to verify a password


def verify_password(password, hashed):
    # Check if the given password matches the hashed password
    return bcrypt.checkpw(password.encode('utf-8'), hashed)

# Example usage of the hashing and verification functions


# Define a password to be hashed
password = "securepassword123"

# Hash the password using the hash_password function
hashed_password = hash_password(password)

# Print the hashed password
print(f"Hashed password: {hashed_password}")

# Verify the password using the verify_password function
is_valid = verify_password("securepassword123", hashed_password)

# Print whether the password is valid
print(f"Password is valid: {is_valid}")


# Importing the bcrypt library:

# The code begins by importing the bcrypt library, which is a Python library used for hashing passwords securely. It provides functions for generating salts, hashing passwords, and verifying password hashes.
# Function hash_password:

# This function takes a plaintext password as input and returns a hashed version of the password.
# It generates a salt using bcrypt.gensalt(). A salt is a random value that is used to ensure that the same password will hash to a different value each time, increasing security.
# The password is hashed using bcrypt.hashpw(), which combines the password and salt to produce a hashed password.
# The function returns the hashed password, which can be stored securely in a database.
# Function verify_password:

# This function checks whether a given plaintext password matches a previously hashed password.
# It uses bcrypt.checkpw(), which takes the plaintext password and the hashed password as inputs, encoding the plaintext password to UTF-8 for compatibility.
# It returns True if the passwords match and False otherwise, allowing verification of password authenticity.
# Example Usage:

# A sample password("securepassword123") is defined and hashed using the hash_password function.
# The hashed password is printed to the console.
# The original password is then verified against the hashed password using the verify_password function.
# The result of the verification(True or False) is printed, indicating whether the original password matches the hashed password.
