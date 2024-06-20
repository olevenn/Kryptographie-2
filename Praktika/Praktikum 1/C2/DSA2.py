from hashlib import sha256
import sympy
from sympy import mod_inverse
from random import randint


def generateDSAKeys():
    p = q = 0

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

    return p, q, alpha, a, beta


def createSignature(r, q, alpha, p, hashMessage, a):
    # gamma and delta
    gamma = pow(alpha, r, p) % q
    delta = ((hashMessage + (a * gamma)) * mod_inverse(r, q)) % q
    return gamma, delta


def verifiacation(hashMessage, delta, q, gamma, alpha, beta, p):
    e1 = hashMessage * mod_inverse(delta, q) % q
    e2 = gamma * mod_inverse(delta, q) % q
    return ((pow(alpha, e1, p) * pow(beta, e2, p)) % p) % q == gamma


# Create First Signature
m1 = 123
h1 = sha256(m1.to_bytes(m1.bit_length(), 'big'))
h1 = int.from_bytes(h1.digest(), 'big')
p, q, alpha, a, beta = generateDSAKeys()
print(f'p: {p}\nq: {q}\nalpha: {alpha}\na: {a}\nbeta: {beta}')
gamma1, delta1 = createSignature(10, q, alpha, p, h1, a)
print(f'gamma1: {gamma1}\ndelta1: {delta1}\n')
print("\n\n\n")

# create second Signature
m2 = 234
h2 = sha256(m2.to_bytes(m2.bit_length(), 'big'))
h2 = int.from_bytes(h2.digest(), 'big')
gamma2, delta2 = createSignature(10, q, alpha, p, h2, a)
print(f'gamma2: {gamma2}\ndelta2: {delta2}\n')

delta2_ = mod_inverse(delta2, q)
delta1_ = mod_inverse(delta1, q)
gamma1_ = mod_inverse(gamma1, q)

# Calculate a
a = ((((((h2 * delta2_) - (h1 * delta1_)) * gamma1_) * (mod_inverse(delta1_ - delta2_, q)))%q) == a)

print(a)