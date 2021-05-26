from numpy import *

p = array(['_', '_', '_', '_', '_', '_', '_', '_', '_'])
z = array([ 0 , 1 , 2 , 3 , 4 , 5 , 6 , 7 , 8 ])                                   # plane
a = 'o'
b = 'x'
m = p.reshape(3, 3)
n = z.reshape(3, 3)                                                           # reshape of plane
print(n)
print('choose any one no. from upper table.')
try:
    for i in range(0, 5):klmk
        x = int(input('write for x :'))
        if 'x' != p[x] and 'o' != p[x]:
            p[x] = 'x'

            if i == 0:
                if x != 4:
                    p[4] = 'o'
                if x == 4:
                    p[0] = 'o'

            if i >= 1:

                for b in range(0, 9):
                    if p[b] == 'o':

                        if b == 0 or b == 3 or b == 6:

                            if 'o' == p[b + 1] and p[b + 1] != p[b + 2] and p[b + 2] != 'x':  # checking of 1st row
                                p[b + 2] = 'o'
                                print(m)
                                print('o won!')
                                end
                            if 'o' == p[b + 2] and p[b + 1] != 'o' and p[b + 1] != 'x':
                                p[b + 1] = 'o'
                                print(m)
                                print('o won!')
                                end

                            if b == 0:
                                if 'o' == p[b + 4] and p[b + 4] != p[b + 8] and p[b + 8] != 'x':  # checking diagonal from 0 to 8
                                    p[b + 8] = 'o'
                                    print(m)
                                    print('o won!')
                                    end
                                if 'o' == p[b + 3] and 'o' != p[b + 6] and p[b + 6] != 'x':  # checking coloumn 1st
                                    p[b + 6] = 'o'
                                    print(m)
                                    print('o won!')
                                    end
                                if 'o' != p[b + 3] and 'o' == p[b + 6] and p[b + 3] != 'x':  # checking coloumn 1st
                                    p[b + 3] = 'o'
                                    print(m)
                                    print('o won!')
                                    end

                            if b == 6:
                                if 'o' == p[b - 2] and p[b - 2] != p[b - 4] and p[b - 4] != 'x':  # checking diagonal from 6 to 2
                                    p[b - 4] = 'o'
                                    print(m)
                                    print('o won!')
                                    end
                                if 'o' == p[b - 3] and 'o' != p[b - 6] and p[b - 6] != 'x':  # checking coloumn 1st
                                    p[b - 6] = 'o'
                                    print(m)
                                    print('o won!')
                                    end

                            if b == 3:
                                if 'o' == p[b - 3] and 'o' != p[b + 3] and p[b + 3] != 'x':  # checking coloumn 1st
                                    p[b + 3] = 'o'
                                    print(m)
                                    print('o won!')
                                    end

                        if b == 1 or b == 4 or b == 7:

                            if 'o' == p[b + 1] and p[b + 1] != p[b - 1] and p[b - 1] != 'x':  # cheking of 2nd row
                                p[b - 1] = 'o'
                                print(m)
                                print('o won!')
                                end

                            if b == 1:
                                if 'o' == p[b + 3] and 'o' != p[b + 6] and p[b + 6] != 'x':  # checking coloumn 2nd
                                    p[b + 6] = 'o'
                                    print(m)
                                    print('o won!')
                                    end
                                if 'o' != p[b + 3] and 'o' == p[b + 6] and p[b + 3] != 'x':  # checking coloumn 1st
                                    p[b + 3] = 'o'
                                    print(m)
                                    print('o won!')
                                    end

                            if b == 4:
                                if 'o' == p[b - 3] and 'o' != p[b + 3] and p[b + 3] != 'x':  # checking coloumn 2nd
                                    p[b + 3] = 'o'
                                    print(m)
                                    print('o won!')
                                    end

                            if b == 7:
                                if 'o' == p[b - 3] and 'o' != p[b - 6] and p[b - 6] != 'x':  # checking coloumn 2nd
                                    p[b - 6] = 'o'
                                    print(m)
                                    print('o won!')
                                    end

                        if b == 2 or b == 5 or b == 8:

                            if 'o' == p[b - 1] and p[b - 1] != p[b - 2] and p[b - 2] != 'x':  # checking of 3rd row
                                p[b - 2] = 'o'
                                print(m)
                                print('o won!')
                                end

                            if b == 2:
                                if 'o' == p[b + 2] and p[b + 4] != p[b + 2] and p[b + 4] != 'x':  # checking diagonal from 2 to 6
                                    p[b + 4] = 'o'
                                    print(m)
                                    print('o won!')
                                    end
                                if 'o' == p[b + 3] and 'o' != p[b + 6] and p[b + 6] != 'x':  # checking coloumn 3rd
                                    p[b + 6] = 'o'
                                    print(m)
                                    print('o won!')
                                    end
                                if 'o' != p[b + 3] and 'o' == p[b + 6] and p[b + 3] != 'x':  # checking coloumn 1st
                                    p[b + 3] = 'o'
                                    print(m)
                                    print('o won!')
                                    end

                            if b == 8:
                                if 'o' == p[b - 4] and p[b - 4] != p[b - 8] and p[b - 8] != 'x':  # checking diagonal from 8 to 0
                                    p[b - 8] = 'o'
                                    print(m)
                                    print('o won!')
                                    end
                                if 'o' == p[b - 3] and 'o' != p[b - 6] and p[b - 6] != 'x':  # checking coloumn 3rd
                                    p[b - 6] = 'o'
                                    print(m)
                                    print('o won!')
                                    end

                            if b == 5:
                                if 'o' == p[b + 3] and 'o' != p[b - 3] and p[b - 3] != 'x':  # checking coloumn 3rd
                                    p[b - 3] = 'o'
                                    print(m)
                                    print('o won!')
                                    end

                try:
                    if x == 0 or x == 3 or x == 6:
                        if p[x] == p[x + 1] and p[x] != p[x + 2] and 'o' != p[x + 2]:
                            p[x + 2] = 'o'
                            end
                        if p[x] == p[x + 2] and p[x] != p[x + 1] and 'o' != p[x + 1]:
                            p[x + 1] = 'o'
                            end

                        if x == 0:
                            if p[x] == p[x + 3] and p[x] != p[x + 6] and 'o' != p[x + 6]:
                                p[x + 6] = 'o'
                                end
                            if p[x] == p[x + 6] and p[x] != p[x + 3] and 'o' != p[x + 3]:
                                p[x + 3] = 'o'
                                end
                            if p[x] == p[x + 8] and p[x] != p[x + 4]:
                                p[1] = 'o'
                                end

                        if x == 3:
                            if p[x] == p[x + 3] and p[x] != p[x - 3] and 'o' != p[x - 3]:
                                p[x - 3] = 'o'
                                end
                            if p[x] == p[x - 3] and p[x] != p[x + 3] and 'o' != p[x + 3]:
                                p[x + 3] = 'o'
                                end
                            if p[x] != p[x + 3] and p[x] != p[x - 3] and p[x + 3] == p[x - 3]:
                                p[x - 3] = 'o'
                                end
                            if p[x] != p[x + 3] and p[x] != p[x - 3] and p[x + 3] == 'o':
                                p[x - 3] = 'o'
                                end
                            if p[x] != p[x + 3] and p[x] != p[x - 3] and p[x - 3] != 'x':
                                p[x + 3] = 'o'
                                end


                        if x == 6:
                            if p[x] == p[x - 3] and p[x] != p[x - 6] and 'o' != p[x - 6]:
                                p[x - 6] = 'o'
                                end
                            if p[x] == p[x - 6] and p[x] != p[x - 3] and 'o' != p[x - 3]:
                                p[x - 3] = 'o'
                                end
                            if p[x] == p[x - 4] and p[x] != p[x - 2]:
                                p[1] = 'o'
                                end


                        if x == 0 or x == 6:
                            if p[x] == p[4] and p[x] != p[8 - x] and 'o' != p[8 - x]:
                                p[8 - x] = 'o'
                                end
                            if p[x] == p[8 - x] and p[x] != p[4]  and 'o' != p[4]:
                                p[4] = 'o'
                                end


                    if x == 1 or x == 4 or x == 7:
                        if p[x] == p[x + 1] and p[x] != p[x - 1] and 'o' != p[x - 1]:
                            p[x - 1] = 'o'
                            end
                        if p[x] == p[x - 1] and p[x] != p[x + 1] and 'o' != p[x + 1]:
                            p[x + 1] = 'o'
                            end

                        if x == 1:
                            if p[x] == p[x + 3] and p[x] != p[x + 6] and 'o' != p[x + 6]:
                                p[x + 6] = 'o'
                                end
                            if p[x] == p[x + 6] and p[x] != p[x + 3] and 'o' != p[x + 3]:
                                p[x + 3] = 'o'
                                end
                            if p[x] != p[x + 1] and p[x] != p[x - 1] and p[x + 1] == p[x - 1]:
                                p[x + 1] = 'o'
                                end
                            if p[x] != p[x + 1] and p[x] != p[x - 1] and p[x + 1] == 'o':
                                p[x - 1] = 'o'
                                end
                            if p[x] != p[x + 1] and p[x] != p[x - 1] and p[x - 1] != 'x':
                                p[x + 1] = 'o'
                                end

                        if x == 4:
                            if p[x] == p[x + 3] and p[x] != p[x - 3] and 'o' != p[x - 3]:
                                p[x - 3] = 'o'
                                end
                            if p[x] == p[x - 3] and p[x] != p[x + 3] and 'o' != p[x + 3]:
                                p[x + 3] = 'o'
                                end

                        if x == 7:
                            if p[x] == p[x - 3] and p[x] != p[x - 6] and 'o' != p[x - 6]:
                                p[x - 6] = 'o'
                                end
                            if p[x] == p[x - 6] and p[x] != p[x - 3] and 'o' != p[x - 3]:
                                p[x - 3] = 'o'
                                end
                            if p[x] != p[x + 1] and p[x] != p[x - 1] and p[x + 1] == p[x - 1]:
                                p[x - 1] = 'o'
                                end
                            if p[x] != p[x + 1] and p[x] != p[x - 1] and p[x + 1] == 'o':
                                p[x - 1] = 'o'
                                end
                            if p[x] != p[x + 1] and p[x] != p[x - 1] and p[x - 1] != 'x':
                                p[x + 1] = 'o'
                                end

                    if x == 2 or x == 5 or x == 8:
                        if p[x] == p[x - 1] and p[x] != p[x - 2] and 'o' != p[x - 2]:
                            p[x - 2] = 'o'
                            end
                        if p[x] == p[x - 2] and p[x] != p[x - 1] and 'o' != p[x - 1]:
                            p[x - 1] = 'o'
                            end

                        if x == 2:
                            if p[x] == p[x + 3] and p[x] != p[x + 6] and 'o' != p[x + 6]:
                                p[x + 6] = 'o'
                                end
                            if p[x] == p[x + 6] and p[x] != p[x + 3] and 'o' != p[x + 3]:
                                p[x + 3] = 'o'
                                end
                            if p[x] == p[x + 4] and p[x] != p[x + 2]:
                                p[1] = 'o'
                                end

                        if x == 5:
                            if p[x] == p[x + 3] and p[x] != p[x - 3] and 'o' != p[x - 3]:
                                p[x - 3] = 'o'
                                end
                            if p[x] == p[x - 3] and p[x] != p[x + 3] and 'o' != p[x + 3]:
                                p[x + 3] = 'o'
                                end
                            if p[x] != p[x + 3] and p[x] != p[x - 3] and p[x + 3] == p[x - 3]:
                                p[x + 3] = 'o'
                                end
                            if p[x] != p[x + 3] and p[x] != p[x - 3] and p[x + 3] == 'o':
                                p[x - 3] = 'o'
                                end
                            if p[x] != p[x + 3] and p[x] != p[x - 3] and p[x - 3] != 'x':
                                p[x + 3] = 'o'
                                end

                        if x == 8:
                            if p[x] == p[x - 3] and p[x] != p[x - 6] and 'o' != p[x - 6]:
                                p[x - 6] = 'o'
                                end
                            if p[x] == p[x - 6] and p[x] != p[x - 3] and 'o' != p[x - 3]:
                                p[x - 3] = 'o'
                                end
                            if p[x] == p[x - 8] and p[x] != p[x - 4]:
                                p[1] = 'o'
                                end
                            if 'o' == p[x - 8] and p[x - 8] != p[2]:
                                p[2] = 'o'


                        if x == 2 or x == 8:
                            if p[x] == p[4] and p[x] != p[8 - x]:
                                p[8 - x] = 'o'
                                end
                            if p[x] == p[8 - x] and p[x] != p[4]:
                                p[4] = 'o'
                                end
                except NameError as a:
                    print(end='')

            print(m)
            for a in range(0, 9):
                if p[a] == 'x' or p[a] == 'o':

                    if a == 0 or a == 3 or a == 6:

                        if p[a] == p[a + 1] and p[a + 1] == p[a + 2]:  # checking of 1st row
                            print(p[a], end=' ')
                            print('won!', end='')
                            end

                        if a == 0:
                            if p[a] == p[a + 4] and p[a + 4] == p[a + 8]:  # checking diagonal from 0 to 8
                                print(p[a], end=' ')
                                print('won!', end='')
                                end
                            if p[a] == p[a + 3] and p[a] == p[a + 6]:  # checking coloumn 1st
                                print(p[a], end=' ')
                                print('won!', end='')
                                end

                        if a == 6:
                            if p[a] == p[a - 2] and p[a - 2] == p[a - 4]:  # checking diagonal from 6 to 2
                                print(p[a], end=' ')
                                print('won!', end='')
                                end
                            if p[a] == p[a - 3] and p[a] == p[a - 6]:  # checking coloumn 1st
                                print(p[a], end=' ')
                                print('won!', end='')
                                end

                        if a == 3:
                            if p[a] == p[a - 3] and p[a] == p[a + 3]:  # checking coloumn 1st
                                print(p[a], end=' ')
                                print('won!', end='')
                                end

                    if a == 1 or a == 4 or a == 7:

                        if p[a] == p[a + 1] and p[a + 1] == p[a - 1]:  # cheking of 2nd row
                            print(p[a], end=' ')
                            print('won!', end='')
                            end

                        if a == 1:
                            if p[a] == p[a + 3] and p[a] == p[a + 6]:  # checking coloumn 2nd
                                print(p[a], end=' ')
                                print('won!', end='')
                                end

                        if a == 4:
                            if p[a] == p[a - 3] and p[a] == p[a + 3]:  # checking coloumn 2nd
                                print(p[a], end=' ')
                                print('won!', end='')
                                end

                        if a == 7:
                            if p[a] == p[a - 3] and p[a] == p[a - 6]:  # checking coloumn 2nd
                                print(p[a], end=' ')
                                print('won!', end='')
                                end

                    if a == 2 or a == 5 or a == 8:

                        if p[a] == p[a - 1] and p[a - 1] == p[a - 2]:  # checking of 3rd row
                            print(p[a], end=' ')
                            print('won!', end='')
                            end

                        if a == 2:
                            if p[a] == p[a + 2] and p[a + 4] == p[a + 2]:  # checking diagonal from 2 to 6
                                print(p[a], end=' ')
                                print('won!', end='')
                                end
                            if p[a] == p[a + 3] and p[a] == p[a + 6]:  # checking coloumn 3rd
                                print(p[a], end=' ')
                                print('won!', end='')
                                end

                        if a == 8:
                            if p[a] == p[a - 4] and p[a - 4] == p[a - 8]:  # checking diagonal from 8 to 0
                                print(p[a], end=' ')
                                print('won!', end='')
                                end
                            if p[a] == p[a - 3] and p[a] == p[a - 6]:  # checking coloumn 3rd
                                print(p[a], end=' ')
                                print('won!', end='')
                                end

                        if a == 5:
                            if p[a] == p[a + 3] and p[a] == p[a - 3]:  # checking coloumn 3rd
                                print(p[a], end=' ')
                                print('won!', end='')
                                end

    if p.any != 'o' or p.any != 'x':
        print('draw')


except NameError as e:
    print('')
except IndexError as a:
    print('Restart the game!')
