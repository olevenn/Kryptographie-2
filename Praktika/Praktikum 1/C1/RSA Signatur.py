from random import randint
from sympy import mod_inverse

import sympy


def is_prime(num, test_count):
    if num == 1:
        return False
    if test_count >= num:
        test_count = num - 1
    for x in range(test_count):
        val = randint(1, num - 1)
        if pow(val, num - 1, num) != 1:
            return False
    return True


def generate_big_prime(n):
    found_prime = False
    while not found_prime:
        p = randint(2 ** (n - 1), 2 ** n)
        if is_prime(p, 1000):
            return p


def finde_teilerfremde_zahl():
    teilerfremde = 0
    for i in range(2, phi - 1):
        if sympy.gcd(phi, i) == 1:
            teilerfremde = i
            break
    return teilerfremde


p = generate_big_prime(1500)
q = generate_big_prime(1500)
n = p * q
phi = (p - 1) * (q - 1)
e = finde_teilerfremde_zahl()
d = mod_inverse(e, phi)
print("p: " + str(p))
print("q: " + str(q))
print("n: " + str(n))
print("phi: " + str(phi))
print("e: " + str(e))
print("d: " + str(d))

m = 20
r = 0
for i in range(p):
    if i ** e % n != 1:
        r = i
        break
ss = ((r ** (e*d)) * (m**d)) % n
s = mod_inverse(r, n) * ss
