def czynnikiPierwsze(n):
    i = 2
    czynniki = []
    while i * i <= n:
        if n % i:
            i += 1
        else:
            n //= i
            czynniki.append(i)
    if n > 1:
        czynniki.append(n)
    return czynniki


def liczbaIWykladnik(czynniki):
    if len(set(czynniki)) <= 1:
        return [czynniki[1], len(czynniki)]
    else:
        return 'czynniki nie sa rowne'

