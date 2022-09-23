# from primegenerator import *
from proj1_keygen import *
from primegenerator import *
from Fast_Expo_encrypt_decrypt import *


primeNumList, a_list = get_numbers()
prime = test_prime_number()
p, q = get_p_and_q()

print("p = " + str(p) + " " + "q = " + str(q))

msg = 'gonna ad hominem my ancestors, periodt'

if p == q:
  print('nah')
else:
  # print(str(p) + ' ' + str(q))
  e = getPublicKey(p, q)
  n = p*q
  phi = (p-1)*(q-1)
  t = getPrivateKey(phi, e)

  enc_msg = encode_str(msg, e, n)
  print('Encoded Message: ' + str(enc_msg))
  dec_msg = decode_str(enc_msg, t, n)
  end_msg = to_char(dec_msg)
  print('Decoded Message: ' + str(end_msg))

  print('Public Key: ' + str(e) + ' Private Key: ' + str(t))


