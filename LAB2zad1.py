from collections import Counter


def zadanie1(text):
    ilosc_slow = len(text.split())
    ilosc_zdan = text.count(".")
    ilosc_akapitow = len([paragraph for paragraph in text.split("\n") if paragraph.strip()])

    print(f"Liczba słów: {ilosc_slow}")
    print(f"Liczba zdań: {ilosc_zdan}")
    print(f"Liczba akapitów: {ilosc_akapitow}")

    # Najczęstsze słowa bez stop words
    stop_words = {"i", "a", "the", "ale", "nie", "na", "to"}
    words = [word.strip(".,").lower() for word in text.split() if word.lower() not in stop_words]
    najczestsze = Counter(words).most_common(3)
    print("Najczęstsze słowa (bez stop words):", najczestsze)

    # Transformacja słów zaczynających się na "a" lub "A"
    transformed = [
        word[::-1] if word.lower().startswith("a") else word
        for word in text.split()
    ]
    transformed_text = " ".join(transformed)
    print("Tekst po transformacji:")
    print(transformed_text)


# Przykładowy tekst
tekst = """
Ala ma kota.
Ala ma kota. Ale nie ma psa.
ala ma kota. Ale nie ma psa.
"""

zadanie1(tekst)