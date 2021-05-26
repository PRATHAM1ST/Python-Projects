import pygame
import random
import datetime
import time
from time import *
from pygame import *

################################################################
pygame.init()

DISPLAY_BACKGROUND = pygame.display.set_mode((500,500))
pygame.display.set_caption('Snake Game')

font = pygame.font.SysFont("Century Gothic", 25, True)

black = (0, 0, 0)

clock = pygame.time.Clock()

session_start = datetime.datetime.utcnow()

start_time = pygame.time.get_ticks()

x = 50
y = 50

path = []

vel = 5

food = 0

food_x = random.randint(20, 480)
food_y = random.randint(20, 480)

key = []

extra_food_x = random.randint(50, 450)
extra_food_y = random.randint(50, 450)
extra_food_size = 50
extra_food_random = False
extra_food_selection = [20, 40, 60, 80, 100, 120, 140, 160, 180, 200]
extra_food_time_start = 0

######################################################################################################################

start = [pygame.image.load('start.png')]
start = [pygame.transform.scale(start[0], (500, 500))]

#############################################################################################

extra_food = [pygame.image.load('extra_food.png')]
extra_food = [pygame.transform.scale(extra_food[0], (extra_food_size, extra_food_size))]

background = [pygame.image.load('background.png')]
background = [pygame.transform.scale(background[0], (500, 500))]

snake = [pygame.image.load('1.jpg'),pygame.image.load('2.jpg'),pygame.image.load('3.jpg'),pygame.image.load('4.jpg'),pygame.image.load('5.jpg'),pygame.image.load('6.jpg'),pygame.image.load('7.jpg'),pygame.image.load('8.jpg'),pygame.image.load('9.jpg'),pygame.image.load('10.jpg'),pygame.image.load('11.jpg'),pygame.image.load('12.jpg'),pygame.image.load('13.jpg'),pygame.image.load('14.jpg'),pygame.image.load('15.jpg'),pygame.image.load('16.jpg'),pygame.image.load('17.jpg'),pygame.image.load('18.jpg'),pygame.image.load('19.jpg'),pygame.image.load('20.jpg'),pygame.image.load('21.jpg'),pygame.image.load('22.jpg'),pygame.image.load('23.jpg'),pygame.image.load('24.jpg'),pygame.image.load('25.jpg'),pygame.image.load('26.jpg'),pygame.image.load('27.jpg'),pygame.image.load('28.jpg'),pygame.image.load('29.jpg'),pygame.image.load('30.jpg'),pygame.image.load('31.jpg'),pygame.image.load('32.jpg'),pygame.image.load('33.jpg'),pygame.image.load('34.jpg'),pygame.image.load('35.jpg'),pygame.image.load('36.jpg'),pygame.image.load('37.jpg'),pygame.image.load('38.jpg'),pygame.image.load('39.jpg'),pygame.image.load('40.jpg'),pygame.image.load('41.jpg'),pygame.image.load('42.jpg'),pygame.image.load('43.jpg'),pygame.image.load('44.jpg'),pygame.image.load('45.jpg'),pygame.image.load('46.jpg'),pygame.image.load('47.jpg'),pygame.image.load('48.jpg'),pygame.image.load('49.jpg'),pygame.image.load('50.jpg'),pygame.image.load('51.jpg'),pygame.image.load('52.jpg'),pygame.image.load('53.jpg'),pygame.image.load('54.jpg'),pygame.image.load('55.jpg'),pygame.image.load('56.jpg'),pygame.image.load('57.jpg'),pygame.image.load('58.jpg'),pygame.image.load('59.jpg'),pygame.image.load('60.jpg'),pygame.image.load('61.jpg'),pygame.image.load('62.jpg'),pygame.image.load('63.jpg'),pygame.image.load('64.jpg'),pygame.image.load('65.jpg'),pygame.image.load('66.jpg'),pygame.image.load('67.jpg'),pygame.image.load('68.jpg'),pygame.image.load('69.jpg'),pygame.image.load('70.jpg'),pygame.image.load('71.jpg'),pygame.image.load('72.jpg'),pygame.image.load('73.jpg'),pygame.image.load('74.jpg'),pygame.image.load('75.jpg'),pygame.image.load('76.jpg'),pygame.image.load('77.jpg'),pygame.image.load('78.jpg'),pygame.image.load('79.jpg'),pygame.image.load('80.jpg'),pygame.image.load('81.jpg'),pygame.image.load('82.jpg'),pygame.image.load('83.jpg'),pygame.image.load('84.jpg'),pygame.image.load('85.jpg'),pygame.image.load('86.jpg'),pygame.image.load('87.jpg'),pygame.image.load('88.jpg'),pygame.image.load('89.jpg'),pygame.image.load('90.jpg'),pygame.image.load('91.jpg'),pygame.image.load('92.jpg'),pygame.image.load('93.jpg'),pygame.image.load('94.jpg'),pygame.image.load('95.jpg'),pygame.image.load('96.jpg'),pygame.image.load('97.jpg'),pygame.image.load('98.jpg'),pygame.image.load('99.jpg'),pygame.image.load('100.jpg'),pygame.image.load('101.jpg'),pygame.image.load('102.jpg'),pygame.image.load('103.jpg'),pygame.image.load('104.jpg'),pygame.image.load('105.jpg'),pygame.image.load('106.jpg'),pygame.image.load('107.jpg'),pygame.image.load('108.jpg'),pygame.image.load('109.jpg'),pygame.image.load('110.jpg'),pygame.image.load('111.jpg'),pygame.image.load('112.jpg'),pygame.image.load('113.jpg'),pygame.image.load('114.jpg'),pygame.image.load('115.jpg'),pygame.image.load('116.jpg'),pygame.image.load('117.jpg'),pygame.image.load('118.jpg'),pygame.image.load('119.jpg'),pygame.image.load('120.jpg'),pygame.image.load('121.jpg'),pygame.image.load('122.jpg'),pygame.image.load('123.jpg'),pygame.image.load('124.jpg'),pygame.image.load('125.jpg'),pygame.image.load('126.jpg'),pygame.image.load('127.jpg'),pygame.image.load('128.jpg'),pygame.image.load('129.jpg'),pygame.image.load('130.jpg'),pygame.image.load('131.jpg'),pygame.image.load('132.jpg'),pygame.image.load('133.jpg'),pygame.image.load('134.jpg'),pygame.image.load('135.jpg'),pygame.image.load('136.jpg'),pygame.image.load('137.jpg'),pygame.image.load('138.jpg'),pygame.image.load('139.jpg'),pygame.image.load('140.jpg'),pygame.image.load('141.jpg'),pygame.image.load('142.jpg'),pygame.image.load('143.jpg'),pygame.image.load('144.jpg'),pygame.image.load('145.jpg'),pygame.image.load('146.jpg'),pygame.image.load('147.jpg'),pygame.image.load('148.jpg'),pygame.image.load('149.jpg'),pygame.image.load('150.jpg'),pygame.image.load('151.jpg')]

snake = [pygame.transform.scale(snake[0], (20, 20)),pygame.transform.scale(snake[1], (20, 20)),pygame.transform.scale(snake[2], (20, 20)),pygame.transform.scale(snake[3], (20, 20)),pygame.transform.scale(snake[4], (20, 20)),pygame.transform.scale(snake[5], (20, 20)),pygame.transform.scale(snake[6], (20, 20)),pygame.transform.scale(snake[7], (20, 20)),pygame.transform.scale(snake[8], (20, 20)),pygame.transform.scale(snake[9], (20, 20)),pygame.transform.scale(snake[10], (20, 20)),pygame.transform.scale(snake[11], (20, 20)),pygame.transform.scale(snake[12], (20, 20)),pygame.transform.scale(snake[13], (20, 20)),pygame.transform.scale(snake[14], (20, 20)),pygame.transform.scale(snake[15], (20, 20)),pygame.transform.scale(snake[16], (20, 20)),pygame.transform.scale(snake[17], (20, 20)),pygame.transform.scale(snake[18], (20, 20)),pygame.transform.scale(snake[19], (20, 20)),pygame.transform.scale(snake[20], (20, 20)),pygame.transform.scale(snake[21], (20, 20)),pygame.transform.scale(snake[22], (20, 20)),pygame.transform.scale(snake[23], (20, 20)),pygame.transform.scale(snake[24], (20, 20)),pygame.transform.scale(snake[25], (20, 20)),pygame.transform.scale(snake[26], (20, 20)),pygame.transform.scale(snake[27], (20, 20)),pygame.transform.scale(snake[28], (20, 20)),pygame.transform.scale(snake[29], (20, 20)),pygame.transform.scale(snake[30], (20, 20)),pygame.transform.scale(snake[31], (20, 20)),pygame.transform.scale(snake[32], (20, 20)),pygame.transform.scale(snake[33], (20, 20)),pygame.transform.scale(snake[34], (20, 20)),pygame.transform.scale(snake[35], (20, 20)),pygame.transform.scale(snake[36], (20, 20)),pygame.transform.scale(snake[37], (20, 20)),pygame.transform.scale(snake[38], (20, 20)),pygame.transform.scale(snake[39], (20, 20)),pygame.transform.scale(snake[40], (20, 20)),pygame.transform.scale(snake[41], (20, 20)),pygame.transform.scale(snake[42], (20, 20)),pygame.transform.scale(snake[43], (20, 20)),pygame.transform.scale(snake[44], (20, 20)),pygame.transform.scale(snake[45], (20, 20)),pygame.transform.scale(snake[46], (20, 20)),pygame.transform.scale(snake[47], (20, 20)),pygame.transform.scale(snake[48], (20, 20)),pygame.transform.scale(snake[49], (20, 20)),pygame.transform.scale(snake[50], (20, 20)),pygame.transform.scale(snake[51], (20, 20)),pygame.transform.scale(snake[52], (20, 20)),pygame.transform.scale(snake[53], (20, 20)),pygame.transform.scale(snake[54], (20, 20)),pygame.transform.scale(snake[55], (20, 20)),pygame.transform.scale(snake[56], (20, 20)),pygame.transform.scale(snake[57], (20, 20)),pygame.transform.scale(snake[58], (20, 20)),pygame.transform.scale(snake[59], (20, 20)),pygame.transform.scale(snake[60], (20, 20)),pygame.transform.scale(snake[61], (20, 20)),pygame.transform.scale(snake[62], (20, 20)),pygame.transform.scale(snake[63], (20, 20)),pygame.transform.scale(snake[64], (20, 20)),pygame.transform.scale(snake[65], (20, 20)),pygame.transform.scale(snake[66], (20, 20)),pygame.transform.scale(snake[67], (20, 20)),pygame.transform.scale(snake[68], (20, 20)),pygame.transform.scale(snake[69], (20, 20)),pygame.transform.scale(snake[70], (20, 20)),pygame.transform.scale(snake[71], (20, 20)),pygame.transform.scale(snake[72], (20, 20)),pygame.transform.scale(snake[73], (20, 20)),pygame.transform.scale(snake[74], (20, 20)),pygame.transform.scale(snake[75], (20, 20)),pygame.transform.scale(snake[76], (20, 20)),pygame.transform.scale(snake[77], (20, 20)),pygame.transform.scale(snake[78], (20, 20)),pygame.transform.scale(snake[79], (20, 20)),pygame.transform.scale(snake[80], (20, 20)),pygame.transform.scale(snake[81], (20, 20)),pygame.transform.scale(snake[82], (20, 20)),pygame.transform.scale(snake[83], (20, 20)),pygame.transform.scale(snake[84], (20, 20)),pygame.transform.scale(snake[85], (20, 20)),pygame.transform.scale(snake[86], (20, 20)),pygame.transform.scale(snake[87], (20, 20)),pygame.transform.scale(snake[88], (20, 20)),pygame.transform.scale(snake[89], (20, 20)),pygame.transform.scale(snake[90], (20, 20)),pygame.transform.scale(snake[91], (20, 20)),pygame.transform.scale(snake[92], (20, 20)),pygame.transform.scale(snake[93], (20, 20)),pygame.transform.scale(snake[94], (20, 20)),pygame.transform.scale(snake[95], (20, 20)),pygame.transform.scale(snake[96], (20, 20)),pygame.transform.scale(snake[97], (20, 20)),pygame.transform.scale(snake[98], (20, 20)),pygame.transform.scale(snake[99], (20, 20)),pygame.transform.scale(snake[100], (20, 20)),pygame.transform.scale(snake[101], (20, 20)),pygame.transform.scale(snake[102], (20, 20)),pygame.transform.scale(snake[103], (20, 20)),pygame.transform.scale(snake[104], (20, 20)),pygame.transform.scale(snake[105], (20, 20)),pygame.transform.scale(snake[106], (20, 20)),pygame.transform.scale(snake[107], (20, 20)),pygame.transform.scale(snake[108], (20, 20)),pygame.transform.scale(snake[109], (20, 20)),pygame.transform.scale(snake[110], (20, 20)),pygame.transform.scale(snake[111], (20, 20)),pygame.transform.scale(snake[112], (20, 20)),pygame.transform.scale(snake[113], (20, 20)),pygame.transform.scale(snake[114], (20, 20)),pygame.transform.scale(snake[115], (20, 20)),pygame.transform.scale(snake[116], (20, 20)),pygame.transform.scale(snake[117], (20, 20)),pygame.transform.scale(snake[118], (20, 20)),pygame.transform.scale(snake[119], (20, 20)),pygame.transform.scale(snake[120], (20, 20)),pygame.transform.scale(snake[121], (20, 20)),pygame.transform.scale(snake[122], (20, 20)),pygame.transform.scale(snake[123], (20, 20)),pygame.transform.scale(snake[124], (20, 20)),pygame.transform.scale(snake[125], (20, 20)),pygame.transform.scale(snake[126], (20, 20)),pygame.transform.scale(snake[127], (20, 20)),pygame.transform.scale(snake[128], (20, 20)),pygame.transform.scale(snake[129], (20, 20)),pygame.transform.scale(snake[130], (20, 20)),pygame.transform.scale(snake[131], (20, 20)),pygame.transform.scale(snake[132], (20, 20)),pygame.transform.scale(snake[133], (20, 20)),pygame.transform.scale(snake[134], (20, 20)),pygame.transform.scale(snake[135], (20, 20)),pygame.transform.scale(snake[136], (20, 20)),pygame.transform.scale(snake[137], (20, 20)),pygame.transform.scale(snake[138], (20, 20)),pygame.transform.scale(snake[139], (20, 20)),pygame.transform.scale(snake[140], (20, 20)),pygame.transform.scale(snake[141], (20, 20)),pygame.transform.scale(snake[142], (20, 20)),pygame.transform.scale(snake[143], (20, 20)),pygame.transform.scale(snake[144], (20, 20)),pygame.transform.scale(snake[145], (20, 20)),pygame.transform.scale(snake[146], (20, 20)),pygame.transform.scale(snake[147], (20, 20)),pygame.transform.scale(snake[148], (20, 20)),pygame.transform.scale(snake[149], (20, 20)),pygame.transform.scale(snake[150], (20, 20))]

#####################################################################################

def redraw():

    path.append((x, y))

    score_text = font.render('Score: ' +  str(food), 1, (255, 255, 255))
    if food < 10:
        DISPLAY_BACKGROUND.blit(score_text, (390, 0))
    elif food < 100:
        DISPLAY_BACKGROUND.blit(score_text, (380, 0))
    else:
        DISPLAY_BACKGROUND.blit(score_text, (350, 0))

    session_instant = datetime.datetime.utcnow()
    session_time = session_instant - session_start
    session_text = font.render('Time: ' + str(session_time), 1, (255, 255, 255))
    DISPLAY_BACKGROUND.blit(session_text, (345,30))
    for repeat in range(food + 1):
        (a, b) = path[len(path) - (1 * (repeat + 1))]
        if repeat <= 149:
            DISPLAY_BACKGROUND.blit(snake[repeat], (a , b))
        else:
            DISPLAY_BACKGROUND.blit(snake[150], (a, b))

    if extra_food_random == True and (int(time.time()) - extra_food_time_start) < 5:
        DISPLAY_BACKGROUND.blit(extra_food[0], (extra_food_x, extra_food_y))

    pygame.display.update()

def compare(a, b):
    (f, g) = a
    (i, j), (i_2, j_2) = b
    if i <= f and f <= j and i_2 <= g and g <= j_2:
        return True
    else:
        return False

def collision(x, y, food_x, food_y):
    set_i = [(x + 20, y),                                           (y + 20, x + 20),                                (x,y),                                    (y + 20,x),                                      (x,y),                                    (y,x),                                 (x, y + 20),                                                   (x + 20 ,y),                                     (y, x)]
    set_j = [((food_x, food_x + 20), (food_y, food_y + 20)), ((food_y, food_y + 20),(food_x, food_x + 20)), ((food_x + 20, food_x), (food_y, food_y + 20)), ((food_y, food_y + 20),(food_x, food_x)), ((food_x, food_x + 20),(food_y, food_y)), ((food_y + 20, food_y),(food_x, food_x)), ((food_x, food_x + 20), (food_y, food_y + 20)), ((food_y + 20, food_y),(food_x, food_x + 20)), ((food_y, food_y + 20), (food_x, food_x + 20))]
    for a in range(8):
        if compare(set_i[a], set_j[a]) == True:
            return True

    return False

def self_collision(x, y, a, b):
    set_i = [(x + 20, y),                            (x + 20, y),                                       (y, x + 20) ]
    set_j = [((a + 20, a),(b + 20, b)),           ((a, a + 20),(b, b + 20)),                         ((b, b + 20),(a, a + 20))]
    for z in range(3):
        if compare(set_i[z], set_j[z]) == True:
            return True

    return False

def extra_food_collision(x, y, extra_food_x, extra_food_y):
    set_i = [(x + 50, y),                                           (y + 50, x + 50),                                (x,y),                                    (y + 50,x),                                      (x,y),                                    (y,x),                                 (x, y + 50),                                                   (x + 50 ,y),                                     (y, x)]
    set_j = [((extra_food_x, extra_food_x + 50), (extra_food_y, extra_food_y + 50)), ((extra_food_y, extra_food_y + 50),(extra_food_x, extra_food_x + 50)), ((extra_food_x + 50, extra_food_x), (extra_food_y, extra_food_y + 50)), ((extra_food_y, extra_food_y + 50),(extra_food_x, extra_food_x)), ((extra_food_x, extra_food_x + 50),(extra_food_y, extra_food_y)), ((extra_food_y + 50, extra_food_y),(extra_food_x, extra_food_x)), ((extra_food_x, extra_food_x + 50), (extra_food_y, extra_food_y + 50)), ((extra_food_y + 50, extra_food_y),(extra_food_x, extra_food_x + 50)), ((extra_food_y, extra_food_y + 50), (extra_food_x, extra_food_x + 50))]
    for a in range(8):
        if compare(set_i[a], set_j[a]) == True:
            return True

    return False

################################################################################################
#main loop
while True:
    run = False
    if run == False:
        DISPLAY_BACKGROUND.blit(start[0], (0, 0))
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                quit()

        start_key = pygame.key.get_pressed()
        if start_key[pygame.K_KP_ENTER]:
            run = True

        elif start_key[pygame.K_RETURN]:
            run = True

        pygame.display.update()

    while run == True:
        clock.tick(30)
        DISPLAY_BACKGROUND.blit(background[0], (0, 0))
        if food <= 148:
            DISPLAY_BACKGROUND.blit(snake[food + 1], (food_x, food_y))
        else:
            DISPLAY_BACKGROUND.blit(snake[150], (food_x, food_y))
        pygame.time.delay(10)

        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                quit()

        if len(key) != 0:
            if key[len(key) - 1] == 'LEFT':
                if x > 0:
                    x -= vel
            elif key[len(key) - 1] == 'RIGHT':
                if x < 480:
                    x += vel
            elif key[len(key) - 1] == 'UP':
                if y > 0:
                    y -= vel
            elif key[len(key) - 1] == 'DOWN':
                if y < 480:
                    y += vel
        else:
            key.append('RIGHT')

        keys = pygame.key.get_pressed()
        if food == 0:
            if keys[pygame.K_LEFT]:
                if x > 0:
                    x -= vel
                    key.append('LEFT')

            elif keys[pygame.K_RIGHT]:
                if x < 480:
                    x += vel
                    key.append('RIGHT')

            elif keys[pygame.K_UP]:
                if y > 0:
                    y -= vel
                    key.append('UP')

            elif keys[pygame.K_DOWN]:
                if y < 480:
                    y += vel
                    key.append('DOWN')

        else:
            if keys[pygame.K_LEFT] and key[len(key) - 1] != 'RIGHT':
                if x > 0:
                    x -= vel
                    key.append('LEFT')
            elif keys[pygame.K_RIGHT] and key[len(key) - 1] != 'LEFT':
                if x < 480:
                    x += vel
                    key.append('RIGHT')

            elif keys[pygame.K_UP] and key[len(key) - 1] != 'DOWN':
                if y > 0:
                    y -= vel
                    key.append('UP')

            elif keys[pygame.K_DOWN] and key[len(key) - 1] != 'UP':
                if y < 480:
                    y += vel
                    key.append('DOWN')

        if extra_food_random == False and (extra_food_time_start) < 5:
            if food == extra_food_selection[0]:
                random_no = random.randint(1, 2)
                print(food, random_no)
                extra_food_selection.remove(extra_food_selection[0])
                if random_no == 2:
                    extra_food_random = False


        if extra_food_random == True and (int(time.time()) - extra_food_time_start) < 5:
            if extra_food_collision(x, y, extra_food_x, extra_food_y) == True:
                extra_food_random = False
                food += 5

        if collision(x, y, food_x, food_y) == True:
            food_x = random.randint(20, 480)
            food_y = random.randint(20, 480)
            extra_food_random = False
            food += 1

        for repeat in range(food + 1):
            if repeat > 5:
                if x != 0 and y != 0 and x != 480 and y != 480:
                    (a, b) = path[len(path) - (1 * (repeat + 1))]
                    if self_collision(x, y, a, b) == True:
                        print(x, y)
                        pygame.quit()


        redraw()
pygame.quit()
