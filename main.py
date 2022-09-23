# from primegenerator import *
from proj1_keygen import *
from primegenerator import *
from Fast_Expo_encrypt_decrypt import *

# gather prime numbers p and q
primeNumList, a_list = get_numbers()
prime = test_prime_number(a_list, primeNumList)
p, q = get_p_and_q(prime)

# calculate other necessary numbers and both RSA keys
n = p * q
e = getPublicKey(p, q)
phi = (p-1)*(q-1)
d = getPrivateKey(phi, e)

# Initialize other info
signature = None
sig_msg = None
enc_msg = None


print('RSA keys have been generated.')

# Loop to ask what type of user the user is, sends them to proper area, 3 exits program
loop = True
while loop == True:
  print('Please select your user type: ')
  print('     1. A public user\n     2. The owner of the keys\n     3. Exit program')
  selection = input()

  if selection == '1':
    enc_msg = public_user(e, n, signature, sig_msg)
  elif selection == '2':
    signature, sig_msg = owner(n, d, enc_msg)
  elif selection == '3':
    loop = False





# print("p = " + str(p) + " " + "q = " + str(q))

# msg = 'gonna ad hominem my ancestors, periodt'

# if p == q:
#   print('nah')
# else:
#   # print(str(p) + ' ' + str(q))
#   e = getPublicKey(p, q)
#   n = p*q
#   phi = (p-1)*(q-1)
#   t = getPrivateKey(phi, e)

#   enc_msg = encode_str(msg, e, n)
#   print('Encoded Message: ' + str(enc_msg))
#   dec_msg = decode_str(enc_msg, t, n)
#   end_msg = to_char(dec_msg)
#   print('Decoded Message: ' + str(end_msg))

#   print('Public Key: ' + str(e) + ' Private Key: ' + str(t))


