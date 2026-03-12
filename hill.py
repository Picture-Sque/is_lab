key = [[3,3],[2,5]]

text = input("Enter text: ").upper()

# If length is odd add X
if len(text) % 2 != 0:
    text += 'X'

cipher = ""

for i in range(0, len(text), 2):
    a = ord(text[i]) - 65
    b = ord(text[i+1]) - 65

    c1 = (key[0][0]*a + key[0][1]*b) % 26
    c2 = (key[1][0]*a + key[1][1]*b) % 26

    cipher += chr(c1 + 65)
    cipher += chr(c2 + 65)

print("Cipher Text:", cipher)