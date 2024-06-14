import re


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
    main()
