from random import randint
import Comp1

def check(plane, f, g):
    for a in range(0, 9, 3):
        for b in range(3):
            x = [f, f, f]
            o = [g, g, g]
            if (plane[a:a + 3] == x) or (plane[a + b :: 3] == x and a == 0) or (plane[a + b::4] == x and (a, b) == (0, 0)) or (plane[a + b:7:2] == x and (a, b) == (0, 2)):
                return f
            if (plane[a:a + 3] == o) or (plane[a + b :: 3] == o and a == 0) or (plane[a + b::4] == o and (a, b) == (0, 0)) or (plane[a + b:7:2] == o and (a, b) == (0, 2)):
                return g

            elif (plane[a:a + 3].count(g) == 2 and '_' in plane[a:a+3]):
                return ((list(range(a, a + 3)), 2))
            elif (plane[a + b :: 3].count(g) == 2 and '_' in plane[a + b::3] and a == 0):
                return ((list(range(a + b, 9, 3)), 2))
            elif (plane[a + b:: 4].count(g) == 2 and '_' in plane[a + b::4] and (a, b) == (0, 0)):
                return ((list(range(a + b, 9, 4)), 2))
            elif (plane[a + b:7:2].count(g) == 2 and '_' in plane[a + b:7:2] and (a, b) == (0, 2)):
                return ((list(range(a + b, 7, 2)), 2))

            elif (plane[a:a + 3].count(f) == 2 and '_' in plane[a:a+3]):
                return ((list(range(a, a + 3)), 2))
            elif (plane[a + b :: 3].count(f) == 2 and '_' in plane[a + b::3] and a == 0):
                return ((list(range(a + b, 9, 3)), 2))
            elif (plane[a + b:: 4].count(f) == 2 and '_' in plane[a + b::4] and (a, b) == (0, 0)):
                return ((list(range(a + b, 9, 4)), 2))
            elif (plane[a + b:7:2].count(f) == 2 and '_' in plane[a + b:7:2] and (a, b) == (0, 2)):
                return ((list(range(a + b, 7, 2)), 2))

def comp2(plane, comp_u, n, f, g):
            user = Comp1.user(plane, comp_u, n, f, g)
            return user
