# from primegenerator import *
from proj1_keygen import *

# p = get_prime_number()
# q = get_prime_number()
p = 59
q = 61
msg = 12

if p == q:
  print('nah')
else:
  # print(str(p) + ' ' + str(q))
  e = getPublicKey(p, q)
  phi = (p-1)*(q-1)
  t = getPrivateKey(e, phi)

  print('Public Key: ' + str(e) + ' Private Key: ' + str(t))


