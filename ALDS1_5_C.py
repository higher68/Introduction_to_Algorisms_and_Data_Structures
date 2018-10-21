import math
n = int(input())
pi = math.acos(-1)
th = pi/3


class point:
    def __init__(self, x, y):
        self.x = x
        self.y = y


def koch(n, a, b):
        if n == 0:
            return 0
        s = point((2*a.x+1*b.x)/3, (2*a.y+1*b.y)/3)
        t = point((1*a.x+2*b.x)/3, (1*a.y+2*b.y)/3)
        u = point((t.x-s.x)*math.cos(th)
                  - (t.y-s.y)*math.sin(th)+s.x,
                  (t.x-s.x)*math.sin(th)+(t.y-s.y)*math.cos(th)+s.y)
        koch(n-1, a, s)
        print("{:.8f} {:.8f}".format(s.x, s.y))
        koch(n-1, s, u)
        print("{:.8f} {:.8f}".format(u.x, u.y))
        koch(n-1, u, t)
        print("{:.8f} {:.8f}".format(t.x, t.y))
        koch(n-1, t, b)


a = point(round(0, 8), round(0, 8))
b = point(round(100, 8), round(0, 8))
print("{:.8f} {:.8f}".format(a.x, a.y))
koch(n, a, b)
print("{:.8f} {:.8f}".format(b.x, b.y))
