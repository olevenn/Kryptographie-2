from sympy import mod_inverse

hashMessage = 26
r = 10
p = 59
q = 29
alpha = 3
a = 7
beta = 4
gamma = 20
delta = 5

e1 = hashMessage * mod_inverse(delta, q) % q
print("e1: " + str(e1))
e2 = gamma * mod_inverse(delta, q) % q
print("e2: " + str(e2))

print(((alpha ** e1) * (beta ** e2) % p) % q)
print(((pow(alpha, e1, p) * pow(beta, e2, p)) % p) % q == gamma)
