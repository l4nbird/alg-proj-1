# Shelley Wieburg
# Algorithms 3330
# Project 1
# Uses fast exponentiation algorithm to encrypt and decrypt a message, encodes & decodes
# strings, and converts ascii back to characters


# encrypts or decrypts a message recursively using fast exponentiation
# from Algorithms lecture slides
def crypt_fastExpo(input, key, n):
    if key == 0:
        return 1
    if key%2 == 0:
        t = crypt_fastExpo(input, key//2, n)
        return(t*t)%n
    else:
        t = crypt_fastExpo(input, key//2, n)
        return input *(t**2%n)%n
    # OR just return pow(input, key, n)


# Takes a string input, breaks it into a list, and encodes each list item in ascii
# It then passes that list to crypt_fastExpo with key e and returns the result
def encode_str(str, e, n):
    strlist = list(str.encode('ascii'))
    encodedstr = list()
    for i in strlist:
        encodedstr.append(crypt_fastExpo(i, e, n))
    return encodedstr


# Takes the encrypted message c, breaks it into a list, and passes each item through
# crypt_fastExpo with key d and returns the decoded list
# c represents coded message, d represents a specific key (public/private?)
# n is the modulus (mod n)
def decode_str(c, d, n):
    decodelist = list()
    for i in c:
        decodelist.append(crypt_fastExpo(i, d, n))
    return decodelist


# Takes the result of decode_str and adds it to a character array, converting each item
# into a character ascii, then returns the resulting array
def to_char(in_ascii):
    char_arr = []
    for single in in_ascii:
        char_arr.append(chr(single))
    return char_arr


