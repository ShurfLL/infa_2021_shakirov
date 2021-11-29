import math
from random import choice
from random import randint as rnd
import pygame


FPS = 30

RED = 0xFF0000
BLUE = 0x0000FF
YELLOW = 0xFFC91F
GREEN = 0x00FF00
MAGENTA = 0xFF03B8
CYAN = 0x00FFCC
BLACK = (0, 0, 0)
WHITE = 0xFFFFFF
GREY = 0x7D7D7D
GAME_COLORS = [RED, BLUE, YELLOW, GREEN, MAGENTA, CYAN]

WIDTH = 800
HEIGHT = 600

g=0.7

class AbstractBall:
    def __init__(self, screen: pygame.Surface, x=40, y=450, r=10):
        self.screen = screen
        self.x = x
        self.y = y
        self.r = r
        self.vx = 0
        self.vy = 0
        self.color = choice(GAME_COLORS)
        self.live = 200

    def move(self):
        self.x += self.vx
        self.y -= self.vy
        self.vy -= g
        if(self.y > HEIGHT-self.r):
            self.y = HEIGHT-self.r
            self.vy *= -0.7

    def draw(self):
        pygame.draw.circle(
            self.screen,
            self.color,
            (self.x, self.y),
            self.r
        )

    def hittest(self, obj):
        return ((self.x-obj.x)**2+(self.y-obj.y)**2 <= (self.r+obj.r)**2)


class Gun_ball(AbstractBall):
    def __init__(self, screen, x, y):
        super().__init__(screen, x, y, 15)


class Target_ball(AbstractBall):
    def __init__(self, screen, x, y):
        super().__init__(screen, x, y, 20)
        self.color = GREY


class Gun:
    def __init__(self, screen, x=40, y=550):
        self.screen = screen
        self.f2_power = 10
        self.f2_on = 0
        self.an = 1
        self.color = BLACK
        self.x = x
        self.y = y
        self.r = 40
        self.vx = 5
        self.vy = 5
        self.move_left = 0
        self.move_right = 0

    def get_move(self, event):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                self.move_left = 1
            if event.key == pygame.K_RIGHT:
                self.move_right = 1
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT:
                self.move_left = 0
            if event.key == pygame.K_RIGHT:
                self.move_right = 0

    def move(self):
        if self.move_left:
            self.x -= self.vx
        if self.move_right:
            self.x += self.vx

    def fire2_start(self, event):
        self.f2_on = 1

    def fire2_end(self, event):
        new_ball = Gun_ball(self.screen, self.x, self.y)
        self.an = math.atan2(
            (event.pos[1]-self.y), (event.pos[0]-self.x))
        new_ball.vx = self.f2_power * math.cos(self.an)
        new_ball.vy = - self.f2_power * math.sin(self.an)
        self.f2_on = 0
        self.f2_power = 10
        return new_ball

    def targetting(self, event):
        if event:
            self.an = math.atan2(
            (event.pos[1]-self.y), (event.pos[0]-self.x))
        if self.f2_on:
            self.color = RED
        else:
            self.color = BLACK

    def draw(self):
        width = 10
        coords = [
            (self.x, self.y),
            (self.x+(self.f2_power+20)*math.cos(self.an),
             self.y+(self.f2_power+20)*math.sin(self.an)),
            (self.x+(self.f2_power+20)*math.cos(self.an)+width*math.sin(self.an),
             self.y+(self.f2_power+20)*math.sin(self.an)-width*math.cos(self.an)),
            (self.x+width*math.sin(self.an), self.y-width*math.cos(self.an))
        ]
        pygame.draw.polygon(self.screen, self.color, ((self.x-self.r, self.y-10), 
            (self.x-self.r, self.y+self.r), (self.x+self.r, self.y+self.r), 
            (self.x+self.r, self.y-10)))
        pygame.draw.polygon(self.screen, self.color, (coords))

    def power_up(self):
        if self.f2_on:
            if self.f2_power < 100:
                self.f2_power += 1
                self.color = RED
        else:
            self.color = BLACK


class AbstractTarget:
    def __init__(self, x, y, r):
        self.x = x
        self.y = y
        self.r = r
        self.vx = rnd(1, 7)
        self.vy = rnd(-7, 7)
        self.color = choice(GAME_COLORS)
        self.live = 1

    def hit(self):
        self.live -=1

    def draw(self):
        pass

    def move(self):
        self.x += self.vx
        self.y += self.vy

    def collision(self):
        if(self.x + self.r > WIDTH):
            self.vx *= -1
            self.x = WIDTH-self.r
        elif(self.x - self.r < 0):
            self.vx *= -1
            self.x = self.r
        elif(self.y - self.r < 0):
            self.vy *= -1
            self.y = self.r
        elif(self.y + self.r > HEIGHT):
            self.vy *= -1
            self.y = HEIGHT-self.r


class CircleTarget(AbstractTarget):
    def __init__(self, x, y, r):
        super().__init__(x, y, r)

    def draw (self):
        self.color = choice(GAME_COLORS)
        pygame.draw.circle(
            screen,
            self.color,
            (self.x, self.y),
            self.r)


class UfoTarget(AbstractTarget):
    def __init__(self, x, r):
        super().__init__(x, 50, r)
        self.live = 3
        self.fire_time = 30
        self.color = GREY

    def move (self):
        self.x += self.vx

    def fire(self):        
        new_ball = Target_ball(screen, self.x, self.y)
        new_ball.live = 40
        return new_ball

    def draw (self):
        pygame.draw.rect(
            screen,
            self.color,
            (self.x-self.r, self.y-self.r/8,
             self.r*2, self.r/4))
        pygame.draw.circle(
            screen,
            self.color,
            (self.x, self.y),
            self.r/2 )


def draw_text(text, x_cord, y_cord, size, color):
    '''Отрисовывает текст

    отрисовывает text от точки (x_cord, y_cord)
    с размером шрифта size и цветом color
    '''
    font = pygame.font.Font(None, size)
    text1 = font.render(text, True, color)
    screen.blit(text1, (x_cord, y_cord))
    pygame.display.update()


def draw_points(points):
    draw_text('Your points:'+str(points), 0, 0, 24, BLACK)


pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
bullet = 0
points = 0
balls = []

clock = pygame.time.Clock()
gun = Gun(screen)
target1 = CircleTarget(rnd(600, 780), rnd(300, 550), rnd(15,50))
target2 = UfoTarget(rnd(600, 780), rnd(15,50))
finished = False

while not finished:
    screen.fill(WHITE)
    gun.draw()
    target2.move()
    target1.move()
    target2.collision()
    target1.collision()
    target1.draw()
    target2.draw()
    for b in balls:
        b.draw()
    gun.move()
    draw_points(points)
    pygame.display.update()
    if target2.fire_time >= 30:
        target2.fire_time = 0
        balls.append(target2.fire())
    else:
        target2.fire_time += 1
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True
        elif event.type == pygame.MOUSEBUTTONDOWN:
            gun.fire2_start(event)
        elif event.type == pygame.MOUSEBUTTONUP:
            balls.append(gun.fire2_end(event))
        elif event.type == pygame.MOUSEMOTION:
            gun.targetting(event)
        gun.get_move(event)

    for b in balls:
        b.move()
        b.live -= 1
        if (b.hittest(gun) and type(b)==Target_ball):
            balls.remove(b)
            points -= 5
        if b.live <= 0:
            balls.remove(b)
        elif type(b) == Gun_ball and b.hittest(target1):
            target1.hit()
            if target1.live <= 0:
                points += 1
                target1 = CircleTarget(rnd(600, 780), rnd(300, 550), rnd(15, 50))
            balls.remove(b)
        elif type(b) == Gun_ball and b.hittest(target2):
            target2.hit()
            if target2.live <= 0:
                points += 3
                target2 = UfoTarget(rnd(600, 780), rnd(15, 50))
            balls.remove(b)
    gun.power_up()

pygame.quit()