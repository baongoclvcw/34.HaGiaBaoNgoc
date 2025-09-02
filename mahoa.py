def caesar_encrypt(text, k):
    result = ""
    k = k % 26  

    for char in text:
        if char.isalpha():
            base = ord('A') if char.isupper() else ord('a')
            result += chr((ord(char) - base + k) % 26 + base)
        else:
            result += char
    return result


if __name__ == "__main__":
    plaintext = "HaGiaBaoNgoc"
    k = 34
    ciphertext = caesar_encrypt(plaintext, k)
    print("Plaintext:", plaintext)
    print("Ciphertext:", ciphertext)
