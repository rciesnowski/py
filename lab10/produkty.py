class PolskiProdukt:
    def __init__(self, wytwornia, miasto, gwarancja):
        self.wytwornia = wytwornia
        self.miasto = miasto
        self.gwarancja = gwarancja

    def __str__(self):
        s = "wytwornia: " + self.wytwornia + "\n"
        s += "miasto: " + str(self.miasto) + "\n"
        if self.gwarancja:
            s += "gwarancja: tak"
        else:
            s += "gwarancja: nie"
        return s