def dodaj_macierze(a, b):
    if len(a) != len(b) or len(a[0]) != len(b[0]):
        raise ValueError("Macierze musza miec takie same wymiary.")
    return [[a[i][j] + b[i][j] for j in range(len(a[0]))] for i in range(len(a))]

def pomnoz_macierze(a, b):
    if len(a[0]) != len(b):
        raise ValueError("Liczba kolumn macierzy A musi byc rowna liczbie wierszy macierzy B.")
    return [[sum(a[i][k] * b[k][j] for k in range(len(b))) for j in range(len(b[0]))] for i in range(len(a))]

def transponuj_macierz(a):
    return [[a[j][i] for j in range(len(a))] for i in range(len(a[0]))]

def wykonaj(operacja, zmienne):
    try:
        return eval(operacja, {}, zmienne)
    except Exception as e:
        return f"Blad: {str(e)}"

macierz_a = [[1, 2], [3, 4]]
macierz_b = [[5, 6], [7, 8]]

operacje = [
    "dodaj_macierze(macierz_a, macierz_b)",
    "pomnoz_macierze(macierz_a, macierz_b)",
    "transponuj_macierz(macierz_a)"
]

for operacja in operacje:
    wynik = wykonaj(operacja, {
        "macierz_a": macierz_a,
        "macierz_b": macierz_b,
        "dodaj_macierze": dodaj_macierze,
        "pomnoz_macierze": pomnoz_macierze,
        "transponuj_macierz": transponuj_macierz
    })
    print(f"Operacja: {operacja}\nWynik:\n{wynik}\n")
