import xorc

#First, generate this data with the functions used in Encrypt.py
data = "00011101001010110010110100111100001010110011101001101110000000110010101100111101001111010010111100101001001010110110111101101110000111010010011000100110011000000110000001100000"
key = "01001110"

unencrypted, key = xorc.XORc(data=data, mode="decrypt", key=key)
print(f"Unencrypted Data Output: {unencrypted}")
print(f"XOR Key: {key}")