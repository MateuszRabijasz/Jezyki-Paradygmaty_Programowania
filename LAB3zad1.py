class Employee:
    def __init__(self, name, age, salary):
        self.name = name
        self.age = age
        self.salary = salary

    def __str__(self):
        return f"Pracownik: {self.name}, Wiek: {self.age}, Wynagrodzenie: {self.salary}"

class EmployeesManager:
    def __init__(self):
        self.employees = []

    def dodaj_pracownika(self):
        name = input("Podaj imię i nazwisko pracownika: ")
        age = int(input("Podaj wiek pracownika: "))
        salary = float(input("Podaj wynagrodzenie pracownika: "))
        pracownik = Employee(name, age, salary)
        self.employees.append(pracownik)
        print("Pracownik dodany!\n")

    def wyswietl_pracownikow(self):
        if not self.employees:
            print("Brak pracowników.\n")
        else:
            for pracownik in self.employees:
                print(pracownik)

    def szukaj_pracownika(self):
        name = input("Podaj imię i nazwisko do wyszukania: ")
        znaleziony = [pracownik for pracownik in self.employees if pracownik.name == name]
        if znaleziony:
            for pracownik in znaleziony:
                print(pracownik)
        else:
            print("Nie znaleziono pracownika o podanym imieniu i nazwisku.\n")

    def aktualizuj_wynagrodzenie(self):
        name = input("Podaj imię i nazwisko pracownika: ")
        nowe_wynagrodzenie = float(input("Podaj nowe wynagrodzenie: "))
        for pracownik in self.employees:
            if pracownik.name == name:
                pracownik.salary = nowe_wynagrodzenie
                print("Wynagrodzenie zaktualizowane!\n")
                return
        print("Nie znaleziono pracownika o podanym imieniu i nazwisku.\n")

class FrontendManager:
    def __init__(self):
        self.manager = EmployeesManager()

    def menu(self):
        while True:
            print("1. Dodaj pracownika")
            print("2. Wyświetl pracowników")
            print("3. Szukaj pracownika")
            print("4. Aktualizuj wynagrodzenie")
            print("5. Wyjdź")
            wybor = input("Wybierz opcję: ")
            if wybor == "1":
                self.manager.dodaj_pracownika()
            elif wybor == "2":
                self.manager.wyswietl_pracownikow()
            elif wybor == "3":
                self.manager.szukaj_pracownika()
            elif wybor == "4":
                self.manager.aktualizuj_wynagrodzenie()
            elif wybor == "5":
                print("Koniec programu.")
                break
            else:
                print("Nieprawidłowy wybór, spróbuj ponownie.\n")

if __name__ == "__main__":
    frontend = FrontendManager()
    frontend.menu()