# Zad 4.1
# 1) wypisze "qwerty", bo wewnatrz funkcji nie ma lokalnej zmiennej X, wiec Python szuka jej w zakresie globalnym
# 2) wypisze "qwerty", bo X = "abc" tworzy nowa zmienna lokalna wewnatrz funkcji i nie zmienia globalnej zmiennej X
# 3) wypisze "abc", bo instrukcja global X pozwala funkcji modyfikowac zmienna X z zakresu globalnego

# Zad 4.2
def make_ruler(n):
    kreski = "|"
    liczby = "0"
    for i in range(1, n + 1):
        kreski = kreski + "....|"
        s = str(i)
        ile_spacji = 5 - len(s)
        liczby = liczby + (" " * ile_spacji) + s
    return kreski + "\n" + liczby

def make_grid(rows, cols):
    linia1 = "+" + "---+" * cols + "\n"
    linia2 = "|" + "   |" * cols + "\n"
    prostokat = ""
    for i in range(rows):
        prostokat = prostokat + linia1 + linia2
    prostokat = prostokat + linia1.strip()
    return prostokat

miarka = make_ruler(12)
print("4.2 miarka:")
print(miarka)
assert miarka == "|....|....|....|....|....|....|....|....|....|....|....|....|\n0    1    2    3    4    5    6    7    8    9   10   11   12"

siatka = make_grid(2, 4)
print("4.2 siatka:")
print(siatka)
assert siatka == "+---+---+---+---+\n|   |   |   |   |\n+---+---+---+---+\n|   |   |   |   |\n+---+---+---+---+"

# Zad 4.3
def factorial(n):
    wynik = 1
    for i in range(2, n + 1):
        wynik = wynik * i
    return wynik

silnia_5 = factorial(5)
print("4.3:", silnia_5)
assert factorial(0) == 1
assert silnia_5 == 120

# Zad 4.4
def fibonacci(n):
    a = 0
    b = 1
    for i in range(n):
        a, b = b, a + b
    return a

fib_10 = fibonacci(10)
print("4.4:", fib_10)
assert fibonacci(0) == 0
assert fibonacci(1) == 1
assert fib_10 == 55

# Zad 4.5
def odwracanie(L, left, right):
    while left < right:
        L[left], L[right] = L[right], L[left]
        left = left + 1
        right = right - 1

def odwracanie_rek(L, left, right):
    if left < right:
        L[left], L[right] = L[right], L[left]
        odwracanie_rek(L, left + 1, right - 1)

lista1 = [0, 1, 2, 3, 4, 5, 6]
odwracanie(lista1, 2, 5)
print("4.5 iteracyjnie:", lista1)
assert lista1 == [0, 1, 5, 4, 3, 2, 6]

lista2 = [0, 1, 2, 3, 4, 5, 6]
odwracanie_rek(lista2, 2, 5)
print("4.5 rekurencyjnie:", lista2)
assert lista2 == [0, 1, 5, 4, 3, 2, 6]

# Zad 4.6
def sum_seq(sequence):
    suma = 0
    for item in sequence:
        if isinstance(item, (list, tuple)):
            suma = suma + sum_seq(item)
        else:
            suma = suma + item
    return suma

seq_suma = [1, (2, 3), [], [4, (5, 6, 7)], 8, [9]]
wynik_suma = sum_seq(seq_suma)
print("4.6:", wynik_suma)
assert wynik_suma == 45

# Zad 4.7
def flatten(sequence):
    wynik = []
    for item in sequence:
        if isinstance(item, (list, tuple)):
            wynik = wynik + flatten(item)
        else:
            wynik.append(item)
    return wynik

sequence = [1, (2, 3), [], [4, (5, 6, 7)], 8, [9]]
splaszczona = flatten(sequence)
print("4.7:", splaszczona)
assert splaszczona == [1, 2, 3, 4, 5, 6, 7, 8, 9]
