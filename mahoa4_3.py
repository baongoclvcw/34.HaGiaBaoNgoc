def rsa_encrypt(plaintext, p, q, e):
    n = p * q
    phi_n = (p - 1) * (q - 1)

    plaintext_numbers = [ord(char.lower()) - ord('a') for char in plaintext if char.isalpha()]
    ciphertext = [pow(p, e, n) for p in plaintext_numbers]
    return ciphertext, n, e
if __name__ == "__main__":
    p = 17  
    q = 23 
    e = 5   
    
    plaintext = "HaGiaBaoNgoc"
    ciphertext, n, e = rsa_encrypt(plaintext, p, q, e)
    
    print(f"Plaintext: {plaintext}")
    print(f"Ciphertext: {ciphertext}")
    print(f"Public Key (n, e): ({n}, {e})")
