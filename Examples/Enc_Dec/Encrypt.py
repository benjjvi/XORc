import xorc

data = "Secret Message! Shh..."
encrypted, key = xorc.XORc(data=data, mode="encrypt", key=False) #key=False means generate a key for me.

print(f"Data Output: {encrypted}")
print(f"XOR Key: {key}")