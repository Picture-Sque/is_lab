text = input("Enter text: ").upper()
a = int(input("Enter a: "))
b = int(input("Enter b: "))

# Encryption
enc = ""
for c in text:
    if c.isalpha():
        enc += chr(((a*(ord(c)-65)+b) % 26) + 65)
    else:
        enc += c

print("Encrypted:", enc)

# Find modular inverse of a
for i in range(26):
    if (a*i) % 26 == 1:
        a_inv = i

# Decryption
dec = ""
for c in enc:
    if c.isalpha():
        dec += chr((a_inv*((ord(c)-65)-b) % 26) + 65)
    else:
        dec += c

print("Decrypted:", dec)