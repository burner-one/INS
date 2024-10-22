import math  

def gcd(a, h):
    while True:
        temp = a % h
        if temp == 0:
            return h
        a = h
        h = temp

# Define prime numbers
p = 3  
q = 7  
n = p * q  

# Initialize e
e = 2  
phi = (p - 1) * (q - 1)  

# Find e that is co-prime to phi
while e < phi:
    if gcd(e, phi) == 1:
        break
    else:
        e += 1

# Calculate private key (d)
k = 2  
d = (1 + (k * phi)) / e  

# Message to be encrypted
msg = 12.0  
print("Message data =", msg)  

# Encryption: c = (msg ^ e) % n
c = pow(msg, e)  
c = math.fmod(c, n)  
print("Encrypted data =", c)  

# Decryption: m = (c ^ d) % n
m = pow(c, d)  
m = math.fmod(m, n)  
print("Original message sent =", m)  
