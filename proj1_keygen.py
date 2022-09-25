import math
from operator import truediv
import random
import unittest
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
    (x, y, d) = extended_gcd(b, a % b)
    return y, x - a//b*y, d

# input public key and phi of initial prime numbers
# finds private key d using extended euclid's algorithm
# -- needs to fulfill ed mod phi = 1 --
def getPrivateKey(phi, e):
    d = extended_gcd(e, phi)
    (x, y, gcd) = d
    key = x % phi 
    return key



# Unittesting for this file
class TestKeyGeneration(unittest.TestCase):
    def testGetPublicKey(self):     # Tests values of X (will be in the range of 0-12)
        phi = 12
        result = getPublicKey(3, 7)
        #expected = random.randint(0, 12)
        self.assertIn(result, range(0, 13))

    def testAttemptKey(self):       # Tests whether the generated key is within an acceptable range with the units given
        result = attemptKey(10)
        expected = range(0, 10)
        self.assertIn(result, expected)
    
    def testGCD(self):              # Tests whether the expected result is equal to 1 
        result = gcd(3, 10)
        expected = 1
        self.assertEqual(result, expected)
