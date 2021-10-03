import pygame
from pygame.draw import *

pygame.init()

FPS = 30
screen = pygame.display.set_mode((800, 800))
screen.fill('grey')
circle(screen, (255, 255, 0), (800/2, 800/2), 800/4)
circle(screen, (0, 0, 0), (800/2, 800/2), 800/4,1)
rect(screen, (0, 0, 0), (300,500,200,10))
circle(screen, (255, 0, 0), (300, 350), 40)
circle(screen, (0, 0, 0), (300, 350), 20)
circle(screen, (255, 0, 0), (500, 350), 30)
circle(screen, (0, 0, 0), (500, 350), 15)
surf=pygame.Surface((150,20))
surf=pygame.Surface.convert_alpha(surf)
rect(surf,(0,0,0),(0,0,150,20))
surf=pygame.transform.rotate(surf,-30)
screen.blit(surf,(230,250))
surf=pygame.transform.rotate(surf,60)
screen.blit(surf,(420,225))




     
pygame.display.update()
clock = pygame.time.Clock()
finished = False

while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True

pygame.quit()
