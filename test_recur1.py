n = 2
s = [0] * n


def rec(i):
    if i == n:
        print(s)
        return s

    rec(i+1)
    s[i] = 1
    rec(i+1)
    s[i] = 0


rec(0)
