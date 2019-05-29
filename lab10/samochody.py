import produkty


class Samochod:
    def __init__(self, marka, rokProdukcji, iloscDrzwi, przebieg = 0, kolor = ""):
        self.marka = marka
        self.rokProdukcji = rokProdukcji
        self.iloscDrzwi = iloscDrzwi
        self.przebieg = przebieg
        self.kolor = kolor

    def __str__(self):
        s = "marka: " + self.marka + "\n"
        s += "rok produkcji: " + str(self.rokProdukcji) + "\n"
        s += "ilosc drzwi: " + str(self.iloscDrzwi) + "\n"
        s += "przebieg: " + str(self.przebieg) + "\n"
        s += "kolor: " + self.kolor
        return s


class Maluch(Samochod, produkty.PolskiProdukt):
    def __init__(self, glosnosc, rokProdukcji, wytwornia, miasto, gwarancja, czyJezdzi = True):
        Samochod.__init__(self, "Fiat", rokProdukcji,2)
        produkty.PolskiProdukt.__init__(self, wytwornia, miasto, gwarancja)
        self.glosnosc = glosnosc
        self.czyJezdzi = czyJezdzi

    def __str__(self):
        s = Samochod.__str__(self) + "\n"
        s += produkty.PolskiProdukt.__str__(self) + "\n"
        s += "ilosc drzwi: " + str(self.iloscDrzwi) + "\n"
        if self.czyJezdzi:
            s += "czy jezdzi: tak\n"
        else:
            s += "czy jezdzi: nie\n"
        return s


class Porche(Samochod):
    def __init__(self, ileDoSetki, marka, rokProdukcji, iloscDrzwi):
        Samochod.__init__(self, marka, rokProdukcji, iloscDrzwi)
        self.ileDoSetki = ileDoSetki

    def __str__(self):
        s = Samochod.__str__(self) + "\n"
        s += "ile do setki: " + str(self.ileDoSetki) + "\n"
        return s