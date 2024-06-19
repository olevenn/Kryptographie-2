from sympy import mod_inverse

p = 59
q = 29
alpha = 3
a = 7  # privater Schlüsselparameter
beta = alpha ** a % p

hashm1 = 26
r = 10

rmodinverse = mod_inverse(r, q)

gamma1 = (alpha ** r % p) % q
delta1 = (hashm1 + a * gamma1) * rmodinverse % q

print("Signatur 1 von der Nachricht: " + str(hashm1) + " ist die Signatur " + str(gamma1) + " und " + str(delta1))

# jetzt erstellen wir eine weiter Signatur mit einer neuen Nachricht aber demselben r

hashm2 = 24

gamma2 = (alpha ** r % p) % q
delta2 = (hashm2 + a * gamma2) * rmodinverse % q

print("Signatur 1 von der Nachricht: " + str(hashm2) + " ist die Signatur " + str(gamma2) + " und " + str(delta2))


def find_r(base, mod1, mod2, target):
    for r in range(mod1):
        if (pow(base, r, mod1) % mod2) == target:
            return r
    return None

base = 3
mod1 = 59
mod2 = 29
target = 20

r = find_r(base, mod1, mod2, target)

print(r)
