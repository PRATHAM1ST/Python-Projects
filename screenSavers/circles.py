import pygame
from random import randint
import random

pygame.init()

def yr():
    x = randint(1, 2)
    if x == 1:
        return -1
    else:
        return 1

bg = pygame.display.set_mode((1500, 700))

points = []
colour = []
size = []
vel = []

run = True
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    bg.fill((255, 255, 255))
    many = randint(5, 20)
    point_x = []
    colour_x = []
    size_x = []
    vel_x = []
    for i in range(many):
        a = (randint(0, 255), randint(0, 255), randint(0, 255))
        b = [randint(0, 1495), 0]
        c = randint(5, 15)
        pygame.draw.circle(bg, a, b, c)
        point_x.append(b)
        colour_x.append(a)
        size_x.append(c)
        vel_x.append((randint(5, 15), randint(1, 200)))
    points.append(point_x)
    colour.append(colour_x)
    size.append(size_x)
    vel.append(vel_x)

    for i in range(len(points)):
        for j in range(len(points[i])):
            y = yr()
            points[i][j][0] += (y * vel[i][j][1])
            points[i][j][1] += vel[i][j][0]
            pygame.draw.circle(bg, colour[i][j], points[i][j], size[i][j])

    if len(points) == 161:
        points.remove(points[0])
        colour.remove(colour[0])
        size.remove(size[0])
        vel.remove(vel[0])

    print(len(points))
    pygame.display.update()
