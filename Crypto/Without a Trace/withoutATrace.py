from Crypto.Util.number import *

a = 2000128101369
b1 = 2504408575853
b2 = 2440285994541
b3 = 2426159182680
b4 = 2163980646766
b5 = 2465934208374

plain = b""
plain = long_to_bytes(b1 - a) + long_to_bytes(b2 - a) + long_to_bytes(b3 - a) + long_to_bytes(b4 - a) + long_to_bytes(b5 - a)

print(plain)