p = 11
q = 13
d = 103


#öffentlichen Schlüsselparameter
n = 143
e = 7

# wir wollen die RSA-Signatur für die Nachricht x=6 fälschen
# wir haben Zugriff auf ein Orakel, das zwei beliebige gewählte Nachrichten mit RSA signiert

# wir wählen zwei Nachrichten x1 und x2
m1 = 2
m2 = 3

# Simulieren jetzt die Signaturen für die Nachrichten

# x1 Signatur
s1 = (m1**d) % n

# x2 Signatur
s2 = (m2**d) % n

# jetzt führen wir eine known-message attack (bzw. existentielle Fälschung durch)
m = (m1 * m2) % n
s = (s1 * s2) % n

# Verifikation, ob jetzt die gefälschte Signatur richtig ist
print((m % n)==(s**e) % n)


