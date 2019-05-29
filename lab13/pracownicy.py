class Pracownik:
    def __init__(self, nazwisko, imie, pesel, stanowisko, zarobki):
        self.nazwisko = nazwisko
        self.imie = imie
        self.pesel = pesel
        self.stanowisko = stanowisko
        self.zarobki = zarobki

    def __str__(self):
        n = "Nazwisko: " + self.nazwisko + "\nImie: " + self.imie
        n += "\nPesel: " + self.pesel + "\nStanowisko: " + self.stanowisko
        n += "\nZarobki: " + self.zarobki
        return n

class Programista(Pracownik):
    def __init__(self, wiersz):
        nazwisko = wiersz[0]
        imie = wiersz[1]
        pesel = wiersz[2]
        stanowisko = wiersz[3]
        zarobki = wiersz[4]
        jp = wiersz[5]
        if len(wiersz) == 7:
            self.dodatkowe = wiersz[6]
        else:
            self.dodatkowe = ""

        super().__init__(nazwisko, imie, pesel, stanowisko, zarobki)
        self.jp = jp


    def __str__(self):
        jp = ""
        for j in self.jp.split(" "):
            jp += "\n- " + j

        if self.dodatkowe is not "":
            n = super().__str__() + "\nDodatkowe umiejetnosci: " + self.dodatkowe
            n += "\nProgramista zna nastepujace jezyki: " + jp
            return n
        else:
            n = super().__str__() + "\nProgramista zna nastepujace jezyki: " + jp
            return n

class Sprzedawca(Pracownik):
    def __init__(self, wiersz):
        nazwisko = wiersz[0]
        imie = wiersz[1]
        pesel = wiersz[2]
        stanowisko = wiersz[3]
        zarobki = wiersz[4]
        jo = wiersz[5]
        charakterystyka = wiersz[6]
        if len(wiersz) == 8:
            self.dodatkowe = wiersz[7]
        else:
            self.dodatkowe = ""

        super().__init__(nazwisko, imie, pesel, stanowisko, zarobki)
        self.jo = jo
        self.charakterystyka = charakterystyka

    def __str__(self):
        jo = ""
        for j in self.jo.split(" "):
            jo += "\n- " + j
        if self.dodatkowe is not "":
            n = super().__str__() + "\nDodatkowe umiejetnosci: " + self.dodatkowe
            n += "\nSprzedawca posluguje sie nastepujacymi jezykami: " + jo
            n += "\nCharakterystyka pracy: " + self.charakterystyka
            return n
        else:
            n = super().__str__() + "\nSprzedawca posluguje sie nastepujacymi jezykami: " + jo
            n += "\nCharakterystyka pracy: " + self.charakterystyka
            return n

