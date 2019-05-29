import pracownicy

with open("pracownicy.txt") as file:
    wiersze = file.read().splitlines()
file.close()

for wiersz in wiersze:
    if "Programista" in wiersz or "programista" in wiersz:
        pracownik = pracownicy.Programista(wiersz.split(','))
        print(pracownik.__str__())
    if "sprzeda" in wiersz:
        pracownik = pracownicy.Sprzedawca(wiersz.split(','))
        print(pracownik.__str__())