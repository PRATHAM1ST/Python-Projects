import pygame
from pygame import *
from random import *

pygame.init()

def lines():
    pygame.draw.line(bg, (200, 200, 200), [275, 50], [275, 650], 1)
    pygame.draw.line(bg, (200, 200, 200), [475, 50], [475, 650], 1)
    pygame.draw.line(bg, (200, 200, 200), [75, 250], [675, 250], 1)
    pygame.draw.line(bg, (200, 200, 200), [75, 450], [675, 450], 1)

    pygame.draw.line(bg, (0, 0, 0), [740, 25], [740, 225], 2)
    pygame.draw.line(bg, (0, 0, 0), [740, 225], [1250, 225], 2)

    pygame.draw.line(bg, (0, 0, 0), [750, 375], [750, 675], 3)
    pygame.draw.line(bg, (0, 0, 0), [750, 675], [1250, 675], 3)
    #pygame.draw.line(bg, (0, 0, 200), [750, 675], [1250, 375], 1)

    if len(line_points) >= 2:
        for i in range(len(exp_points)- 1, 1, -1):
            pygame.draw.line(bg, (200, 100, 10), exp_points[i], exp_points[i - 1], 2)

def redraw():
    pygame.draw.rect(bg, black, [75, 50, 600, 600], 0)
    lines()
    win_text = font.render('Win: ' + str(win), 1, (0, 0, 0))
    lose_text = font.render('Lose: ' + str(lose), 1, (0, 0, 0))
    draw_text = font.render('Draw: ' + str(draw), 1, (0, 0, 0))
    total_text = font.render('Total: ' + str(draw + win + lose), 1, (0, 0, 0))
    graph = font.render('Win Graphs with No. Of Games Played', 1, (0, 0, 0))
    timer = font.render('Games Played Per Sec: {}'.format(count / (end_time * 1000)), 1, (0, 0, 0))
    bg.blit(win_text, (0, 0))
    bg.blit(lose_text, (187.5, 0))
    bg.blit(draw_text, (375, 0))
    bg.blit(total_text, (562.5,0))
    bg.blit(graph, (775, 275))
    bg.blit(timer, (75, 650))

    total = win + lose + draw
    if count >= 2:
        pygame.draw.rect(bg, red, [750, 25, ((win * 500) / total), 200], 0)
        win_text1 = font.render('Win', 1, (255, 255, 255))
        bg.blit(win_text1, ((((win * 500) / total)*(0.45)) + 740, 100))

        pygame.draw.rect(bg, green, [740 + ((win * 500)/ (total)), 25, (lose * 500)/ (total), 200], 0)
        lose_text = font.render('Lose', 1, (255, 255, 255))
        bg.blit(lose_text, ((((lose * 500) / total)*(0.35)) + 740 + ((win * 500)/ (total)), 100))

        pygame.draw.rect(bg, blue, [740 + ((lose * 500)/ (total)) + ((win * 500)/ (total)), 25, (draw * 500)/ (total), 200], 0)
        if ((draw * 500)/ (total)) >= 80:
            draw_text = font.render('Draw', 1, (255, 255, 255))
            bg.blit(draw_text, ((((draw * 500) / total)*(0.5)) + 740 + ((win * 500)/ (total)) + (draw * 500)/ (total), 100))
        else:
            draw_text = font.render('Draw', 1, (0, 0, 255))
            bg.blit(draw_text, (740 + ((lose * 500)/ (total)) + ((win * 500)/ (total)), -5))


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

def check(plane, f, g):
    for a in range(0, 9, 3):
        for b in range(3):
            x = [f, f, f]
            o = [g, g, g]
            if (plane[a:a + 3] == x) or (plane[a + b :: 3] == x and a == 0) or (plane[a + b::4] == x and (a, b) == (0, 0)) or (plane[a + b:7:2] == x and (a, b) == (0, 2)):
                return f
            if (plane[a:a + 3] == o) or (plane[a + b :: 3] == o and a == 0) or (plane[a + b::4] == o and (a, b) == (0, 0)) or (plane[a + b:7:2] == o and (a, b) == (0, 2)):
                return g

bg = pygame.display.set_mode((1350, 700), 0, 32)
pygame.display.set_caption("Tic Tac Toe Random")

font = pygame.font.SysFont("Century Gothic", 25, True)
plane = ["_", "_", "_", "_", "_", "_", "_", "_", "_"]
win = 0
lose = 0
draw = 0
total = win + lose + draw
count = 1
max_count = 100
n = 0
f = 'x'
g = 'o'
graph_x = (500 / max_count)
graph_line_y = 125
graph_exp_y = (300 / max_count)
line_points = []
exp_points = []
red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)
white = (255, 255, 255)
black = (0, 0, 0)

run = True
clock = pygame.time.Clock()

start_time = pygame.time.get_ticks()
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

        user = 0
        while True:
            b = randint(0, 8)
            if plane[b] == '_':
                plane[b] = f
                n += 1
                break

        if check(plane, f, g) == f:
            exp_points.append(((750 + (graph_x * (count))), 675 - (graph_exp_y * (count - win))))
            line_points.append(((count * graph_x) + 750, graph_line_y - 100))
            win += 1
            count += 1
            askforagain = 'y' if count <= max_count else 'n'
            if askforagain == 'y':
                plane = ["_", "_", "_", "_", "_", "_", "_", "_", "_"]
                n = 0
                end
            else:
                print('')

        if plane.count('_') == 0:
            line_points.append(((count * graph_x) + 750, graph_line_y))
            exp_points.append((750 + (graph_x * (count)), 675 - (graph_exp_y * (count - win))))
            draw += 1
            count += 1
            askforagain = 'y' if count <= max_count else 'n'
            if askforagain == 'y':
                plane = ["_", "_", "_", "_", "_", "_", "_", "_", "_"]
                n = 0
                end
            else:
                print('')

        while True:
            b = randint(0, 8)
            if plane[b] == '_':
                plane[b] = g
                n += 1
                break

        if check(plane, f, g) == g:
            exp_points.append(((750 + (graph_x * (count))), 675 - (graph_exp_y * (count - win))))
            line_points.append(((count * graph_x) + 750, graph_line_y + 100))
            lose += 1
            count += 1
            askforagain = 'y' if count <= max_count else 'n'
            if askforagain == 'y':
                plane = ["_", "_", "_", "_", "_", "_", "_", "_", "_"]
                n = 0
                end
            else:
                print('')

        if plane.count('_') == 0:
            line_points.append(((count * graph_x) + 750, graph_line_y))
            exp_points.append((750 + (graph_x * (count)), 675 - (graph_exp_y * (count - win))))
            draw += 1
            count += 1
            askforagain = 'y' if count <= max_count else 'n'
            if askforagain == 'y':
                plane = ["_", "_", "_", "_", "_", "_", "_", "_", "_"]
                n = 0
                end
            else:
                print('')

    except:
        print(end = '')

    bg.fill(white)

    end_time = pygame.time.get_ticks() - start_time

    redraw()

    clock.tick(60)
