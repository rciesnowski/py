
from random import randint

class Macierz:
    def __init__(self, m, n):
        self.m = m
        self.n = n
        self.macierz = [m][n]
        for i in m:
            for j in n:
                macierz[i][j] = randint(1,10)
    def __str__(self):
        zwrot = "\n"
        for i in m:
            for j in n:
                zwrot += str(macierz[i][j])
            zwrot += "\n"
        return zwrot
    def sumaWierszy(self):
        listaSum = []
        for i in m:
            sumka = 0
            for j in n:
                sumka += macierz[i][j]
            listaSum.append(sumka)
        print("Suma liczb w wierszach: " + listaSum)
    def sumaKolumn(self):
        listaSum = []
        for j in n:
            sumka = 0
            for i in m:
                sumka += macierz[i][j]
            listaSum.append(sumka)
        print("\nSuma liczb w kolumnach: " + listaSum)

class MacierzTrojkatna(Macierz):
    def __init__(self, n, wlasciwosc = "L"):
        Macierz.__init__(n, n)
        self.wlasciwosc = wlasciwosc
        if wlasciwosc == "U":
            for i in n:
                while (j <= n) and (j >= i):
                   for j in (j, n):
                       macierz[i][j] = 0
        if wlasciwosc == "L":
             for i in n:
                while (j <= n) and (j >= i):
                   for j in (j, n):
                       macierz[j][i] = 0
    def __str__(self):
        zwrot = Macierz.__str__(self) + "\n"
        if self.wlasciwosc == "L":
            zwrot += " - jest to macierz trojkatna dolna\n"
        if self.wlasciwosc == "U":
            zwrot += " - jest to macierz trojkatna gorna\n"