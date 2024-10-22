# Diffie-Hellman Code

# Power function to return value of a^b mod P
def power(a, b, p):
    if b == 1:
        return a % p
    else:
        return pow(a, b, p)

# Main function
def main():
    # Both persons agree upon the public keys G and P
    P = 23  # A prime number
    print("The value of P:", P)

    G = 9  # A primitive root for P
    print("The value of G:", G)

    # Alice chooses the private key a
    a = 4  # Alice's private key
    print("The private key a for Alice:", a)

    # Generate the public key for Alice
    x = power(G, a, P)

    # Bob chooses the private key b
    b = 3  # Bob's private key
    print("The private key b for Bob:", b)

    # Generate the public key for Bob
    y = power(G, b, P)

    # Generating the secret key after the exchange of keys
    ka = power(y, a, P)  # Secret key for Alice
    kb = power(x, b, P)  # Secret key for Bob

    print("Secret key for Alice is:", ka)
    print("Secret key for Bob is:", kb)

if __name__ == "__main__":
    main()
