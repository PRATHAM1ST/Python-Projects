from random import *

################################################################################

def split(word):
    return [char for char in word]

def seperator(list1, list2):
    for i in range(len(list1)):
        for a in range(len(list1)):
            if i <= a:
                if list1[i] != 'A' and list1[i] != 'E' and list1[i] != 'O' and list1[i] != 'I' and list1[i] != 'U' and list1[i] != ' ' and list1[i] != '|' and list1[a] != 'A' and list1[a] != 'E' and list1[a] != 'O' and list1[a] != 'I' and list1[a] != 'U' and list1[a] != ' ' and list1[a] != '|':
                    if list1[i] == list1[a]:
                        list2.append(list1[i])
                        break
                    else:
                        list2.append(list1[a])
                        break
            if i == 0:
                if list1[i] != 'A' and list1[i] != 'E' and list1[i] != 'O' and list1[i] != 'I' and list1[i] != 'U' and list1[i] != ' ' and list1[i] != '|' and list1[a] != 'A' and list1[a] != 'E' and list1[a] != 'O' and list1[a] != 'I' and list1[a] != 'U' and list1[a] != ' ' and list1[a] != '|':
                    if list1[i] == list1[a]:
                        list2.append(list1[i])
                        break
                    else:
                        list2.append(list1[i])
                        break

    LIST_1 = duplicate_finder(list2)

    for i in range(len(LIST_1)):
        remover(list2, LIST_1[i])

    list2 += LIST_1



def duplicate_finder(list):
    LIST= []

    for i in range(len(list)):
        for a in range(len(list)):
            if i < a:
                if list[i] == list[a]:
                    LIST.append(list[i])
                    break

    x = 0
    y = 0
    while (x + 1):
        if x < len(LIST):
            while (y + 1):
                if y < len(LIST):
                    if x < y:
                        if LIST[x] == LIST[y]:
                            LIST.remove(LIST[y])
                else:
                    break
                y += 1
        else:
            break
        x += 1

    return LIST

def remover(list, input):
    x = 0
    while (x + 1):
        if x < len(list):
            if list[x] == input:
                list.remove(list[x])
        else:
            return
        x += 1

def rules():
    print('')
    print('Rules Are Simple, You Will Be Provided By:')
    print('1. Question With Gaps And Vowels Written.')
    print('2. You Just Have To Write A Letter Or The Number Which You Have Gussed.')
    print('3. NINE Tries Will Be Given To You.')
    print('4. At Last TWO Free Hints Are Given To You To Find The Name. For Applying Hint Type Hint.')
    print('5. Each Time You Write Hint No. Of Hints Get Deducted, Even If You Have Used It Earlier. So Try To Avoid Such Things.')
    print('6. Be Careful In Typing, As It May Cause You To Loose The No. Of Tries.')
    print('')

def movies_list_type():
    print('')
    print('TYPES OF MOVIES AVILABLE, For Applying Any One Them Write Their Corresponding Letter')
    print('BOLLYWOOD = b            HOLLYWOOD = h           TOLLYWOOD = t')
    print("MARVEL = m               DC = d                  EARLY 90'S = e")
    print('You Can Even Add By TYping It Without Space.')
    print('')

################################################################################
print('                                         Welcome To The World Of Finding Movies Names')
print('                                                     So Here We Begins!')
print('                                                    ENJOY AND GOOD LUCK!')
print('')

################################################################################

BOLLYWOOD = ['PANGA', 'STREET DANCER 3D', 'LAAL KAPTAAN', 'DABANGG 3', 'TANHAJI THE UNSUNG WARRIOR', 'GOOD NEWWZ', 'ANDHADHUN', 'ARTICLE 15', 'BAADSHAHO', 'BADHAAI HO', 'BALA', 'DREAM GIRL', 'GULLY BOY', 'JUDGEMENTALL HAI KYA', 'KESARI', 'PAGALPANTI', 'PATI PATNI AUR WOH', 'SAAHO', 'SIMMBA', 'WAR', 'JAWAANI JAANEMAN', 'MALANG', 'CHHAPAAK', 'PANIPAT', 'COMMANDO 3', 'MARJAAVAAN', 'HOUSEFULL 4', 'MADE IN CHINA', 'THE ACCIDENTAL PRIME MINISTER', 'TOTAL DHAMAAL', 'LUKA CHUPPI', 'SONCHIRIYA',         'BADLA', 'NOTEBOOK', 'GONE KESH', 'ROMEO AKBAR WALTER', 'KALANK', 'BLANK', 'STUDENT OF THE YEAR 2', 'DE DE PYAAR DE', 'BHARAT', 'KABIR SINGH', 'ARTICLE 15', 'SUPER 30', 'BATLA HOUSE', 'MISSION MANGAL', 'SAAHO', 'CHHICHHORE', 'DREAM GIRL', 'SECTION 375', 'THE ZOYA FACTOR', 'PAL PAL DIL KE PAAS', 'PRASSTHANAM', 'THE SKY IS PINK', 'SAAND KI AANKH', 'MADE IN CHINA', 'DRIVE', 'UJDA CHAMAN', 'MARDAANI 2', 'BAAGHI 2']
HOLLYWOOD = ['FAST AND FURIOUS']
DC = ['DARK KNIGHT']
TOLLYWOOD = []
EARLY_90s = []

################################################################################

MOVIES = []

################################################################################

CHOICE = input('WHICH TYPE OF MOVIE YOU WOULD LIKE TO HAVE : ')
CHOICE = CHOICE.upper()
if CHOICE == 'RULES':
    rules()
elif CHOICE == 'LIST':
    movies_list_type()
else:
    CHOICE = split(CHOICE)
    for c in range(len(CHOICE)):
        if CHOICE[c] == 'B':
            MOVIES += BOLLYWOOD
        elif CHOICE[c] == 'H':
            MOVIES += HOLLYWOOD
        elif CHOICE[c] == 'T':
            MOVIES += TOLLYWOOD
        elif CHOICE[c] == 'M':
            MOVIES += MARVEL
        elif CHOICE[c] == 'D':
            MOVIES += DC
        elif CHOICE[c] == 'E':
            MOVIES += EARLY_90s
        else:
            print('YOU HAVE WRITTEN IT WRONG, TRY AGAIN BY REFRESHING IT PAGE')

################################################################################

SELECTION = randint(0, len(MOVIES)-1)
SELECTED_MOVIE = MOVIES[SELECTION]
SPLIT = split(SELECTED_MOVIE)
print(SELECTED_MOVIE)
QUESTION = []
ENTERIES_NEEDED = []
TRIES_LEFT = 9
CORRECT = 0
HINTS_LEFT = 2

################################################################################

seperator(SPLIT, ENTERIES_NEEDED)

################################################################################

print('')
print('NO. OF TRIES LEFT:', TRIES_LEFT)
print('NO. OF HINTS LEFT:', HINTS_LEFT)
print('')

################################################################################

for i in range(len(SELECTED_MOVIE)):
    if SELECTED_MOVIE[i] == 'A' or SELECTED_MOVIE[i] == 'E' or SELECTED_MOVIE[i] == 'I' or SELECTED_MOVIE[i] == 'O' or SELECTED_MOVIE[i] == 'U':
        print(SELECTED_MOVIE[i], end = ' ')
        QUESTION.append(SELECTED_MOVIE[i])
    elif SELECTED_MOVIE[i] == ' ':
        print('| ', end = '')
        QUESTION.append('|')
        SPLIT[i] = '|'
    else:
        print('_ ', end = '')
        QUESTION.append('_')
print('')

################################################################################

INPUT = []

while TRIES_LEFT:
    USER = input('WRITE YOUR GUESS : ')
    USER = USER.upper()
    INPUT.append(USER)
    if USER != 'A' and USER != 'E' and USER != 'I' and USER != 'O' and USER != 'U' and USER != ' ':
        if USER == 'HINT':
            if HINTS_LEFT != 0:
                print('YOUR HINT IS {} NOW YOU HAVE {} HINTS LEFT!, LETS ROCK IT BRO!'.format(ENTERIES_NEEDED[0], HINTS_LEFT - 1))
                HINTS_LEFT -= 1
            else:
                print('SORRY YOU CANNOT USE MORE THAN 3 HINTS, TRY HARD NAD DONT LOOSE HOPE')
        if QUESTION != SPLIT:
            for i in range(len(SELECTED_MOVIE)):
                    if USER == SELECTED_MOVIE[i]:
                        remover(ENTERIES_NEEDED, USER)
                        CORRECT += 1
            if CORRECT != 0:
                for i in range(len(SELECTED_MOVIE)):
                    if USER == SELECTED_MOVIE[i] and USER != ' ':
                        QUESTION[i] = USER
                for a in QUESTION:
                    print(a, end = ' ')
                print('')
                CORRECT = 0
            elif USER != 'HINT':
                TRIES_LEFT -= 1
                print('YOU HAVE', TRIES_LEFT, ' TRIES LEFT, HURRY UP TRY HARD!')
                print('')
        if QUESTION == SPLIT:
            print('')
            print('YOU HAVE CRACKED THE MOVIE, HURRAY! BRO PARTY!')
            break
        if TRIES_LEFT == 0:
            print('SORRY YOU HAVE RUN OUT OF TRIES!, BETTER LUCK NEXT TIME AND COME PREPARED WELL!')
            print('')
            print('THE MOVIE IS', MOVIES[SELECTION])
            break
        print('')

    else:
        print('SORRY VOWELS OR SPACES ARE NOT ALLOWED, GROW UP BUDDY!')
        print('')

################################################################################
