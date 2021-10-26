import pygame
import random


FPS = 100
game_time = 10000
gamer_name = ''
X_BORDER = 1600
Y_BORDER = 800
screen = pygame.display.set_mode((X_BORDER, Y_BORDER))
WHITE = (255, 255, 255)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
GREEN = (0, 255, 0)
MAGENTA = (255, 0, 255)
CYAN = (0, 255, 255)
BLACK = (0, 0, 0)
COLORS = [RED, BLUE, YELLOW, GREEN, MAGENTA, CYAN]
count = 0
NUMBERS_OF_BALLS = 10
NUMBERS_OF_SQUARES = 20
'''массив массивов, содержащих инфу о шарах в след. виде: [положение х, 
   положение у, радиус, цвет(индекс в массиве выше), скорость х, скорость у]'''
balls_info = [[random.randint(X_BORDER/16, X_BORDER-X_BORDER/16),
               random.randint(Y_BORDER/16, Y_BORDER-Y_BORDER/16),
               random.randint(X_BORDER/80, X_BORDER/16),
               random.randint(0, 5),
               random.randint(X_BORDER/800, X_BORDER/160),
               random.randint(Y_BORDER/800, Y_BORDER/160)]
              for i in range(0, NUMBERS_OF_BALLS)]
squares_info = [[random.randint(X_BORDER/16, X_BORDER-X_BORDER/16),
                 random.randint(Y_BORDER/16, Y_BORDER-Y_BORDER/16),
                 random.randint(X_BORDER/80, X_BORDER/16),
                 random.randint(0, 5),
                 random.randint(X_BORDER/800, X_BORDER/160),
                 random.randint(Y_BORDER/800, Y_BORDER/160)]
                for i in range(0, NUMBERS_OF_SQUARES)]
pygame.font.init()


def draw_ball(ball_info):
    '''рисует шар по данным из массива с инфой об этом шаре'''
    pygame.draw.circle(
        screen, COLORS[ball_info[3]], (ball_info[0], ball_info[1]),
        ball_info[2])


def draw_square(square_info):
    '''рисует square по данным из массива с инфой об этом square'''
    pygame.draw.rect(screen, COLORS[square_info[3]],
                     (square_info[0], square_info[1],
                      square_info[2], square_info[2]))


def move_ball(ball_info):
    '''изменяет координату шара за условную единицу времени'''
    ball_info[0] += ball_info[4]
    ball_info[1] += ball_info[5]


def move_square(square_info):
    '''изменяет координату square за условную единицу времени'''
    square_info[0] += square_info[4]
    square_info[1] += square_info[5]


def reflection_of_ball(ball_info, X_BORDER, Y_BORDER):
    '''отражает шар при соприкосновении со стеной'''
    if ball_info[0]+ball_info[2] > X_BORDER:
        ball_info[4] *= -1
        ball_info[0] = X_BORDER-ball_info[2]
    elif ball_info[0]-ball_info[2] < 0:
        ball_info[4] *= -1
        ball_info[0] = ball_info[2]
    elif ball_info[1]+ball_info[2] > Y_BORDER:
        ball_info[5] *= -1
        ball_info[1] = Y_BORDER-ball_info[2]
    elif ball_info[1]-ball_info[2] < 0:
        ball_info[5] *= -1
        ball_info[1] = ball_info[2]


def reflection_of_square(square_info, X_BORDER, Y_BORDER):
    '''отражает square при соприкосновении со стеной'''
    if square_info[0]+square_info[2] > X_BORDER:
        square_info[4] *= -1
        square_info[0] = X_BORDER-square_info[2]
    elif square_info[0] < 0:
        square_info[4] *= -1
        square_info[0] = 0
    elif square_info[1]+square_info[2] > Y_BORDER:
        square_info[5] *= -1
        square_info[1] = Y_BORDER-square_info[2]
    elif square_info[1] < 0:
        square_info[5] *= -1
        square_info[1] = 0


def click_ball(ball_info, event):
    '''увеличивает кол-во очков при кликании мышкой по шарам'''
    global count
    if((ball_info[0]-event.pos[0])**2 + (ball_info[1]-event.pos[1])**2
            <= ball_info[2]**2):
        count += 1
    return ((ball_info[0]-event.pos[0])**2 + (ball_info[1]-event.pos[1])**2
            <= ball_info[2]**2)


def click_square(square_info, event):
    '''увеличивает кол-во очков при кликании мышкой по square'''
    if (event.pos[0]-square_info[0] >= 0 and
            event.pos[0]-square_info[0] <= square_info[2] and
            event.pos[1]-square_info[1] >= 0 and
            event.pos[1]-square_info[1] <= square_info[2]):
        global count
        count -= 5
    return (event.pos[0]-square_info[0] >= 0 and
            event.pos[0]-square_info[0] <= square_info[2] and
            event.pos[1]-square_info[1] >= 0 and
            event.pos[1]-square_info[1] <= square_info[2])


def show_number_of_points(points):
    '''отрисовывает счет игрока на экране'''
    font = pygame.font.Font(None, 36)
    number_of_points = 'points: '
    number_of_points += str(points)
    text1 = font.render(number_of_points, True, 'red')
    screen.blit(text1, (0, 0))


def make_new_ball(ball_info):
    '''меняет характеристики шара на новые рандомные'''
    ball_info[0] = random.randint(X_BORDER/16, X_BORDER-X_BORDER/16)
    ball_info[1] = random.randint(Y_BORDER/16, Y_BORDER-Y_BORDER/16)
    ball_info[2] = random.randint(X_BORDER/80, X_BORDER/16)
    ball_info[3] = random.randint(0, 5)
    ball_info[4] = random.randint(X_BORDER/800, X_BORDER/160)
    ball_info[5] = random.randint(Y_BORDER/800, Y_BORDER/160)


def make_new_square(square_info):
    '''меняет характеристики square на новые рандомные'''
    square_info[0] = random.randint(X_BORDER/16, X_BORDER-X_BORDER/16)
    square_info[1] = random.randint(Y_BORDER/16, Y_BORDER-Y_BORDER/16)
    square_info[2] = random.randint(X_BORDER/80, X_BORDER/16)
    square_info[3] = random.randint(0, 5)
    square_info[4] = random.randint(X_BORDER/800, X_BORDER/160)
    square_info[5] = random.randint(Y_BORDER/800, Y_BORDER/160)


def draw_text(text, x_cord, y_cord, size, color):
    '''Отрисовывает текст

    отрисовывает text от точки (x_cord, y_cord)
    с размером шрифта size и цветом color
    '''
    font = pygame.font.Font(None, size)
    text1 = font.render(text, True, color)
    screen.blit(text1, (x_cord, y_cord))
    pygame.display.update()


def change_player_name(event, gamer_name):
    '''возращает имя игрока в завершающем окне'''
    if pygame.key.name(event.key) == 'backspace':
        gamer_name = gamer_name[:-1]
    else:
        gamer_name += str(event.unicode)
    return gamer_name


def get_leaderboard_from_file(file_name):
    '''Возращает массив таблицы лидеров из файла'''
    file = open(file_name, 'r')
    leaderboard = file.readlines()
    leaderboard = [line.rstrip() for line in leaderboard]
    leaderboard = [line.split() for line in leaderboard]
    leaderboard = [[line[0], int(line[1])] for line in leaderboard]
    file.close()
    return leaderboard


def sort_leaders(leaderboard):
    '''Возращает отсортированный массив списка лидеров'''
    mas = leaderboard
    for i in range(len(mas)-1):
        for j in range(len(mas)-2, i-1, -1):
            if mas[j+1][1] < mas[j][1]:
                mas[j], mas[j+1] = mas[j+1], mas[j]
    return mas


def return_leaders_to_file(leaderboard, file_name):
    '''Возращает таблицу лидеров в файл'''
    file = open(file_name, 'w')
    for player in leaderboard:
        file.write(player[0]+' '+str(player[1])+'\n')
    file.close()


pygame.display.update()
clock = pygame.time.Clock()
finished = False
while not finished:
    clock.tick(FPS)
    if game_time >= 0:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                finished = True
            elif event.type == pygame.MOUSEBUTTONDOWN:
                for ball_info in balls_info:
                    if click_ball(ball_info, event):
                        make_new_ball(ball_info)
                for square_info in squares_info:
                    if click_square(square_info, event):
                        make_new_square(square_info)

        for ball_info in balls_info:
            move_ball(ball_info)
            reflection_of_ball(ball_info, X_BORDER, Y_BORDER)
            draw_ball(ball_info)

        for square_info in squares_info:
            move_square(square_info)
            reflection_of_square(square_info, X_BORDER, Y_BORDER)
            draw_square(square_info)

        show_number_of_points(count)

        pygame.display.update()
        screen.fill('black')
        game_time -= 10
    else:
        screen.fill('black')
        draw_text('Введите ваше имя:'+gamer_name, 0, 0, 48, 'white')
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                finished = True
            elif (event.type == pygame.KEYDOWN and 
                    pygame.key.name(event.key) == 'return'):
                finished = True
                leaderboard = get_leaderboard_from_file('leaderboard.txt')
                leaderboard.append([gamer_name, count])
                leaderboard = sort_leaders(leaderboard)
                return_leaders_to_file(leaderboard, 'leaderboard.txt')
                print(leaderboard)
            elif event.type == pygame.KEYDOWN:
                gamer_name = change_player_name(event, gamer_name)


pygame.quit()
