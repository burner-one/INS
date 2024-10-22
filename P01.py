### P01 A ###
def encrypt(text, s):
    result = ""
    
    # Traverse the text
    for i in range(len(text)):
        char = text[i]
        
        # Encrypt uppercase characters
        if char.isupper():
            result += chr((ord(char) + s - 65) % 26 + 65)
        # Encrypt lowercase characters
        elif char.islower():
            result += chr((ord(char) + s - 97) % 26 + 97)
        else:
            result += char  # Preserve non-alphabetic characters
    
    return result

# Check the above function
text = input("Enter the text to encrypt: ")
s = 3

print("Text: " + text)
print("Cipher: " + encrypt(text, s))

### P01 B ###
# Get input from the user
string = input("Enter a string: ")

def RailFence(txt):
    result = ""
    
    # Append characters at even indices
    for i in range(len(txt)):
        if i % 2 == 0:
            result += txt[i]
    
    # Append characters at odd indices
    for i in range(len(txt)):
        if i % 2 != 0:
            result += txt[i]
    
    return result

# Print the encrypted result
print("Encrypted text:", RailFence(string))
