# Zad 3.1
# 1) kod dziala poprawnie chociaz sredniki na koncu i nawiasy przy if sa niepotrzebne
# 2) kod nie dziala bo po dwukropku w petli for nie mozna dac instrukcji if w tej samej linii
# 3) kod dziala poprawnie

# Zad 3.2
# 1) metoda sort() sortuje liste w miejscu i zwraca None wiec pod L przypisze sie None
# 2) za duzo wartosci do przypisania bo sa trzy liczby a tylko dwie zmienne
# 3) X to tuple a krotki nie mozna modyfikowac
# 4) lista ma 3 elementy (indeksy 0, 1, 2) wiec X[3] wychodzi poza zakres
# 5) na stringu nie mozna uzyc metody append()
# 6) funkcja pow() wymaga dwoch argumentow a dostaje tylko jeden

# Zad 3.3
wynik_for = ""
for i in range(31):
    if i % 3 != 0:
        wynik_for = wynik_for + str(i) + " "
wynik_for = wynik_for.strip()
print("3.3 for:", wynik_for)

wynik_while = ""
i = 0
while i <= 30:
    if i % 3 != 0:
        wynik_while = wynik_while + str(i) + " "
    i = i + 1
wynik_while = wynik_while.strip()
print("3.3 while:", wynik_while)
assert wynik_for == "1 2 4 5 7 8 10 11 13 14 16 17 19 20 22 23 25 26 28 29"
assert wynik_while == wynik_for

# Zad 3.4
while True:
    tekst = input("Podaj liczbe (lub stop): ")
    if tekst == "stop":
        break
    try:
        x = float(tekst)
        print(x, x ** 3)
    except ValueError:
        print("Blad, podana wartosc nie jest liczba")

# Zad 3.5
x = 12
kreski = "|"
liczby = "0"
for i in range(1, x + 1):
    kreski = kreski + "....|"
    s = str(i)
    ile_spacji = 5 - len(s)
    liczby = liczby + (" " * ile_spacji) + s
miarka = kreski + "\n" + liczby
print("3.5:")
print(miarka)
assert miarka == "|....|....|....|....|....|....|....|....|....|....|....|....|\n0    1    2    3    4    5    6    7    8    9   10   11   12"

# Zad 3.6
x = 4
y = 2
linia1 = "+" + "---+" * x + "\n"
linia2 = "|" + "   |" * x + "\n"
prostokat = ""
for i in range(y):
    prostokat = prostokat + linia1 + linia2
prostokat = prostokat + linia1.strip()
print("3.6:")
print(prostokat)
assert prostokat == "+---+---+---+---+\n|   |   |   |   |\n+---+---+---+---+\n|   |   |   |   |\n+---+---+---+---+"

# Zad 3.7
class Time:
    def __init__(self, seconds=0):
        self.s = seconds

    def __str__(self):
        return "{} sec".format(self.s)

    def __repr__(self):
        return "Time({})".format(self.s)

time1 = Time(12)
time2 = Time(3456)
print(time1, time2)
print([time1, time2])
# po zakomentowaniu __str__ pierwszy print uzyje metody __repr__ i wypisze Time(12) Time(3456)
# po zakomentowaniu __repr__ wypisanie listy pokaze domyslna reprezentacje obiektow z adresem w pamieci

# Zad 3.8
a = [1, 2, 3, 4, 4, 5]
b = [3, 4, 5, 6, 7]
wspolne = list(set(a) & set(b))
wszystkie = list(set(a) | set(b))
print("3.8 a:", wspolne)
print("3.8 b:", wszystkie)
assert sorted(wspolne) == [3, 4, 5]
assert sorted(wszystkie) == [1, 2, 3, 4, 5, 6, 7]

# Zad 3.9
L = [[], [4], (1, 2), [3, 4], (5, 6, 7)]
wynik = []
for el in L:
    wynik.append(sum(el))
print("3.9:", wynik)
assert wynik == [0, 4, 3, 7, 18]

# Zad 3.10
# 1 sposob - nawiasy klamrowe
rzymskie1 = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}

# 2 sposob - dict() z lista krotek
rzymskie2 = dict([("I", 1), ("V", 5), ("X", 10), ("L", 50), ("C", 100), ("D", 500), ("M", 1000)])

# 3 sposob - polaczenie dwoch list przez zip()
klucze = ["I", "V", "X", "L", "C", "D", "M"]
wartosci = [1, 5, 10, 50, 100, 500, 1000]
rzymskie3 = dict(zip(klucze, wartosci))

# 4 sposob - dict() z argumentami nazwanymi
rzymskie4 = dict(I=1, V=5, X=10, L=50, C=100, D=500, M=1000)

assert rzymskie1 == rzymskie2 == rzymskie3 == rzymskie4

# petla przechodzi po kolejnych znakach napisu i pobiera ich wartosci ze slownika
# jezeli biezacy znak jest mniejszy od nastepnego (np. IV, XL) to odejmujemy go od wyniku, w przeciwnym razie dodajemy
def roman2int(napis):
    wynik = 0
    for i in range(len(napis)):
        aktualna = rzymskie1[napis[i]]
        if i + 1 < len(napis) and aktualna < rzymskie1[napis[i + 1]]:
            wynik = wynik - aktualna
        else:
            wynik = wynik + aktualna
    return wynik

liczba_arabska = roman2int("MMXXIV")
print("3.10:", liczba_arabska)
assert liczba_arabska == 2024
