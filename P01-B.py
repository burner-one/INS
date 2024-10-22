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
