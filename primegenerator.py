# Created by Erik Stinnett

import math
import random
from tkinter import N
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


def test_prime_number(primeNumList, a_list):
    prime = []
    for (a, b) in zip(a_list, primeNumList):                # Fermat's primality test
        if pow(a, b-1, b) == 1:   # If != 1, then NOT prime
            prime.append(b)
    print("PRIME LIST")
    [print(i) for i in prime] 
    return prime


def get_p_and_q(prime):      # Get p and q from prime list
    p = prime.pop()
    q = prime.pop()

    return p, q


#def call_prime_functions():
    #get_numbers()
   # test_prime_number()
   # get_p_and_q()


primeNumList, a_list = get_numbers()
prime = test_prime_number(primeNumList, a_list)
p, q = get_p_and_q(prime)
#print("p: " + str(p) + " q: " + str(q))


#[print(i) for i in primeNumList]  
#print("A follows: ")
#[print(i) for i in a_list] 