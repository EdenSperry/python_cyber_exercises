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
