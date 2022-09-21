import math
import random

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
def getPrivateKey(e, phi):
    d = extended_gcd(e, phi)
    (x, y, gcd) = d
    key = x % phi 
    return key