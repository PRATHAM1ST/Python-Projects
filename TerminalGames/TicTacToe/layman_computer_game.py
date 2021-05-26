from random import *
from numpy import *

p = array(['_', '_', '_', '_', '_', '_', '_', '_', '_'])                               # plane
z = array([0 , 1 , 2 , 3 , 4 , 5 , 6 , 7 , 8])
m = p.reshape(3, 3)
n = z.reshape(3, 3)                                                           # reshape of plane
print(n)
print('choose any one no. from upper table.')
for i in range(0, 100):
    try:
        x = int(input('write for x :'))
        if 'x' != p[x] and 'o' != p[x]:
            p[x] = 'x'
        else:
            end

        try:
            for i in range(10):
                o = random.randint(0, 9)
                print(o)
                if p[o] != 'o' and p[o] != 'x':
                        p[o] = 'o'
                        end
                elif o + 1 <= 8:
                    if p[o + 1] != 'o' and p[o + 1] != 'x':
                        p[o + 1] ='o'
                        end
        except NameError as e:
            print(end='')
        print(m)
        for a in range(0, 9):
                if p[a] == 'x' or p[a] == 'o':

                    if a == 0 or a == 3 or a == 6:

                        if p[a] == p[a + 1] and p[a + 1] == p[a + 2]:  # checking of 1st row
                            print(p[a], end=' ')
                            print('won!')
                            1/0

                        if a == 0:
                            if p[a] == p[a + 4] and p[a + 4] == p[a + 8]:  # checking diagonal from 0 to 8
                                print(p[a], end=' ')
                                print('won!')
                                1/0
                            if p[a] == p[a + 3] and p[a] == p[a + 6]:  # checking coloumn 1st
                                print(p[a], end=' ')
                                print('won!')
                                1/0

                        if a == 6:
                            if p[a] == p[a - 2] and p[a - 2] == p[a - 4]:  # checking diagonal from 6 to 2
                                print(p[a], end=' ')
                                print('won!')
                                1/0
                            if p[a] == p[a - 3] and p[a] == p[a - 6]:  # checking coloumn 1st
                                print(p[a], end=' ')
                                print('won!')
                                1/0

                        if a == 3:
                            if p[a] == p[a - 3] and p[a] == p[a + 3]:  # checking coloumn 1st
                                print(p[a], end=' ')
                                print('won!')
                                1/0

                    if a == 1 or a == 4 or a == 7:

                        if p[a] == p[a + 1] and p[a + 1] == p[a - 1]:  # cheking of 2nd row
                            print(p[a], end=' ')
                            print('won!')
                            1/0

                        if a == 1:
                            if p[a] == p[a + 3] and p[a] == p[a + 6]:  # checking coloumn 2nd
                                print(p[a], end=' ')
                                print('won!')
                                1/0

                        if a == 4:
                            if p[a] == p[a - 3] and p[a] == p[a + 3]:  # checking coloumn 2nd
                                print(p[a], end=' ')
                                print('won!')
                                1/0

                        if a == 7:
                            if p[a] == p[a - 3] and p[a] == p[a - 6]:  # checking coloumn 2nd
                                print(p[a], end=' ')
                                print('won!')
                                1/0

                    if a == 2 or a == 5 or a == 8:

                        if p[a] == p[a - 1] and p[a - 1] == p[a - 2]:  # checking of 3rd row
                            print(p[a], end=' ')
                            print('won!')
                            1/0

                        if a == 2:
                            if p[a] == p[a + 2] and p[a + 4] == p[a + 2]:  # checking diagonal from 2 to 6
                                print(p[a], end=' ')
                                print('won!')
                                1/0
                            if p[a] == p[a + 3] and p[a] == p[a + 6]:  # checking coloumn 3rd
                                print(p[a], end=' ')
                                print('won!')
                                1/0

                        if a == 8:
                            if p[a] == p[a - 4] and p[a - 4] == p[a - 8]:  # checking diagonal from 8 to 0
                                print(p[a], end=' ')
                                print('won!')
                                1/0
                            if p[a] == p[a - 3] and p[a] == p[a - 6]:  # checking coloumn 3rd
                                print(p[a], end=' ')
                                print('won!')
                                1/0

                        if a == 5:
                            if p[a] == p[a + 3] and p[a] == p[a - 3]:  # checking coloumn 3rd
                                print(p[a], end=' ')
                                print('won!')
                                1/0
        if i >= 6:
            if p.any != 'o' and p.any != 'x':
                print('draw')

    except NameError as a:
        print(end='')
    except ZeroDivisionError as a:
        break
    except IndexError as a:
        print(end='')
