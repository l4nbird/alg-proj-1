# Created by Erik Stinnett

import math
import random
from tkinter import N


# Fermat's Little Theorem: If n = prime integer and a = positive integer less than n, then
# a^n % n == a mod n (ex. n = 5, then a E [1,2,3,4])
# same as: a^(n-1) = 1

# 1) Generate n
# 2) Generate a (a E [1, n-1])
# 3) Test if n is prime (a ** (n-1)) % n != 1
# 4) if YES, save n as p or q (Return true)
# 5) if no, return false (repeat algorithm, new int)

def get_prime_number():
    min = 21
    #infinity = math.inf

    test = True

    n = random.randint(min, 100)   # Generate n between 2 and infinity : Check if infinity is necessary!!!  1,000,000 to 10,000,000
                                    # check only 20 times? pseudoprime
    a = random.randint(2, (n-1))        # Generate 1 < a < n
    
    print("n = " + str(n) + " a = " + str(a))

    if (n % 2 == 0):
        return(get_prime_number())
    else:
        for i in range(1, 3):
            if (a ** (n-1)) % n != 1:   # If != 1, then NOT prime
                test = False
                break
        if test == False:
            print("Not prime")
            return(get_prime_number())
        else:
            print("prime")
            primeNumber = n
            return primeNumber
        

#primeNumber = get_prime_number()
#p = primeNumber
#print("p = " + str(p))
