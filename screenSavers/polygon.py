import pygame
import math
from random import randint

pygame.init()

add_3 = math.sqrt(3)

l = 400
m = 600
n = 800
o = 1000
p = 1200
ll = randint(1, 6) - 1
ml = randint(1, 6) - 1
nl = randint(1, 6) - 1
ol = randint(1, 6) - 1
pl = randint(1, 6) - 1
lc = (randint(0, 255), randint(0, 255), randint(0, 255))
mc = (randint(0, 255), randint(0, 255), randint(0, 255))
nc = (randint(0, 255), randint(0, 255), randint(0, 255))
oc = (randint(0, 255), randint(0, 255), randint(0, 255))
pc = (randint(0, 255), randint(0, 255), randint(0, 255))

bg = pygame.display.set_mode((700, 700))
clock = pygame.time.Clock()
run = True
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    bg.fill((255, 255, 255))

    point1 = [(350 - (l / 2), 350 - (l * add_3 / 2)), (350 + (l / 2), 350 - (l * add_3 / 2)), (350 + l, 350), (350 + (l / 2), 350 + (l * add_3 / 2)), (350 - (l / 2), 350 + (l * add_3 / 2)), (350 - l, 350)]
    pygame.draw.polygon(bg, lc, point1, 10)
    if ll != 5:
        pygame.draw.line(bg, (255, 255, 255), point1[ll], point1[ll + 1], 10)
    else:
        pygame.draw.line(bg, (255, 255, 255), point1[ll], point1[0], 10)
    l -= 0.5
    if l == 0:
        l = 400
        ll = randint(1, 6) - 1
        lc = (randint(0, 255), randint(0, 255), randint(0, 255))

    point2 = [(350 - (m / 2), 350 - (m * add_3 / 2)), (350 + (m / 2), 350 - (m * add_3 / 2)), (350 + m, 350), (350 + (m / 2), 350 + (m * add_3 / 2)), (350 - (m / 2), 350 + (m * add_3 / 2)), (350 - m, 350)]
    pygame.draw.polygon(bg, mc, point2, 10)
    if ml != 5:
        pygame.draw.line(bg, (255, 255, 255), point2[ml], point2[ml + 1], 10)
    else:
        pygame.draw.line(bg, (255, 255, 255), point2[ml], point2[0], 10)
    m -= 0.5
    if m == 0:
        m = 600
        ml = randint(1, 6) - 1
        mc = (randint(0, 255), randint(0, 255), randint(0, 255))

    point3 = [(350 - (n / 2), 350 - (n * add_3 / 2)), (350 + (n / 2), 350 - (n * add_3 / 2)), (350 + n, 350), (350 + (n / 2), 350 + (n * add_3 / 2)), (350 - (n / 2), 350 + (n * add_3 / 2)), (350 - n, 350)]
    pygame.draw.polygon(bg, nc, point3, 10)
    if nl != 5:
        pygame.draw.line(bg, (255, 255, 255), point3[nl], point3[nl + 1], 10)
    else:
        pygame.draw.line(bg, (255, 255, 255), point3[nl], point3[0], 10)
    n -= 0.5
    if n == 0:
        n = 800
        nl = randint(1, 6) - 1
        nc = (randint(0, 255), randint(0, 255), randint(0, 255))

    point4 = [(350 - (o / 2), 350 - (o * add_3 / 2)), (350 + (o / 2), 350 - (o * add_3 / 2)), (350 + o, 350), (350 + (o / 2), 350 + (o * add_3 / 2)), (350 - (o / 2), 350 + (o * add_3 / 2)), (350 - o, 350)]
    pygame.draw.polygon(bg, oc, point4, 10)
    if ol != 5:
        pygame.draw.line(bg, (255, 255, 255), point4[ol], point4[ol + 1], 10)
    else:
        pygame.draw.line(bg, (255, 255, 255), point4[ol], point4[0], 10)
    o -= 0.5
    if o == 0:
        o = 1000
        ol = randint(1, 6) - 1
        oc = (randint(0, 255), randint(0, 255), randint(0, 255))

    point5 = [(350 - (p / 2), 350 - (p * add_3 / 2)), (350 + (p / 2), 350 - (p * add_3 / 2)), (350 + p, 350), (350 + (p / 2), 350 + (p * add_3 / 2)), (350 - (p / 2), 350 + (p * add_3 / 2)), (350 - p, 350)]
    pygame.draw.polygon(bg, pc, point5, 10)
    if pl != 5:
        pygame.draw.line(bg, (255, 255, 255), point5[pl], point5[pl + 1], 10)
    else:
        pygame.draw.line(bg, (255, 255, 255), point5[pl], point5[0], 10)
    p -= 0.5
    if p == 0:
        p = 1200
        pl = randint(1, 6) - 1
        pc = (randint(0, 255), randint(0, 255), randint(0, 255))

    user = pygame.mouse.get_pos()

    pygame.draw.circle(bg, (255, 0, 0), user, 20)
    print(user)

    clock.tick(120)

    pygame.display.update()
