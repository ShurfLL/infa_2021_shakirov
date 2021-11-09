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

class Ball:
    def __init__(self, screen: pygame.Surface, x=40, y=450, r=10):
        self.screen = screen
        self.x = x
        self.y = y
        self.r = r
        self.vx = 0
        self.vy = 0
        self.color = choice(GAME_COLORS)
        self.live = 30

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


class Gun:
    def __init__(self, screen, x=40, y=450):
        self.screen = screen
        self.f2_power = 10
        self.f2_on = 0
        self.an = 1
        self.color = GREY
        self.x = x
        self.y = y

    def fire2_start(self, event):
        self.f2_on = 1

    def fire2_end(self, event):
        new_ball = Ball(self.screen, self.x, self.y)
        new_ball.r += 5
        self.an = math.atan2(
            (event.pos[1]-self.y), (event.pos[0]-self.x))
        new_ball.vx = self.f2_power * math.cos(self.an)
        new_ball.vy = - self.f2_power * math.sin(self.an)
        self.f2_on = 0
        #self.f2_power = 10
        return new_ball

    def targetting(self, event):
        if event:
            self.an = math.atan2(
            (event.pos[1]-self.y), (event.pos[0]-self.x))
        if self.f2_on:
            self.color = RED
        else:
            self.color = GREY

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
        pygame.draw.polygon(self.screen, self.color, (coords), width=0)

    def power_up(self):
        if self.f2_on:
            if self.f2_power < 100:
                self.f2_power += 1
                self.color = RED
        else:
            self.color = GREY


class AbstractTarget:
    def __init__(self, x, y, r):
        self.x = x
        self.y = y
        self.r = r
        self.vx = rnd(-7, 7)
        self.vy = rnd(-7, 7)
        self.color = GAME_COLORS[rnd(0, 5)]
        self.live = 1

    def hit(self, point=1):
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
        pygame.draw.circle(
            screen,
            self.color,
            (self.x, self.y),
            self.r)

class SquareTarget(AbstractTarget):
    def __init__(self, x, y, r):
        super().__init__(x, y, r)
        self.live = 3
    def draw (self):
        pygame.draw.rect(
            screen,
            self.color,
            (self.x-self.r, self.y-self.r, self.r*2,self.r*2))


pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
bullet = 0
balls = []

clock = pygame.time.Clock()
gun = Gun(screen)
target1 = CircleTarget(rnd(600, 780), rnd(300, 550), rnd(15,50))
target2 = SquareTarget(rnd(600, 780), rnd(300, 550), rnd(15,50))
finished = False

while not finished:
    screen.fill(WHITE)
    gun.draw()
    target1.draw()
    target2.draw()
    for b in balls:
        b.draw()
    pygame.display.update()

    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True
        elif event.type == pygame.MOUSEBUTTONDOWN:
            gun.fire2_start(event)
        elif event.type == pygame.MOUSEBUTTONUP:
            gun.fire2_end(event)
            balls.append(gun.fire2_end(event))
            gun.f2_power = 10
        elif event.type == pygame.MOUSEMOTION:
            gun.targetting(event)

    for b in balls:
        b.move()
        if b.hittest(target1) and target1.live:
            target1.live = 0
            target1.hit()
            target1 = CircleTarget(rnd(600, 780), rnd(300, 550), rnd(15, 50))
            balls.remove(b)
        if b.hittest(target2) and target2.live:
            target2.live = 0
            target2.hit()
            target2 = CircleTarget(rnd(600, 780), rnd(300, 550), rnd(15, 50))
            balls.remove(b)
    gun.power_up()

pygame.quit()
print(rnd(15,25))