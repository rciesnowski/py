
class Pracownik:
    def __init__(self, nazwisko, imie, pesel, stanowisko, zarobki):
        self.nazwisko = nazwisko
        self.imie = imie
        self.pesel = pesel
        self.stanowisko = stanowisko
        self.zarobki = zarobki

    def __str__(self):
        return "Nazwisko: " + self.nazwisko\
               + "\nImie: " + self.imie\
               + "\nPesel: " + self.pesel\
               + "\nStanowisko: " + self.stanowisko\
               + "\nZarobki: " + self.zarobki\

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
            return super().__str__() + "\nDodatkowe umiejetnosci: " + self.dodatkowe\
                   + "\nProgramista zna nastepujace jezyki: " + jp
        else:
            return super().__str__() + "\nProgramista zna nastepujace jezyki: " + jp

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
            return super().__str__() + "\nDodatkowe umiejetnosci: " + self.dodatkowe\
                   + "\nSprzedawca posluguje sie nastepujacymi jezykami: " + jo \
                   + "\nCharakterystyka pracy: " + self.charakterystyka
        else:
            return super().__str__() + "\nSprzedawca posluguje sie nastepujacymi jezykami: " + jo \
                   + "\nCharakterystyka pracy: " + self.charakterystyka

