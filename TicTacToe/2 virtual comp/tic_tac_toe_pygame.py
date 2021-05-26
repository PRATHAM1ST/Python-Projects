import pygame
import Comp2
from random import randint

pygame.init()

def lines():
    pygame.draw.line(bg, (200, 200, 200), [275, 50], [275, 650], 1)
    pygame.draw.line(bg, (200, 200, 200), [475, 50], [475, 650], 1)
    pygame.draw.line(bg, (200, 200, 200), [75, 250], [675, 250], 1)
    pygame.draw.line(bg, (200, 200, 200), [75, 450], [675, 450], 1)

    pygame.draw.line(bg, (0, 0, 0), [750, 25], [750, 225], 1)
    pygame.draw.line(bg, (0, 0, 0), [750, 225], [1250, 225], 1)

    pygame.draw.line(bg, (0, 0, 0), [750, 375], [750, 675], 1)
    pygame.draw.line(bg, (0, 0, 0), [750, 675], [1250, 675], 1)
    #pygame.draw.line(bg, (0, 0, 200), [750, 675], [1250, 375], 1)

    if len(line_points) >= 2:
        for i in range(len(line_points)- 1):
            pygame.draw.line(bg, (0, 0, 0), line_points[i], (line_points[i][0], line_points[i][1] + 200), 1)
        for i in range(len(exp_points)- 1, 1, -1):
            pygame.draw.line(bg, (0, 0, 0), exp_points[i], exp_points[i - 1], 1)

def redraw():
    pygame.draw.rect(bg, black, [75, 50, 600, 600], 0)
    lines()
    win_text = font.render('Win: ' + str(win), 1, (0, 0, 0))
    lose_text = font.render('Lose: ' + str(lose), 1, (0, 0, 0))
    draw_text = font.render('Draw: ' + str(draw), 1, (0, 0, 0))
    graph = font.render('Win Graphs with No. Of Games Played', 1, (0, 0, 0))
    bg.blit(win_text, (0, 0))
    bg.blit(lose_text, (250, 0))
    bg.blit(draw_text, (500, 0))
    bg.blit(graph, (775, 275))
    pos = [(75, 50), (275, 50), (475, 50), (75, 250), (275, 250), (475, 250), (75, 450), (275, 450), (475, 450)]
    for i in range(9):
        if plane[i] == 'x':
            x = pygame.image.load('x.png')
            x = pygame.transform.scale(x, (200, 200))
            bg.blit(x, pos[i])

        if plane[i] == 'o':
            o = pygame.image.load('o.png')
            o = pygame.transform.scale(o, (200, 200))
            bg.blit(o, pos[i])

    pygame.display.update()

font = pygame.font.SysFont("Century Gothic", 25, True)
plane = ["_", "_", "_", "_", "_", "_", "_", "_", "_"]
win = 0
lose = 0
draw = 0
count = 1
max_count = 1000
n = 0
f = 'x'
g = 'o'
graph_x = (500 / max_count)
graph_line_y = 25
graph_exp_y = (300 / max_count)
line_points = []
exp_points = []
comp_u = []
white = (255, 255, 255)
black = (0, 0, 0)

bg = pygame.display.set_mode((1350, 700), 0, 32)
pygame.display.set_caption("Tic Tac Toe")

run = True
clock = pygame.time.Clock()


while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    try:
        if n == 0:
            while True:
                choice = randint(1, 10)
                if choice % 2 == 0:
                    f = 'o'
                    g = 'x'
                    break
                else:
                    f = 'x'
                    g = 'o'
                    break

        user = Comp2.comp2(plane, comp_u, n, f, g)
        if user in list(range(1, 10)) and plane[user - 1] == '_':
            plane[user - 1] = f

        if Comp2.check(plane, f, g) == f:
            exp_points.append(((750 + (graph_x * (count))), 675 - (graph_exp_y * (count - win))))
            line_points.append(((count * graph_x) + 750, graph_line_y))
            count += 1
            win += 1
            askforagain = 'y' if count <= max_count else 'n'
            if askforagain == 'y':
                plane = ["_", "_", "_", "_", "_", "_", "_", "_", "_"]
                n = 0
                end
            else:
                break

        if n == 0:
            while True:
                b = randint(0, 8)
                if b != user - 1:
                    plane[b] = g
                    comp_u.append(b)
                    n += 1
                    break

        if plane.count('_') <= 1:
            exp_points.append((750 + (graph_x * (count)), 675 - (graph_exp_y * (count - win))))
            count += 1
            draw += 1
            askforagain = 'y' if count <= max_count else 'n'
            if askforagain == 'y':
                plane = ["_", "_", "_", "_", "_", "_", "_", "_", "_"]
                n = 0
                end
            else:
                break

        a = Comp2.check(plane, f, g)
        if a != None:
            if a[1] == 2:
                for i in a[0]:
                    if plane[i] == "_":
                        plane[i] = g
                        comp_u.append(i)

        if plane.count(g) < plane.count(f):
            while True:
                b = randint(0, 8)
                if plane[b] == '_':
                    plane[b] = g
                    break

        if check(plane, f, g) == g:
            count += 1
            lose += 1
            line_points.append(((graph_x*count) + 850, -(graph_line_y*count)))
            askforagain = 'y' if count <= max_count else 'n'
            if askforagain == 'y':
                plane = ["_", "_", "_", "_", "_", "_", "_", "_", "_"]
                n = 0
                end
            else:
                break
    except:
        print(end = '')

    bg.fill(white)

    redraw()

    clock.tick(60)

pygame.quit()
