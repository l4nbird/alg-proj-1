# from primegenerator import *
from proj1_keygen import *
from primegenerator import *
from Fast_Expo_encrypt_decrypt import *
from signature import *

# gather prime numbers p and q
primeNumList, a_list = get_numbers()
prime = test_prime_number()
p, q = get_p_and_q()

# calculate other necessary numbers and both RSA keys
n = p * q
e = getPublicKey(p, q)
phi = (p-1)*(q-1)
d = getPrivateKey(phi, e)

# Initialize other info
signature = []
sig_msg = []
enc_msg = []


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
    print("Bye for now!")
