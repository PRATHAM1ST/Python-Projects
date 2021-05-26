from random import randint
def users(p, x, n, f, g):
    if n == 0:
        return 5
    plane = p
    for a in range(0, 9, 3):
        for b in range(3):
            if (plane[a:a + 3].count(g) == 2 and '_' in plane[a:a+3]):
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
    x = x[-1]
    if n >= 2:
        for b in range(0, 9):
            print(b, end = '')
            if p[b] == 'o':

                if b == 0 or b == 3 or b == 6:

                    if 'o' == p[b + 1] and p[b + 1] != p[b + 2] and p[b + 2] != 'x':  # checking of 1st row
                        return (b + 3)

                    if 'o' == p[b + 2] and p[b + 1] != 'o' and p[b + 1] != 'x':
                        return (b + 2)

                    if b == 0:
                        if 'o' == p[b + 4] and p[b + 4] != p[b + 8] and p[b + 8] != 'x':  # checking diagonal from 0 to 8
                            return (b + 9)

                        if 'o' == p[b + 3] and 'o' != p[b + 6] and p[b + 6] != 'x':  # checking coloumn 1st
                            return (b + 7)

                        if 'o' != p[b + 3] and 'o' == p[b + 6] and p[b + 3] != 'x':  # checking coloumn 1st
                            return (b + 4)

                    if b == 6:
                        if 'o' == p[b - 2] and p[b - 2] != p[b - 4] and p[b - 4] != 'x':  # checking diagonal from 6 to 2
                            return (b - 3)

                        if 'o' == p[b - 3] and 'o' != p[b - 6] and p[b - 6] != 'x':  # checking coloumn 1st
                            return (b - 5)

                    if b == 3:
                        if 'o' == p[b - 3] and 'o' != p[b + 3] and p[b + 3] != 'x':  # checking coloumn 1st
                            return (b + 4)

                if b == 1 or b == 4 or b == 7:

                    if 'o' == p[b + 1] and p[b + 1] != p[b - 1] and p[b - 1] != 'x':  # cheking of 2nd row
                        return (b)

                    if b == 1:
                        if 'o' == p[b + 3] and 'o' != p[b + 6] and p[b + 6] != 'x':  # checking coloumn 2nd
                            return (b + 7)

                        if 'o' != p[b + 3] and 'o' == p[b + 6] and p[b + 3] != 'x':  # checking coloumn 1st
                            return (b + 4)

                    if b == 4:
                        if 'o' == p[b - 3] and 'o' != p[b + 3] and p[b + 3] != 'x':  # checking coloumn 2nd
                            return (b + 4)

                    if b == 7:
                        if 'o' == p[b - 3] and 'o' != p[b - 6] and p[b - 6] != 'x':  # checking coloumn 2nd
                            return (b - 5)

                if b == 2 or b == 5 or b == 8:

                    if 'o' == p[b - 1] and p[b - 1] != p[b - 2] and p[b - 2] != 'x':  # checking of 3rd row
                        return (b - 1)

                    if b == 2:
                        if 'o' == p[b + 2] and p[b + 4] != p[b + 2] and p[b + 4] != 'x':  # checking diagonal from 2 to 6
                            return (b + 5)

                        if 'o' == p[b + 3] and 'o' != p[b + 6] and p[b + 6] != 'x':  # checking coloumn 3rd
                            return (b + 7)

                        if 'o' != p[b + 3] and 'o' == p[b + 6] and p[b + 3] != 'x':  # checking coloumn 1st
                            return (b + 4)

                    if b == 8:
                        if 'o' == p[b - 4] and p[b - 4] != p[b - 8] and p[b - 8] != 'x':  # checking diagonal from 8 to 0
                            return (b - 7)

                        if 'o' == p[b - 3] and 'o' != p[b - 6] and p[b - 6] != 'x':  # checking coloumn 3rd
                            return (b - 5)

                    if b == 5:
                        if 'o' == p[b + 3] and 'o' != p[b - 3] and p[b - 3] != 'x':  # checking coloumn 3rd
                            return (b - 2)

    try:
        if x == 0 or x == 3 or x == 6:
            if p[x] == p[x + 1] and p[x] != p[x + 2] and 'o' != p[x + 2]:
                return (x + 3)

            if p[x] == p[x + 2] and p[x] != p[x + 1] and 'o' != p[x + 1]:
                return (x + 2)


            if x == 0:
                if p[x] == p[x + 3] and p[x] != p[x + 6] and 'o' != p[x + 6]:
                    return (x + 7)

                if p[x] == p[x + 6] and p[x] != p[x + 3] and 'o' != p[x + 3]:
                    return (x + 3)

                if p[x] == p[x + 8] and p[x] != p[x + 4]:
                    return (2)


            if x == 3:
                if p[x] == p[x + 3] and p[x] != p[x - 3] and 'o' != p[x - 3]:
                    return (x - 2)

                if p[x] == p[x - 3] and p[x] != p[x + 3] and 'o' != p[x + 3]:
                    return (x + 4)

                if p[x] != p[x + 3] and p[x] != p[x - 3] and p[x + 3] == p[x - 3]:
                    return (x - 2)

                if p[x] != p[x + 3] and p[x] != p[x - 3] and p[x + 3] == 'o':
                    return (x - 2)

                if p[x] != p[x + 3] and p[x] != p[x - 3] and p[x - 3] != 'x':
                    return (x + 4)



            if x == 6:
                if p[x] == p[x - 3] and p[x] != p[x - 6] and 'o' != p[x - 6]:
                    return (x - 5)

                if p[x] == p[x - 6] and p[x] != p[x - 3] and 'o' != p[x - 3]:
                    return (x - 2)

                if p[x] == p[x - 4] and p[x] != p[x - 2]:
                    return (2)



            if x == 0 or x == 6:
                if p[x] == p[4] and p[x] != p[8 - x] and 'o' != p[8 - x]:
                    return (8 - x + 1)

                if p[x] == p[8 - x] and p[x] != p[4]  and 'o' != p[4]:
                    return (5)



        if x == 1 or x == 4 or x == 7:
            if p[x] == p[x + 1] and p[x] != p[x - 1] and 'o' != p[x - 1]:
                return (x)

            if p[x] == p[x - 1] and p[x] != p[x + 1] and 'o' != p[x + 1]:
                return (x + 2)


            if x == 1:
                if p[x] == p[x + 3] and p[x] != p[x + 6] and 'o' != p[x + 6]:
                    return (x + 7)

                if p[x] == p[x + 6] and p[x] != p[x + 3] and 'o' != p[x + 3]:
                    return (x + 4)

                if p[x] != p[x + 1] and p[x] != p[x - 1] and p[x + 1] == p[x - 1]:
                    return (x + 2)

                if p[x] != p[x + 1] and p[x] != p[x - 1] and p[x + 1] == 'o':
                    return (x)

                if p[x] != p[x + 1] and p[x] != p[x - 1] and p[x - 1] != 'x':
                    return (x + 2)


            if x == 4:
                if p[x] == p[x + 3] and p[x] != p[x - 3] and 'o' != p[x - 3]:
                    return (x - 2)

                if p[x] == p[x - 3] and p[x] != p[x + 3] and 'o' != p[x + 3]:
                    return (x + 4)


            if x == 7:
                if p[x] == p[x - 3] and p[x] != p[x - 6] and 'o' != p[x - 6]:
                    return (x - 5)

                if p[x] == p[x - 6] and p[x] != p[x - 3] and 'o' != p[x - 3]:
                    return (x - 2)

                if p[x] != p[x + 1] and p[x] != p[x - 1] and p[x + 1] == p[x - 1]:
                    return (x)

                if p[x] != p[x + 1] and p[x] != p[x - 1] and p[x + 1] == 'o':
                    return(x)

                if p[x] != p[x + 1] and p[x] != p[x - 1] and p[x - 1] != 'x':
                    return (x + 2)


        if x == 2 or x == 5 or x == 8:
            if p[x] == p[x - 1] and p[x] != p[x - 2] and 'o' != p[x - 2]:
                return (x - 1)

            if p[x] == p[x - 2] and p[x] != p[x - 1] and 'o' != p[x - 1]:
                return (x)


            if x == 2:
                if p[x] == p[x + 3] and p[x] != p[x + 6] and 'o' != p[x + 6]:
                    return (x + 7)

                if p[x] == p[x + 6] and p[x] != p[x + 3] and 'o' != p[x + 3]:
                    return (x + 4)

                if p[x] == p[x + 4] and p[x] != p[x + 2]:
                    return (2)


            if x == 5:
                if p[x] == p[x + 3] and p[x] != p[x - 3] and 'o' != p[x - 3]:
                    return (x - 2)

                if p[x] == p[x - 3] and p[x] != p[x + 3] and 'o' != p[x + 3]:
                    return (x + 4)

                if p[x] != p[x + 3] and p[x] != p[x - 3] and p[x + 3] == p[x - 3]:
                    return (x + 4)

                if p[x] != p[x + 3] and p[x] != p[x - 3] and p[x + 3] == 'o':
                    return (x - 2)

                if p[x] != p[x + 3] and p[x] != p[x - 3] and p[x - 3] != 'x':
                    return (x + 4)


            if x == 8:
                if p[x] == p[x - 3] and p[x] != p[x - 6] and 'o' != p[x - 6]:
                    return (x - 5)

                if p[x] == p[x - 6] and p[x] != p[x - 3] and 'o' != p[x - 3]:
                    return (x - 2)

                if p[x] == p[x - 8] and p[x] != p[x - 4]:
                    return (2)

                if 'o' == p[x - 8] and p[x - 8] != p[2]:
                    return (3)


            if x == 2 or x == 8:
                if p[x] == p[4] and p[x] != p[8 - x]:
                    return (8 - x + 1)

                if p[x] == p[8 - x] and p[x] != p[4]:
                    return (5)

    except NameError as a:
        print(end ='')

def user(p, x, n, f, g):
    x = users(p, x, n, f, g)
    try:
        if x == None or p[x - 1] != '_' :
            while True:
                b = randint(0, 8)
                if p[b] == '_':
                    return (b + 1)
        else:
            return x
    except:
        if x[1] == 2:
            for i in x[0]:
                if p[i] == '_':
                    return (i + 1)
