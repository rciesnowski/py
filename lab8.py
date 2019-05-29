print("Dana jest liczba 123")
dec = 123
dec2 = dec
list = []
while dec2 > 1:
    a = dec2 % 2
    dec2 = dec2//2
    list.insert(0, a)
print "Utworzona lista: [", ' '.join(map(str, list)), "]"
print dec, "= (", ''.join(map(str, list)), ")"


import random
list2 = random.sample(range(1, 49), 6)
list2.sort()
print "\n\nWylosowane liczby: [", ', '.join(map(str, list2)), "]\n\n"


dict1 = {
"student1": {"nazwisko": "Kowalski", "imie": "Jan", "nr albumu":"12345"},
"student2": {"nazwisko": "Adamski", "imie": "Adam", "nr albumu": "12346"},
"student3": {"nazwisko": "Beacka", "imie": "Beata", "nr albumu": "12347"}
}
list3 = dict1.values()
list3.sort()
list4 = []
for i in range (0, len(list3)):
    list4.append(' '.join(map(str, list3[i].values())))
print ', '.join(map(str, list4))

