# Demonstrate the working of MD5 (byte-byte)
import hashlib  

# Encode 'TYCSSTUDENTS' using MD5 hash function
result = hashlib.md5(b'TYCSSTUDENTS')  

# Print the equivalent byte value
print("The byte equivalent of hash is:", end=" ")
print(result.digest())  

# String to hash
str2hash = "TYCSSTUDENTS"  

# Encoding 'TYCSSTUDENTS' using encode() and sending to MD5
result = hashlib.md5(str2hash.encode())  

# Print the equivalent hexadecimal value
print("The hexadecimal equivalent of hash is:", end=" ")
print(result.hexdigest())  
