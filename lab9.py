def is_palindrome(n):
    return n == n[::-1]

def check():
    sol = []
    for i in range(100000, 999996):
        a, b, c, d, e, f = str(i)
        n1 = c, d, e, f
        if is_palindrome(n1):
            a, b, c, d, e, f = str(i + 1)
            n2 = b, c, d, e, f
            if is_palindrome(n2):
                a, b, c, d, e, f = str(i + 2)
                n3 = b, c, d, e
                if is_palindrome(n3):
                    a, b, c, d, e, f = str(i + 3)
                    n4 = a, b, c, d, e, f
                    if is_palindrome(n4):
                        sol.append(i)
    return sol


x = check()
a, b = x
print a, ' : (+1) ', a + 1, ' : (+2) ', a + 2, ' : (+3) ', a + 3
print b, ' : (+1) ', b + 1, ' : (+2) ', b + 2, ' : (+3) ', b + 3




