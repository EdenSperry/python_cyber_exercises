import itertools
import string
import time


def brute_force_attack(target_password, charset=string.ascii_lowercase + string.digits, max_length=5):
    """
    Attempts to crack the password using brute force.

    :param target_password: The password to crack.
    :param charset: Characters to use for generating passwords.
    :param max_length: Maximum length of passwords to try.
    """
    print(f"Starting brute force attack on password: {target_password}")
    # Record the start time to measure how long the attack takes.
    start_time = time.time()

    # Try all possible combinations of passwords up to the specified max_length.
    for length in range(1, max_length + 1):
        # Generate all combinations of the given character set for the current length.
        for guess in itertools.product(charset, repeat=length):
            # Combine the characters into a single string.
            guess_password = ''.join(guess)
            # Check if the generated password matches the target password.
            if guess_password == target_password:
                # Record the end time when the password is cracked.
                end_time = time.time()
                print(f"Password cracked! The password is: {guess_password}")
                print(f"Time taken: {end_time - start_time} seconds")
                return guess_password  # Return the cracked password.
            # Print progress for every 1000th attempt to track the process.
            if len(guess_password) % 1000 == 0:
                print(f"Trying password: {guess_password}")

    # If the password is not found within the given constraints, print a message and return None.
    print("Password not found. Try increasing the max length or using a larger charset.")
    return None


def main():
    # Prompt the user to input the target password to be cracked.
    target_password = str(input('Insert the password you want to crack: '))
    # Character set for password generation.
    charset = string.ascii_lowercase + string.digits
    max_length = 6  # Maximum length of passwords to try.

    # Attempt to crack the password using the brute force attack function.
    cracked_password = brute_force_attack(target_password, charset, max_length)
    if cracked_password:
        print(f"Cracked password: {cracked_password}")
    else:
        print("Failed to crack the password.")


if __name__ == "__main__":
    # Execute the main function if the script is run as the main program.
    main()


# Imports:

# itertools: Provides tools for creating iterators for efficient looping.
# string: Provides access to common string constants like ascii_lowercase and digits.
# time: Used to measure the time taken to crack the password.
# brute_force_attack Function:

# Parameters:
# target_password: The password that the function attempts to crack.
# charset: The set of characters used to generate password guesses(defaults to lowercase letters and digits).
# max_length: The maximum length of passwords to try .
# Process:
# Iterates over all possible combinations of the specified character set for lengths from 1 to max_length.
# Uses itertools.product to generate combinations of characters for each length.
# Checks if the generated password matches the target password.
# If a match is found, it prints the cracked password and the time taken, then returns the password.
# If the password is not found, it suggests increasing the length or character set.
# main Function:

# Prompts the user to input a target password.
# Defines the character set and maximum length for the brute force attack.
# Calls the brute_force_attack function with these parameters.
# Prints the result of the attack, indicating whether the password was cracked or not .
# Execution:

# The script is designed to run the main function if executed as the main module, making it suitable for standalone execution.
