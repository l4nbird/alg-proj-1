# from primegenerator import *
from proj1_keygen import *
from primegenerator import *

primeNumber = -1
p = -1
q = -1

primeNumber = get_prime_number()
p = primeNumber
primeNumber = get_prime_number()
q = primeNumber

print("p = " + str(p) + " q = " + str(q))

msg = 12

if p == q:
  print('nah')
else:
  # print(str(p) + ' ' + str(q))
  e = getPublicKey(p, q)
  phi = (p-1)*(q-1)
  t = getPrivateKey(e, phi)

  print('Public Key: ' + str(e) + ' Private Key: ' + str(t))


