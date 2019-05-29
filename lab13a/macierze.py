
from random import randint

class Macierz:
    def __init__(self, m, n):
        self.m = m
        self.n = n
        self.macierz = []
        for i in range(0, n):
            templist = []
            for j in range(0, m):
                templist.append(randint(1,10))
            self.macierz.append(templist)


    def __str__(self):
        zwrot = "\n"
        self.macierz
        for i in self.macierz:
            zwrot += '\t'.join(map(str, i))
            zwrot += "\n"
        return zwrot

    def sumaWierszy(self):
        listaSum = []
        for i in self.macierz:
            sumka = 0
            for j in i:
                sumka += j
            listaSum.append(sumka)
        print("Suma liczb w wierszach: " + ' '.join(map(str, listaSum)))

class MacierzTrojkatna(Macierz):
    def __init__(self, n, wlasciwosc = "L"):
        Macierz.__init__(n, n)
        self.wlasciwosc = wlasciwosc

    def __str__(self):
        zwrot = Macierz.__str__(self) + "\n"
        if self.wlasciwosc == "L":
            zwrot += " - jest to macierz trojkatna dolna\n"
        if self.wlasciwosc == "U":
            zwrot += " - jest to macierz trojkatna gorna\n"