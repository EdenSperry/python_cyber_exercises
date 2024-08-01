import re  # Import the regular expression module to use for pattern matching.


def validate_email(email):
    # Regular expression for validating an Email
    regex = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'

    # If the string matches the regex, it is a valid email
    if re.match(regex, email):
        return True
    else:
        return False


def main():
    # Input from the user
    email = input("Enter the email address to validate: ")

    # Validate the email and provide feedback
    if validate_email(email):
        print("The email address is valid.")
    else:
        print("Invalid email address. Please ensure it follows the correct format.")


if __name__ == "__main__":
    # Execute the main function if the script is run as the main program.
    main()

# Regular Expressions(re):

# Regular expressions are used to define patterns for matching strings. In this case, it is used to check the format of email addresses.
# re.match(pattern, string) checks if the string matches the pattern from the start and returns a match object if it matches or None if it doesn’t.
# Email Validation Regex:

# The regex pattern used is r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'.
# ^[a-zA-Z0-9_.+-]+: Ensures the email starts with one or more alphanumeric characters, underscores, dots, pluses, or hyphens.
# @[a-zA-Z0-9-]+: Ensures the presence of an @ symbol followed by one or more alphanumeric characters or hyphens (domain name).
# \.[a-zA-Z0-9-.]+$: Ensures a period . followed by one or more alphanumeric characters, dots, or hyphens (top-level domain).
# validate_email Function:

# Takes an email address as input and uses the regular expression to determine if the email is valid.
# Returns True if the email matches the pattern, otherwise returns False.
# main Function:

# Prompts the user to enter an email address.
# Uses the validate_email function to check the email format.
# Prints whether the email is valid or invalid based on the function's result.
# Execution:

# The script runs the main function if it is executed as the main program, making it interactive for the user.
