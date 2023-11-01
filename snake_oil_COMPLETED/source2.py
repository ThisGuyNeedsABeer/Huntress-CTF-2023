# Visit https://www.lddgo.net/en/string/pyc-compile-decompile for more information
# Version : Python 3.9

import io
import sys
import base64

def decrypt(s1, s2):
    return ''.join([chr(ord(c1) ^ ord(c2)) for c1, c2 in zip(s1, s2)])

def deobfuscate():
    part1 = '2ec7627d{galf'[::-1]
    part2 = str(base64.b64decode('NjIwM2I1Y2M2OWY0'.encode('ascii')), 'UTF8')
    part3 = decrypt('\x17*\x07`BC\x14*R@\x14^*', 'uKeVuzwIexplW')
    key = part1 + part2 + part3
    return key

result = deobfuscate()
print(result)