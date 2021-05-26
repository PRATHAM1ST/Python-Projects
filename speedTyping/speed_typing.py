import pygame
import time
import random_story_generator

#initiating the pygame
pygame.init()

#adding display to certain 1200px width and 700px height 
bg = pygame.display.set_mode((1200, 700))

#recording session time
session_start_minutes = 0
session_start_sec = time.clock()

run = True

#list of things to get from the keyboard
alphabet = "qwertyuiopasdfghjklzxcvbnm!_,.'"
font = pygame.font.SysFont("Century Gothic", 40, True)
font_letter_to_type = pygame.font.SysFont("Century Gothic", 70, True)

#getting the next letter before typed
next_letter = ''
#getting the typed letter
typed = '@'
i = 0

#setting the story in a list and saving it
story = random_story_generator.story()
story_list = [i for i in story]

#setting the keypad in display
def key_pad():
    for i in range(len(alphabet)):
        if i >= 0 and i <= 9:
            bg.blit(font.render(alphabet[i], 1, (75, 75, 75)), (100 * (i + 1) + 30, 450)) if story_list[0].lower() != alphabet[i] or story_list[0] != alphabet[i] else bg.blit(font.render(alphabet[i], 1, (255, 0, 0)), (100 * (i + 1) + 30, 450))

        if i >= 10 and i <= 18:
            bg.blit(font.render(alphabet[i], 1, (75, 75, 75)), (100 * (i - 9) + 80, 512.5)) if story_list[0].lower() != alphabet[i] or story_list[0] != alphabet[i] else bg.blit(font.render(alphabet[i], 1, (255, 0, 0)), (100 * (i - 9) + 80, 512.5))

        if i >= 19 and i <= 25:
            bg.blit(font.render(alphabet[i], 1, (75, 75, 75)), (100 * (i - 18) + 175, 575)) if story_list[0].lower() != alphabet[i] or story_list[0] != alphabet[i] else bg.blit(font.render(alphabet[i], 1, (255, 0, 0)), (100 * (i - 18) + 175, 575))

        if i >= 26:
            bg.blit(font.render(alphabet[i], 1, (75, 75, 75)), (100 * (i - 25) + 300, 637.5)) if story_list[0].lower() != alphabet[i] or story_list[0] != alphabet[i] else bg.blit(font.render(alphabet[i], 1, (255, 0, 0)), (100 * (i - 25) + 300, 637.5))
            if story_list[0] == " " and i == 27:
                 bg.blit(font.render(alphabet[i], 1, (255, 0, 0)), (100 * (i - 25) + 300, 637.5))

#running the loop of all things rendering and getting events
while run:
     #getting the events of keypad and mouse clicked
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_q:
                typed = 'q'

            elif event.key == pygame.K_w:
                 typed = 'w'

            elif event.key == pygame.K_e:
                 typed = 'e'

            elif event.key == pygame.K_r:
                 typed = 'r'

            elif event.key == pygame.K_t:
                 typed = 't'

            elif event.key == pygame.K_y:
                 typed = 'y'

            elif event.key == pygame.K_u:
                 typed = 'u'

            elif event.key == pygame.K_i:
                 typed = 'i'

            elif event.key == pygame.K_o:
                 typed = 'o'

            elif event.key == pygame.K_p:
                 typed = 'p'

            elif event.key == pygame.K_a:
                 typed = 'a'

            elif event.key == pygame.K_s:
                 typed = 's'

            elif event.key == pygame.K_d:
                 typed = 'd'

            elif event.key == pygame.K_f:
                 typed = 'f'

            elif event.key == pygame.K_g:
                 typed = 'g'

            elif event.key == pygame.K_h:
                 typed = 'h'

            elif event.key == pygame.K_j:
                 typed = 'j'

            elif event.key == pygame.K_k:
                 typed = 'k'

            elif event.key == pygame.K_l:
                 typed = 'l'

            elif event.key == pygame.K_z:
                 typed = 'z'

            elif event.key == pygame.K_x:
                 typed = 'x'

            elif event.key == pygame.K_c:
                 typed = 'c'

            elif event.key == pygame.K_v:
                 typed = 'v'

            elif event.key == pygame.K_b:
                 typed = 'b'

            elif event.key == pygame.K_n:
                 typed = 'n'

            elif event.key == pygame.K_m:
                 typed = 'm'

            elif event.key == pygame.K_SPACE:
                typed = " "

            elif event.key == pygame.K_COMMA:
                typed = ","

            elif event.key == pygame.K_PERIOD:
                typed = "."

            if event.key == pygame.K_LSHIFT and pygame.K_RSHIFT:
                typed = "!"
                ENJK

            if event.key == pygame.K_QUOTE:
                typed = "'"

    bg.fill((255, 255, 255))
    if i == (len(story) - 1) and typed == story[-1]:
        print('yes')
        pygame.draw.rect(bg, (255, 255, 255), [0, 0, 50, 150]) # need to work
    else:
        key_pad()

    sec_text = int(time.clock() - session_start_sec) if session_start_minutes == 0 else int(time.clock() - session_start_sec - (60 * session_start_minutes))  # need to work
    if sec_text >= 60:
        session_start_minutes += 1
    bg.blit(font.render(str(sec_text) + " seconds", 1, (200, 150, 200)), (600, 30))
    bg.blit(font.render(":", 1, (200, 150, 200)), (560, 30))
    bg.blit(font.render(str(session_start_minutes) + " minutes", 1, (200, 150, 200)), (350, 30))

    if (typed == story_list[0] or typed.upper() == story_list[0]) and i != len(story) - 1:
        print(i, typed, story[-1])
        story_list.remove(story_list[0])
        next_letter = story_list[0] if len(story_list) != 0 else " "
        i += 1

    if i != len(story) - 1:
        bg.blit(font_letter_to_type.render(story_list[0], 1, (255, 25, 130)), (455, 200))
        bg.blit(font.render(story[i + 1:], 1, (255, 100, 100)), (525, 225))





    bg.blit(font.render(story[:i], 1, (255, 100, 100)), (450 - i *  - 25, 225))

    typed_1 = '@' if  i < len(story)  else typed
    typed = typed_1
    print(typed)
    pygame.display.update()
