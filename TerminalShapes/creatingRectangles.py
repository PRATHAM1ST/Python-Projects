def rectangle(x, y):
    count = 0   #counter
    for b in range(x):  #for making height
        print('|', end = '')
        for a in range(y):  #for making width
            if count == 0 or count == x - 1:
                print('--', end='')
            else:
                print('  ', end ='')
        print('|')
        count += 1

#height
HEIGHT = input('what should be the height of the rectangle: ')
#width
WIDTH = input('what should be width of the rectangle: ')

rectangle(int(HEIGHT), int(WIDTH))
