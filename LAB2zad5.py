def wygeneruj_kod(szablon, dane):
    try:
        kod = szablon.format(**dane)
        return kod
    except KeyError as e:
        return f"Blad: Brakuje danych dla: {e}"

def uruchom_kod(kod):
    try:
        exec(kod)
    except Exception as e:
        print(f"Blad podczas uruchamiania kodu: {e}")

szablon = """
def funkcja(x):
    return x {operacja} {wartosc}

wynik = funkcja({argument})
print(f"Wynik: {{wynik}}")
"""

dane = {
    "operacja": "+",
    "wartosc": 10,
    "argument": 5
}

kod = wygeneruj_kod(szablon, dane)
if "Blad" not in kod:
    print("Wygenerowany kod:")
    print(kod)
    print("\nUruchamianie kodu:")
    uruchom_kod(kod)
else:
    print(kod)
