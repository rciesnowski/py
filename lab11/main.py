import logarytm
try:
    l1 = logarytm.Logarytm(3, 8)
    l2 = logarytm.Logarytm(3, 2)
    l3 = logarytm.Logarytm(2, 8)
    #l4 = logarytm.Logarytm(0, 3)
    #l5 = logarytm.Logarytm(3, 0)
    l6 = logarytm.Logarytm(4, 9)
    print l1
    print l1 + l2
    print logarytm.Logarytm.oblicz(l3)
    print logarytm.Logarytm.redukuj(l6)
    print l1 + l3

except logarytm.ZlaPodstawa as zP:
    print zP
except logarytm.ZlyArgument as zA:
    print zA
except logarytm.RoznePodstawy as rP:
    print rP