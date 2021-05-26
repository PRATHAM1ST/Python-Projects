import pygame
from random import *

pygame.init()

bg = pygame.display.set_mode((1200, 700))
ci = [0, 0, 0]
cii = 1
cit = 1
lines_points = []
lines_colour = []

run = True
while run:
    lines_n = len(lines_points)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    if ci != [255, 255, 255] or cii == 2:
        if cii == 1:
            if ci[0] <= 254:
                ci[0] += 1
            elif ci[1] <= 254:
                ci[1] += 1
            elif ci[2] <= 254:
                ci[2] += 1

        if cii == 2:
            if ci[2] >= 1:
                ci[2] -= 1
            elif ci[1] >= 1:
                ci[1] -= 1
            elif ci[0] >= 1:
                ci[0] -= 1
                if ci == [0, 0, 0]:
                    cii = 1
                    if cit == 3:
                        cit = 1
                    else:
                        cit += 1
    else:
        cii = 2
    if cit == 1:
        bg.fill(ci)
    if cit == 2:
        bg.fill((ci[1], ci[2], ci[0]))
    if cit == 3:
        bg.fill((ci[2], ci[0], ci[1]))

    if randint(1, 2) == 1:
        y = randint(0, 700)
        lines_points.append([[0, y], [1200, y]])
        lines_colour.append((randint(0, 255), randint(0, 255), randint(0, 255)))
    else:
        x = (randint(0, 1200))
        lines_points.append([[x, 0], [x, 700]])
        lines_colour.append((randint(0, 255), randint(0, 255), randint(0, 255)))

    for i in range(len(lines_points)):
        pygame.draw.line(bg, lines_colour[i], lines_points[i][0], lines_points[i][1], 10 - (i // 10))

    if lines_n == 100:
        lines_points.remove(lines_points[0])

    print(lines_n)
    pygame.display.update()
