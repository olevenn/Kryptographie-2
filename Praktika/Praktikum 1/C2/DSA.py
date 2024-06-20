from hashlib import sha256
import sympy
from sympy import mod_inverse
from random import randint

p = q = c = 0

while not sympy.isprime(p):
    c = randint(2 ** 2815, 2 ** 2816)
    q = sympy.randprime(2 ** 255, 2 ** 256)
    p = c * q + 1

e = (p - 1) // q
alpha = 1
while alpha == 1:
    h = randint(1, p - 1)
    alpha = pow(h, e, p)

a = randint(1, q - 1)
beta = pow(alpha, a, p)

print("p: " + str(p))
print("q: " + str(q))
print("alpha: " + str(alpha))
print("a: " + str(a))
print("beta: " + str(beta))

#Create Message
message = 1234
hashMessage = sha256(message.to_bytes(message.bit_length(), 'big'))
hashMessage = int.from_bytes(hashMessage.digest(), 'big')

# r random number
r = randint(1, q - 1)

# gamma and delta
gamma = pow(alpha, r, p) % q
delta = ((hashMessage + (a * gamma)) * mod_inverse(r, q)) % q

e1 = hashMessage * mod_inverse(delta, q) % q
e2 = gamma * mod_inverse(delta, q) % q

# Test
print(((pow(alpha, e1, p) * pow(beta, e2, p)) % p) % q == gamma)
