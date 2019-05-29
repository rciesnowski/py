import samochody


class Autohandel:
    def __init__(self):
        self.lista = []

    def dodajSamochod(self, s):
        self.lista.append(s)
    def usunSamochod(self, s):
        self.lista.remove(s)

    def __str__(self):
        a = "Samochody:\n\n"
        for i in self.lista:
            a += str(i)
            a += "\n"
        return a


s1 = samochody.Maluch(2300, 1973, 'FSO', 'Katowice', True, False)
s2 = samochody.Porche(6, 'Porche', 1998, 5)

p = Autohandel()
p.dodajSamochod(s1)
p.dodajSamochod(s2)
print p
p.usunSamochod(s2)
print p


