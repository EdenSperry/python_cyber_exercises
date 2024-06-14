import re


def check_password_strength(password):
    # Checking the length of the password
    if len(password) < 8:
        return "Password too short. It must be at least 8 characters long."

    # Checking for the presence of uppercase, lowercase, digits, and special characters
    if (re.search(r'[A-Z]', password) and re.search(r'[a-z]', password) and
            re.search(r'\d', password) and re.search(r'\W', password)):
        return "Strong password."
    else:
        return "Weak password. Ensure it has uppercase, lowercase, digits, and special characters."


def main():
    # Example usage
    password = input("Enter your password to check its strength: ")
    print(check_password_strength(password))


if __name__ == "__main__":
    main()
