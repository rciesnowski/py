import funkcje
import math

class Logarytm:
    def __init__(self, podstawa, argument):
        if podstawa <= 0 or podstawa == 1:
            raise ZlaPodstawa
        if argument <= 0:
            raise ZlyArgument
        else:
            self.podstawa = podstawa
            self.argument = argument

    def __str__(self):
        s = "log" + str(self.podstawa) + "(" + str(self.argument) + ")\n"
        return s

    def __add__(self, l):
        if self.podstawa == l.podstawa:
            a = Logarytm(self.podstawa, self.argument * l.argument)
        else:
            raise RoznePodstawy
        return a

    def redukuj(self):
        if float(self.podstawa).is_integer():
            lp1 = funkcje.czynnikiPierwsze(self.podstawa)
            lp2 = funkcje.liczbaIWykladnik(lp1)
            la1 = funkcje.czynnikiPierwsze(self.argument)
            la2 = funkcje.liczbaIWykladnik(la1)
            return Logarytm(lp2[0], la2[0])
        else:
            raise TypeError

    def oblicz(self):
        return math.log(self.argument, self.podstawa)


class ZlaPodstawa(Exception):
    def __str__(self):
        return "zla podstawa"


class ZlyArgument(Exception):
    def __str__(self):
        return "zly argument"


class RoznePodstawy(Exception):
    def __str__(self):
        return "rozne podstawy"

