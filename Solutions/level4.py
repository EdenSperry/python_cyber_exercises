def encrypt(text, shift):
    result = ""  # Initialize an empty string to store the encrypted result.

    # Iterate over each character in the input text.
    for i in range(len(text)):
        char = text[i]

        # Check if the character is an alphabetic letter.
        if char.isalpha():
            # Shift the character by the specified amount.
            stay_in_alphabet = ord(char) + shift

            # Handle lowercase letters.
            if char.islower():
                # Calculate the new character position within the lowercase alphabet and wrap around using modulo.
                stay_in_alphabet = (stay_in_alphabet - 97) % 26 + 97

            # Handle uppercase letters.
            else:
                # Calculate the new character position within the uppercase alphabet and wrap around using modulo.
                stay_in_alphabet = (stay_in_alphabet - 65) % 26 + 65

            # Convert the shifted character code back to a character and append it to the result.
            result += chr(stay_in_alphabet)

        # If the character is not alphabetic, leave it unchanged and append it to the result.
        else:
            result += char

    return result  # Return the final encrypted string.


def decrypt(text, shift):
    # Decrypt the text by using the encrypt function with a negative shift.
    return encrypt(text, -shift)


def main():
    # Example usage of the encrypt and decrypt functions.
    # Prompt the user to enter the text to encrypt.
    text = input("Enter the text: ")
    # Prompt the user to enter the shift amount.
    shift = int(input("Enter the shift number: "))

    # Encrypt the input text using the specified shift.
    encrypted = encrypt(text, shift)
    print("Encrypted: " + encrypted)  # Display the encrypted text.

    # Decrypt the encrypted text to verify correctness.
    decrypted = decrypt(encrypted, shift)
    # Display the decrypted text to ensure it matches the original.
    print("Decrypted: " + decrypted)


if __name__ == "__main__":
    # Call the main function if this script is executed as the main program.
    main()


# Explanation
# Encrypt Function: This function takes a text string and a shift value to produce an encrypted version of the text using a Caesar cipher, which shifts each alphabetic character by the specified amount. Non-alphabetic characters remain unchanged.
# Decrypt Function: This function reverses the encryption by calling the encrypt function with a negative shift, effectively shifting characters back to their original positions.
# Main Function: The main function demonstrates how to use the encrypt and decrypt functions. It collects input from the user, performs encryption, and then decrypts to verify the result.

# Important Points
# The use of modulo ( % ) ensures that the shifting wraps around the alphabet, so after 'z', it continues from 'a'.
# The ord() function is used to convert a character to its ASCII numeric value, and chr() converts back from an ASCII value to a character.
# The script only encrypts alphabetic characters, leaving other characters like spaces and punctuation unchanged.
