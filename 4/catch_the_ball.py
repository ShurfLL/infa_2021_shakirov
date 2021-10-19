import pygame
import random


FPS = 90
X_BORDER = 800
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
'''массив массивов, содержащих инфу о шарах в след. виде: [положение х, положение у,
   радиус, цвет(индекс в массиве выше), скорость х, скорость у]'''
BALLS_INFO = [[random.randint(50, 750), random.randint(50, 750), random.randint(10, 50),
               random.randint(0, 5), random.randint(1, 5), random.randint(1, 5)] for i in range(0, NUMBERS_OF_BALLS)]
pygame.font.init()


def draw_ball(ball_info):
    '''рисует шар по данным из массива с инфой об этом шаре'''
    pygame.draw.circle(
        screen, COLORS[ball_info[3]], (ball_info[0], ball_info[1]), ball_info[2])


def move_ball(ball_info):
    '''изменяет координату шара за условную единицу времени'''
    ball_info[0] += ball_info[4]
    ball_info[1] += ball_info[5]


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


def click_ball(ball_info, event):
    '''увеличивает кол-во очков при кликании мышкой по шарам'''
    if((ball_info[0]-event.pos[0])**2 + (ball_info[1]-event.pos[1])**2 <= ball_info[2]**2):
        global count
        count += 1
        

def show_number_of_points(points):
    '''отрисовывает счет игрока на экране'''
    font = pygame.font.Font(None, 36)
    number_of_points = 'points: '
    number_of_points+=str(points)
    text1 = font.render(number_of_points, True,'red')
    screen.blit(text1, (0, 0))


pygame.display.update()
clock = pygame.time.Clock()
finished = False


while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True
        elif event.type == pygame.MOUSEBUTTONDOWN:
            for ball_info in BALLS_INFO:
                click_ball(ball_info, event)

    for ball_info in BALLS_INFO:
        move_ball(ball_info)
        reflection_of_ball(ball_info, X_BORDER, Y_BORDER)
        draw_ball(ball_info)

    show_number_of_points(count)

    pygame.display.update()
    screen.fill('black')

pygame.quit()
