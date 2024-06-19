p = 31
alpha = 3
beta = 6
x = 10

# Signatur 1
gamma1 = 17
delta1 = 5

# Sigantur 2
gamma2 = 13
delta2 = 15

# Aufgabe a) Sind beide Signaturen gültig ?

s1 = (beta**gamma1) * (gamma1**delta1) % p
print(s1)
print((alpha**x)%p)

s2 = (beta**gamma2) * (gamma2**delta2) % p
print(s2)
print((alpha**x)%p)