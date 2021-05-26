import pygame

pygame.init()

bg = pygame.display.set_mode((700, 700))
points = []

run = True
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

        if event.type == pygame.MOUSEBUTTONUP:
            points.append(pygame.mouse.get_pos())

    bg.fill((255, 255, 255))
    if len(points) >= 2:
        pygame.draw.polygon(bg, (0, 0, 0), points, 5)

    pygame.display.update()
