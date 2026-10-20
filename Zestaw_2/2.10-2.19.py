# Zad 2.10
line = "jakis \n wielowierszowy \t tekst"
slowa = line.split()
ile = len(slowa)
print("2.10:", ile)

# Zad 2.11
word = "python"
wynik = "_".join(word)
print("2.11:", wynik)

# Zad 2.12
line = "ala ma kota a kot ma ale"
slowa = line.split()
pierwsze = ""
ostatnie = ""
for s in slowa:
    pierwsze = pierwsze + s[0]
    ostatnie = ostatnie + s[-1]
print("2.12 pierwsze:", pierwsze)
print("2.12 ostatnie:", ostatnie)

# Zad 2.13
line = "krotkie zdanie do testu"
slowa = line.split()
dlugosci = []
for s in slowa:
    dlugosci.append(len(s))
suma = sum(dlugosci)
print("2.13:", suma)

# Zad 2.14
line = "szukamy najdluzszego wyrazu w tym tekscie"
slowa = line.split()
najdluzszy = ""
for s in slowa:
    if len(s) > len(najdluzszy):
        najdluzszy = s
print("2.14 najdluzszy:", najdluzszy)
print("2.14 dlugosc:", len(najdluzszy))

# Zad 2.15
L = [1, 23, 45, 6]
wynik = ""
for liczba in L:
    wynik = wynik + str(liczba)
print("2.15:", wynik)

# Zad 2.16
line = "tworca pythona jest GvR i jest super"
nowy = line.replace("GvR", "Guido van Rossum")
print("2.16:", nowy)

# Zad 2.17
line = "bardzo fajny jezyk programowania"
slowa = line.split()
sort_alf = sorted(slowa)
sort_dl = sorted(slowa, key=len)
print("2.17 alfabetycznie:", sort_alf)
print("2.17 po dlugosci:", sort_dl)

# Zad 2.18
liczba = 10020003004
tekst = str(liczba)
zera = tekst.count("0")
print("2.18:", zera)

# Zad 2.19
L = [7, 24, 123, 5]
wynik = ""
for liczba in L:
    wynik = wynik + str(liczba).zfill(3)
print("2.19:", wynik)