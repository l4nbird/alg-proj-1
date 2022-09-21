# Created by Erik Stinnett

import math
import random


# Fermat's Little Theorem: If n = prime integer and a = positive integer less than n, then
# a^n % n == a mod n (ex. n = 5, then a E [1,2,3,4])
# same as: a^(n-1) = 1

# ex: n = 2
#     a = 1
#     1^(2-1) = 1


# 1) Generate n
# 2) Generate a (a E [1, n-1])
# 3) Test if n is prime (a^n % n = a)
# 4) if YES, save n as p or q (Return true)
# 5) if no, return false (repeat algorithm, new int)

p = 0   # First prime number

def get_prime_number():
    min = 2
    #infinity = math.inf

    test = False

    n = random.randint(min, 100)   # Generate n between 2 and infinity : Check if infinity is necessary!!!  1,000,000 to 10,000,000
                                    # check only 20 times? pseudoprime
    a = random.randint(2, (n-1))        # Generate 1 < a < n
    
    for i in range(1, n):
        if (a**n) % n != a:
            test = False

        if test == False:
            print("Not prime")
        else:
            print("Prime")
    print("n = " + str(n) + " a = " + str(a))
    return n
get_prime_number()
