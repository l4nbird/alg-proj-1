import math
from operator import truediv
import random
from Fast_Expo_encrypt_decrypt import *

# takes two prime numbers over 1
# finds phi of prime numbers and a relative prime of phi, returns relative prime
def getPublicKey(p, q):
    found = False
    phi = (p-1) * (q-1)

    while found == False:
        # find x using euclid algorithm
        x = attemptKey(phi)

        # test if attempt is a valid key
        if (gcd(x, phi)) == 1 and x != 1:

            print(str(x) + ' ' + str(phi))
            found = True
            return x
        else:
            continue

# sent phi, return random integer between 0 and phi - 1
def attemptKey(phi):
    return random.randint(0, phi - 1)

# euclid's algorithm, taken from lecture notes
# returns gcd of two inputs
def gcd(a, b):
    if a == 0:
        return b
 
    return gcd(b % a, a)

# extended euclid's algorithm, taken from lecture notes
# returns inverse of e in Z_phi
def extended_gcd(a =1, b = 1):
    if b == 0:
        return (1, 0, a)
    (x, y, d) = extended_gcd(b, a%b)
    return y, x - a//b*y, d

# input public key and phi of initial prime numbers
# finds private key d using extended euclid's algorithm
# -- needs to fulfill ed mod phi = 1 --
def getPrivateKey(phi, e):
    d = extended_gcd(e, phi)
    (x, y, gcd) = d
    key = x % phi 
    return key

def public_user(e, n):
    loop = True

    while loop != False:
        print("As a public user, what would you like to do?\n       1. Send an encrypted message\n      2. Authenticate a digital signature")
        print("     3. Exit\n")
        selection = input()

        if selection == 1:
            msg = input("Enter a message: ")
            enc_msg = encode_str(msg, e, n)
            print("Message encrypted and sent.")
        elif selection == 2:
            # authenticate signature
            print("yay")
        elif selection == 3:
            loop = False
    if enc_msg:
        return enc_msg
    else:
        return None

def owner(n, d, msg):
    loop = True

    while loop != False:
        print("As the owner of the keys, what would you like to do?\n       1. Decrypt a received message\n      2. Digitally sign a message")
        print("     3. Exit\n")
        selection = input()

        if selection == 1:
            dec_msg = decode_str(msg, d, n)
            print("Decrypted message: " + to_char(dec_msg))
        elif selection == 2:
            # Digitally sign a message
            signature = input("Enter a message: ")
            #encrypt signature with signature^d mod n
        elif selection == 3:
            loop = False
    if signature:
        return signature
    else: return None