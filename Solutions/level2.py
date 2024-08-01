import re  # Import the regular expression module to use for pattern matching.


def check_password_strength(password):
    # Checking the length of the password
    if len(password) < 8:
        return "Password too short. It must be at least 8 characters long."

    # Checking for the presence of uppercase, lowercase, digits, and special characters
    if (re.search(r'[A-Z]', password) and  # Check for at least one uppercase letter.
            # Check for at least one lowercase letter.
            re.search(r'[a-z]', password) and
            re.search(r'\d', password) and  # Check for at least one digit.
            # Check for at least one special character.
            re.search(r'\W', password)):
        return "Strong password."
    else:
        # If any of the above checks fail, return a message indicating the password is weak.
        return "Weak password. Ensure it has uppercase, lowercase, digits, and special characters."


def main():
    # Example usage
    password = input("Enter your password to check its strength: ")
    print(check_password_strength(password))


if __name__ == "__main__":
    # Execute the main function if the script is run as the main program.
    main()


# Regular Expressions(re):

# Regular expressions are used to match patterns within the password string.
# re.search(pattern, string) scans through the string and returns a match object if the pattern is found, otherwise returns None.
# check_password_strength Function:

# Length Check:
# The password must be at least 8 characters long. If not , it returns a message indicating that the password is too short.
# Character Type Checks:
# Uses regular expressions to check for the presence of at least one uppercase letter([A-Z]), one lowercase letter([a-z]), one digit(\d), and one special character (\W).
# If all these conditions are met, the function returns "Strong password."
# If any of these conditions are not met, the function returns "Weak password." with a suggestion to improve it.
# main Function:

# Prompts the user to enter a password to check its strength.
# Calls the check_password_strength function and prints the result.
# Execution:

# The script runs the main function if it is executed as the main program, making it easy to use in a standalone fashion.
