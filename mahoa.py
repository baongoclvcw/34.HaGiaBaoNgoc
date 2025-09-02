
def ma_hoa_caesar(ten, k):
    ket_qua = ""
    k = k % 26 

    for ky_tu in ten:
        if ky_tu.isalpha(): 
            base = ord('A') if ky_tu.isupper() else ord('a')  
            ket_qua += chr((ord(ky_tu) - base + k) % 26 + base)
        else:
            ket_qua += ky_tu  
    return ket_qua


plaintext = "HaGiaBaoNgoc"
k = 34
ciphertext = ma_hoa_caesar(plaintext, k)
print("Plaintext:", plaintext)
print("Ciphertext:", ciphertext)
