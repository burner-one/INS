# SHA hash algorithms demonstration
import hashlib  

# Initialize the string
text = "TYCSSTUDENT"  

# Function to compute and print SHA hashes
def print_sha_hashes(text):
    # SHA-256
    result = hashlib.sha256(text.encode())
    print("The hexadecimal equivalent of SHA256 is:", result.hexdigest())
    
    # SHA-384
    result = hashlib.sha384(text.encode())
    print("The hexadecimal equivalent of SHA384 is:", result.hexdigest())
    
    # SHA-224
    result = hashlib.sha224(text.encode())
    print("The hexadecimal equivalent of SHA224 is:", result.hexdigest())
    
    # SHA-512
    result = hashlib.sha512(text.encode())
    print("The hexadecimal equivalent of SHA512 is:", result.hexdigest())
    
    # SHA-1
    result = hashlib.sha1(text.encode())
    print("The hexadecimal equivalent of SHA1 is:", result.hexdigest())

# Call the function with the input string
print_sha_hashes(text)
