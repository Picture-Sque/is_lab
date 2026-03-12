text = input("Enter text: ").upper()
key = input("Enter key: ").upper()

cipher = ""
for i in range(len(text)):
    if text[i].isalpha():
        p = ord(text[i]) - 65
        k = ord(key[i % len(key)]) - 65
        cipher += chr((p + k) % 26 + 65)
    else:
        cipher += text[i]

print("Encrypted:", cipher)

plain = ""
for i in range(len(cipher)):
    if cipher[i].isalpha():
        c = ord(cipher[i]) - 65
        k = ord(key[i % len(key)]) - 65
        plain += chr((c - k) % 26 + 65)
    else:
        plain += cipher[i]

print("Decrypted:", plain)