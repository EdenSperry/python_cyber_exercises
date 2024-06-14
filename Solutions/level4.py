def encrypt(text, shift):
    result = ""

    for i in range(len(text)):
        char = text[i]
        if char.isalpha():
            stay_in_alphabet = ord(char) + shift
            if char.islower():
                stay_in_alphabet = (stay_in_alphabet - 97) % 26 + 97
            else:
                stay_in_alphabet = (stay_in_alphabet - 65) % 26 + 65
            result += chr(stay_in_alphabet)
        else:
            result += char

    return result


def decrypt(text, shift):
    return encrypt(text, -shift)


def main():
    # Example usage
    text = input("Enter the text: ")
    shift = int(input("Enter the shift number: "))
    encrypted = encrypt(text, shift)
    print("Encrypted: " + encrypted)
    decrypted = decrypt(encrypted, shift)
    print("Decrypted: " + decrypted)


if __name__ == "__main__":
    main()
