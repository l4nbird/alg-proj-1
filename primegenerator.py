# Created by Erik Stinnett

import math
import random
from tkinter import N
import unittest
from webbrowser import get


# Fermat's Little Theorem: If n = prime integer and a = positive integer less than n, then
# a^n % n == a mod n (ex. n = 5, then a E [1,2,3,4])
# same as: a^(n-1) = 1

# 1) Generate n
# 2) Generate a (a E [1, n-1])
# 3) Test if n is prime (a ** (n-1)) % n != 1
# 4) if YES, save n as p or q (Return true)
# 5) if no, return false (repeat algorithm, new int)


# A function to generate a list of 20 potential prime numbers and 20 A's
def get_numbers():  # n = 1,000,000

    x = 1000000
    # List initializing
    primeNumList = []           
    a_list = []
    n = random.randint(x, 10*x) # Get random integer between 1,000,000 and 10n


    while len(primeNumList) < 40:
        if (n % 2) != 0 and (n % 3) != 0 and (n % 5) != 0:  # Quickens the process, removes known factors 
            primeNumList.append(n)                          # If it passes the parameters, add it to the primeNumList
            a = random.randint(2, n-1)                      # generates a
            a_list.append(a)
            n = random.randint(x, 10*x)                     # Generate new rand int

        else:
            n = random.randint(x, 10*x)                     # Generate new rand int

    return primeNumList, a_list


def test_prime_number():
    prime = []
    for (a, b) in zip(a_list, primeNumList):                # Fermat's primality test
        if pow(a, b-1, b) == 1:   # If != 1, then NOT prime
            prime.append(b)
    print("PRIME LIST")
    [print(i) for i in prime] 
    return prime


def get_p_and_q():      # Get p and q from prime list
    p = prime.pop()
    q = prime.pop()

    return p, q


primeNumList, a_list = get_numbers()
prime = test_prime_number()
p, q = get_p_and_q()

class TestPrimeGenerator(unittest.TestCase):
    def setUp(self):
        self.testPrimeNumList = (1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40)
        self.testA_List = (1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40)
    
    def test_list_lengths(self):
        resultN, resultA = get_numbers()
        expectedNList = self.testPrimeNumList
        expectedAList = self.testA_List
        self.assertEqual(len(resultN), len(expectedNList), "List size incorrect! Should equal 40")
        self.assertEqual(len(resultA), len(expectedAList), "List size incorrect! Should equal 40")

    def test_prime_numbers(self):
        primeList = test_prime_number()
        self.assertGreaterEqual(len(primeList), 2, "ERROR: Prime List not long enough")

    def test_p_and_q(self):
        resultP, resultQ = get_p_and_q()

        self.assertIsNotNone(resultP)
        self.assertIsNotNone(resultQ)