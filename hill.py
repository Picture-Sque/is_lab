key = [[17, 17, 5], [21, 18, 21], [2, 2, 19]]

# Determine the size of the key matrix (n x n)
n = len(key)

text = input("Enter text: ").upper()

# If length is not a multiple of n, add 'X'
while len(text) % n != 0:
    text += 'X'

cipher = ""

# Process text in blocks of n
for i in range(0, len(text), n):
    # Extract n characters and convert to 0-25
    block = [ord(text[i+j]) - 65 for j in range(n)]
    
    # Multiply n x n matrix with the n x 1 column vector
    for row in range(n):
        c_val = sum(key[row][k] * block[k] for k in range(n)) % 26
        cipher += chr(c_val + 65)

print("Cipher Text:", cipher)