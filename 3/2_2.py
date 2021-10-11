import pygame
import math as m


FPS = 30
SCREENSIZE = 800
GRASSGREEN = (0, 200, 0)
BLACK = (0, 0, 0)
TREEGREEN = (0, 100, 0)
BROWN = (100, 50, 0)
HOUSEBROWN = (200, 100, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
HOUSEBLUE = (80, 80, 250)
BLUE = (100, 100, 250)
YELLOW = (255, 255, 0)


screen = pygame.display.set_mode((SCREENSIZE, SCREENSIZE))
pygame.init()
pygame.draw.rect(screen, BLUE, (0, 0, SCREENSIZE, SCREENSIZE))
pygame.draw.rect(screen, GRASSGREEN, (0, SCREENSIZE / 2, SCREENSIZE, SCREENSIZE / 2))


def draw_house(xpos, ypos, xsize, ysize):
    """Draws a house on the display

    xpos, ypos - координаты левого верхнего угла изображения
    xsize, ysize - ширина и высота изобажения
    """
    house = pygame.Surface((100, 100))
    house = pygame.Surface.convert_alpha(house)
    house.fill((0, 0, 0, 0))
    pygame.draw.rect(house, HOUSEBROWN, (0, 40, 100, 60))
    pygame.draw.rect(house, BLACK, (0, 40, 100, 60), 1)
    pygame.draw.polygon(house, RED, [(50, 0), (100, 40), (0, 40)])
    pygame.draw.polygon(house, BLACK, [(50, 0), (100, 40), (0, 40)], 1)
    pygame.draw.rect(house, HOUSEBLUE, (35, 55, 30, 30))
    pygame.draw.rect(house, BLACK, (35, 55, 30, 30), 1)
    screen.blit(pygame.transform.smoothscale(house, (xsize, ysize)), (xpos, ypos))


def draw_cloud(xpos, ypos, xsize, ysize):
    """Draws a cloud made of several circles on the display

    xpos, ypos - координаты левого верхнего угла изображения
    xsize, ysize - ширина и высота изобажения
    """
    cloud = pygame.Surface((1000, 600))
    cloud = pygame.Surface.convert_alpha(cloud)
    cloud.fill((0, 0, 0, 0))
    pygame.draw.circle(cloud, WHITE, (400, 200), 200)
    pygame.draw.circle(cloud, BLACK, (400, 200), 200, 10)
    pygame.draw.circle(cloud, WHITE, (600, 200), 200)
    pygame.draw.circle(cloud, BLACK, (600, 200), 200, 10)
    pygame.draw.circle(cloud, WHITE, (200, 400), 200)
    pygame.draw.circle(cloud, BLACK, (200, 400), 200, 10)
    pygame.draw.circle(cloud, WHITE, (400, 400), 200)
    pygame.draw.circle(cloud, BLACK, (400, 400), 200, 10)
    pygame.draw.circle(cloud, WHITE, (600, 400), 200)
    pygame.draw.circle(cloud, BLACK, (600, 400), 200, 10)
    pygame.draw.circle(cloud, WHITE, (800, 400), 200)
    pygame.draw.circle(cloud, BLACK, (800, 400), 200, 10)
    screen.blit(pygame.transform.smoothscale(cloud, (xsize, ysize)), (xpos, ypos))


def draw_tree(xpos, ypos, xsize, ysize):
    """Draws a tree on the display

    xpos, ypos - координаты левого верхнего угла изображения
    xsize, ysize - ширина и высота изобажения
    """
    tree = pygame.Surface((600, 1000))
    tree = pygame.Surface.convert_alpha(tree)
    tree.fill((0, 0, 0, 0))
    pygame.draw.rect(tree, BROWN, (250, 500, 100, 500))
    pygame.draw.circle(tree, TREEGREEN, (300, 200), 200)
    pygame.draw.circle(tree, BLACK, (30, 20), 200, 10)
    pygame.draw.circle(tree, TREEGREEN, (200, 300), 200)
    pygame.draw.circle(tree, BLACK, (200, 300), 200, 10)
    pygame.draw.circle(tree, TREEGREEN, (400, 300), 200)
    pygame.draw.circle(tree, BLACK, (400, 300), 200, 10)
    pygame.draw.circle(tree, TREEGREEN, (300, 400), 200)
    pygame.draw.circle(tree, BLACK, (300, 400), 200, 10)
    pygame.draw.circle(tree, TREEGREEN, (200, 500), 200)
    pygame.draw.circle(tree, BLACK, (200, 500), 200, 10)
    pygame.draw.circle(tree, TREEGREEN, (400, 500), 200)
    pygame.draw.circle(tree, BLACK, (400, 500), 200, 10)
    screen.blit(pygame.transform.smoothscale(tree, (xsize, ysize)), (xpos, ypos))


def draw_sun(xpos, ypos, xsize, ysize, number_of_rays):
    """Draws a sun on the display

    xpos, ypos - координаты левого верхнего угла изображения
    xsize, ysize - ширина и высота изобажения
    sunrays - количество лучей
    """
    sun = pygame.Surface((100, 100))
    sun = pygame.Surface.convert_alpha(sun)
    sun.fill((0, 0, 0, 0))
    outerradius = 50
    innerradius = 30
    alpha = 100
    sunrays = [(0, 0)] * number_of_rays
    for i in range(0, number_of_rays):
        if i % 2 == 0:
            sunrays[i] = (innerradius * m.cos(alpha) + 50, innerradius * m.sin(alpha) + 50)
        else:
            sunrays[i] = (outerradius * m.cos(alpha) + 50, outerradius * m.sin(alpha) + 50)
        alpha += 2 * m.pi / number_of_rays
    pygame.draw.polygon(sun, YELLOW, sunrays)
    pygame.draw.polygon(sun, BLACK, sunrays, 1)
    screen.blit(pygame.transform.rotate(pygame.transform.smoothscale(sun, (xsize, ysize)), 30), (xpos, ypos))


draw_house(300, 300, 10, 300)
draw_tree(216, 300, 320, 280)
draw_house(150, 150, 540, 350)
draw_tree(108, 150, 690, 330)
draw_cloud(200, 120, 550, 100)
draw_cloud(100, 60, 350, 150)
draw_cloud(150, 90, 140, 100)
draw_sun(100, 100, 50, 50, 12)


pygame.display.update()
clock = pygame.time.Clock()
finished = False

while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True

pygame.quit()
