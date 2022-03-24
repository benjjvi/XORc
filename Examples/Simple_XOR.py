import xcrypt

data = "Secret Message! Shh..."
data, key = xcrypt.Modules._XCRYPT(data=data, mode="encrypt", key=False) #key=False means generate a key for me.

print(f"Data Output: {data}")
print(f"XOR Key: {key}")

unencrypted, key = xcrypt.Modules._XCRYPT(data=data, mode="decrypt", key=key)
print(f"Unencrypted Data Output: {unencrypted}")
print(f"XOR Key: {key}")