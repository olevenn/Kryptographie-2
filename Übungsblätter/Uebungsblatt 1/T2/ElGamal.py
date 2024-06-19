from sympy import mod_inverse

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

s1 = (beta ** gamma1) * (gamma1 ** delta1) % p
print(s1)
print((alpha ** x) % p)

s2 = (beta ** gamma2) * (gamma2 ** delta2) % p
print(s2)
print((alpha ** x) % p)

# wir schreiben zwei Schleifen für r und a und testen alle Kombinationen, damit finden wir die Anzahl der gültigen
# Signaturen heraus
count = 0
for r in range(p):
    gamma = (alpha ** r) % p
    for a in range(p-1):
        try:
            # Berechnung des modularen Inversen von r modulo 28
            rinverse = mod_inverse(r, p-1)
            # Berechnung von delta
            delta = ((x - (a * gamma)) * rinverse) % p-1
            # Überprüfung der Gleichung
            if ((beta ** gamma) * (gamma ** delta)) % p == (alpha ** x) % p:
                count += 1
                print(f"gamma: {gamma}, delta: {delta}")
        except ValueError:
            # Wenn kein modulares Inverses existiert, einfach überspringen
            continue

print(count)