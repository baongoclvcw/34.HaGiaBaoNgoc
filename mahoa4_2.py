def mahoa_thaythe(plaintext, k):
    ciphertext = ""
    k = k % 26

    for char in plaintext:
        if char.isalpha(): 
            base = ord('A') if char.isupper() else ord('a')
            p = ord(char) - base
            c = (p + k) % 26
            ciphertext += chr(c + base)
        else:
            ciphertext += char
    return ciphertext


if __name__ == "__main__":
    plaintext = "HaGiaBaoNgoc"
    k = 34
    ciphertext = mahoa_thaythe(plaintext, k)
    print("Plaintext:", plaintext)
    print("Ciphertext:", ciphertext)
