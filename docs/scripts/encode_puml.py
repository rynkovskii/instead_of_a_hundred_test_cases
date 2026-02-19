import sys, zlib, base64

data = sys.stdin.read().encode("utf-8")
compressed = zlib.compress(data)[2:-4]
alphabet = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz-_"

def encode(data):
    res = ""
    for i in range(0, len(data), 3):
        b = data[i:i+3]
        b += b'\0' * (3 - len(b))
        n = b[0] << 16 | b[1] << 8 | b[2]
        res += alphabet[(n >> 18) & 63]
        res += alphabet[(n >> 12) & 63]
        res += alphabet[(n >> 6) & 63]
        res += alphabet[n & 63]
    return res

print(encode(compressed))
