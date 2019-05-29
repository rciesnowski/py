import re

class Car:
    def __init__(self, line):
        [self.model, self.mpg, self.cylinders, self.engine_disp, self.horsepower, self.weight, self.accelerate, self.year, self.origin] = line.split(",")

    def __str__(self):
        a = self.model + ", " + self.mpg + ", " + self.cylinders + ", " + self.engine_disp + ", " + self.horsepower + ", "
        a = a + self.weight + ", " + self.accelerate + ", " + self.year + ", " + self.origin
        return a

class Cars:
    def __init__(self, lineList):
        self.carList=[]
        for line in linesList:
            self.carList.append(Car(line))

    def getCarsByString(self, str1, atrr):
        for c in self.carList:
            if getattr(c, atrr) == str1:
                return c
        return None

    def replaceValue(self, str1, atrr, str2):
        c = self.getCarsByString(str1, atrr)
        setattr(c, atrr, str2)
        return c

filePath = "cars.csv"

with open(filePath) as file:
    linesList = file.read().splitlines()
file.close()

linesList = linesList[1:]
cl = Cars(linesList)

i = 0
for c in cl.carList:
    # fordy
    #a = re.match(r'ford', getattr(c,'model'))
    # toyoty i volvo
    #a = re.match(r'toyota|volvo', getattr(c, 'model'))
    # z liczbami
    #a = re.match(r'.*\d(.*)', getattr(c, 'model'))
    # nielitery nieliczby niespacje
    #a = re.match(r'.*[^A-Za-z\d\s]+.*', getattr(c, 'model'))
    # dwuspacyjne
    #a = re.match(r'[*\s]*[*\s][^\s]*[*\s][^\s]*', getattr(c, 'model'))
    # dwusamogloskowe
    #a = re.match(r'^[*aeiouy\s]*[aeiouy][^aeiouy\s]*[aeiouy][^aeiouy\s]*\s.*', getattr(c, 'model'))
    # konie dwucyfrowe
    #a = re.match(r'[1-9][0-9]', getattr(c, 'horsepower'))
    # przyspieszenie z kropka
    #a = re.match(r'(.*)[.](.*)', getattr(c, 'accelerate'))
    # lata 70
    #a = re.match(r'7\d', getattr(c, 'year'))
    if a:
        print c
        i += 1

print("\n\nZnaleziono %d" % (i))


