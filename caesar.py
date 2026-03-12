def encrypt(text, shift):
    result = ""

    for char in text:
        if char.isalpha():
            if char.isupper():
                result += chr((ord(char) + shift - 65) % 26 + 65)
            else:
                result += chr((ord(char) + shift - 97) % 26 + 97)
        else:
            result += char

    return result


def decrypt(text, shift):
    return encrypt(text, -shift)


# Main Program
message = input("Enter message: ")
shift = int(input("Enter shift value: "))

encrypted = encrypt(message, shift)
print("Encrypted message:", encrypted)

decrypted = decrypt(encrypted, shift)
print("Decrypted message:", decrypted)