''' This program creates a encrypted file out of any file you input into it.The method used is caesar cipher where you shift each letter by 3 letters'''

import string

def caesar_cipher():
    L1 = string.ascii_lowercase
    L1 = list(L1)
    d = {}
    for i in range(len(L1)):
        d[L1[i]] = L1[(i+3)%26]
    return d
f = open('input.txt', 'r')
g = open('encrypted_input.txt', 'w')

d = caesar_cipher()
c = f.read(1)
while (c != ''):
    g.write(d[c])
    c = f.read(1)


f.close()
g.close()

k = open('encrypted_input.txt', 'r') 
o = k.read()
print(o)
k.close()

    
