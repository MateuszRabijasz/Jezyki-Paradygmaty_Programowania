def znajdz_najwieksza_liczbe(dane):
    liczby = filter(lambda x: isinstance(x, (int, float)), dane)
    return max(liczby, default=None)

def znajdz_najdluzszy_napis(dane):
    napisy = filter(lambda x: isinstance(x, str), dane)
    return max(napisy, key=len, default=None)

def znajdz_najwieksza_krotke(dane):
    krotki = filter(lambda x: isinstance(x, tuple), dane)
    return max(krotki, key=len, default=None)

dane = [123, "tekst", (1, 2, 3), [1, 2], {"klucz": "wartosc"}, "dluzszy tekst", 42.5, (1,2)]

najwieksza_liczba = znajdz_najwieksza_liczbe(dane)
najdluzszy_napis = znajdz_najdluzszy_napis(dane)
najwieksza_krotka = znajdz_najwieksza_krotke(dane)

print(f"Najwieksza liczba: {najwieksza_liczba}")
print(f"Najdluzszy napis: {najdluzszy_napis}")
print(f"Najwieksza krotka: {najwieksza_krotka}")