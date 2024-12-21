from functools import reduce

def suma_macierzy(a, b):
    return [[a[i][j] + b[i][j] for j in range(len(a[0]))] for i in range(len(a))]

def iloczyn_macierzy(a, b):
    return [[sum(a[i][k] * b[k][j] for k in range(len(b))) for j in range(len(b[0]))] for i in range(len(a))]

def polacz_macierze(macierze, operacja):
    return reduce(operacja, macierze)

macierz_1 = [[1, 2], [3, 4]]
macierz_2 = [[5, 6], [7, 8]]
macierz_3 = [[1, 1], [1, 1]]

lista_macierzy = [macierz_1, macierz_2, macierz_3]

try:
    operacja = input("Wybierz operacje (suma/iloczyn): ").strip()
    if operacja == "suma":
        wynik = polacz_macierze(lista_macierzy, suma_macierzy)
    elif operacja == "iloczyn":
        wynik = polacz_macierze(lista_macierzy, iloczyn_macierzy)
    else:
        raise ValueError("Nieznana operacja.")

    print("Wynik:")
    for wiersz in wynik:
        print(wiersz)
except Exception as e:
    print(f"Blad: {e}")