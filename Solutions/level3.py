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
    start_time = time.time()

    # Try all possible combinations up to max_length
    for length in range(1, max_length + 1):
        for guess in itertools.product(charset, repeat=length):
            guess_password = ''.join(guess)
            if guess_password == target_password:
                end_time = time.time()
                print(f"Password cracked! The password is: {guess_password}")
                print(f"Time taken: {end_time - start_time} seconds")
                return guess_password
            if len(guess_password) % 1000 == 0:  # Print progress every 1000 attempts
                print(f"Trying password: {guess_password}")

    print("Password not found. Try increasing the max length or using a larger charset.")
    return None


def main():
    target_password = str(input('Insert the password you want to crack: '))
    charset = string.ascii_lowercase + string.digits  # Character set for password generation
    max_length = 6  # Maximum length of passwords to try

    cracked_password = brute_force_attack(target_password, charset, max_length)
    if cracked_password:
        print(f"Cracked password: {cracked_password}")
    else:
        print("Failed to crack the password.")


if __name__ == "__main__":
    main()
