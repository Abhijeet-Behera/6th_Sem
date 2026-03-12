#Vigener cipher
def prepare_text(text):
    return "".join(text.split()).upper()

def generate_key(plaintext, keyword):
    keyword = keyword.upper()
    key = (keyword * (len(plaintext) // len(keyword) + 1))[:len(plaintext)]
    return key

def encrypt(plaintext, key):
    ciphertext = []
    for p, k in zip(plaintext, key):
        char_code = (ord(p) + ord(k) - 2 * ord('A')) % 26
        ciphertext.append(chr(char_code + ord('A')))
    return "".join(ciphertext)

def decrypt(ciphertext, key):
    plaintext = []
    for c, k in zip(ciphertext, key):
        char_code = (ord(c) - ord(k) + 26) % 26
        plaintext.append(chr(char_code + ord('A')))
    return "".join(plaintext)


message = "ATTACK AT DAWN"
keyword = "KEY"


clean_msg = prepare_text(message)
key = generate_key(clean_msg, keyword)
cipher = encrypt(clean_msg, key)
original = decrypt(cipher, key)

print(f"Original:   {clean_msg}")
print(f"Key used:   {key}")
print(f"Ciphertext: {cipher}")
print(f"Decrypted:  {original}")

#OUTPUT:
#Original:   ATTACKATDAWN
#Key used:   KEYKEYKEYKEY
#Ciphertext: KXRKGIKXBKAL
#Decrypted:  ATTACKATDAWN
