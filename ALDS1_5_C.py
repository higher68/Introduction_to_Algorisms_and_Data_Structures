import math
n = int(input())


class point:
    def __init__(self, x, y):
        self.x = x
        self.y = y


def koch(n, point_a, point_b):
        if n == 0:
            return 0
        s = point((2*a.x+1*b.x)/3, (2*a.y+1*b.y)/3)
        t = point((1*a.x+2*b.x)/3, (1*a.y+2*b.y)/3)
        u = point((t.x-s.x)*math.cos(th)-(t.y-s.y)*math.sin(th)+s.x,
                  (t.x-s.x)*math.sin(th)-(t.y-s.y)*math.cos(th)+s.y)
