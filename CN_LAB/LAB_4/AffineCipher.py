#Affine cipher
def prepare_text(text):
    return "".join(text.split()).upper()

def encrypt(plaintext, a, b):
    ciphertext = []
    for p in plaintext:
        p_val = ord(p) - ord('A')
        char_code = (a * p_val + b) % 26
        ciphertext.append(chr(char_code + ord('A')))
    return "".join(ciphertext)

def decrypt(ciphertext, a, b):

    a_inv = 0
    for i in range(26):
        if (a * i) % 26 == 1:
            a_inv = i
            break
    
    plaintext = []
    for c in ciphertext:
        c_val = ord(c) - ord('A')
        char_code = (a_inv * (c_val - b)) % 26
        plaintext.append(chr(char_code + ord('A')))
    return "".join(plaintext)


message = "ATTACK AT DAWN"
key_a = 5 
key_b = 8


clean_msg = prepare_text(message)
cipher = encrypt(clean_msg, key_a, key_b)
original = decrypt(cipher, key_a, key_b)


print(f"Original:   {clean_msg}")
print(f"Keys used:  a={key_a}, b={key_b}")
print(f"Ciphertext: {cipher}")
print(f"Decrypted:  {original}")


#OUTPUT:
#Original:   ATTACKATDAWN
#Keys used:  a=5, b=8
#Ciphertext: IZZISGIZXIOV
#Decrypted:  ATTACKATDAWN
