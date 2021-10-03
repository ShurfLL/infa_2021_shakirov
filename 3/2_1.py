import pygame
import math as m
from pygame.draw import *

pygame.init()

FPS = 30
screen_size=800
screen=pygame.display.set_mode((screen_size,screen_size))
#небо+земля
rect(screen,'cyan', (0,0,screen_size,screen_size))
rect(screen,(0,200,0), (0,screen_size/2,screen_size,screen_size/2))
#дом
house=pygame.Surface((100,100))
house=pygame.Surface.convert_alpha(house)
house.fill((0,0,0,0))
rect(house,(200,100,0),(0,40,100,60))
rect(house,(0,0,0),(0,40,100,60),1)
polygon(house,'red',[(50,0),(100,40),(0,40)])
polygon(house,'black',[(50,0),(100,40),(0,40)],1)
rect(house,(80,80,250),(35,55,30,30))
rect(house,(0,0,0),(35,55,30,30),1)
#облако
cloud=pygame.Surface((100,60))
cloud=pygame.Surface.convert_alpha(cloud)
cloud.fill((0,0,0,0))
circle(cloud,'white',(40,20),20)
circle(cloud,'black',(40,20),20,1)
circle(cloud,'white',(60,20),20)
circle(cloud,'black',(60,20),20,1)
circle(cloud,'white',(20,40),20)
circle(cloud,'black',(20,40),20,1)
circle(cloud,'white',(40,40),20)
circle(cloud,'black',(40,40),20,1)
circle(cloud,'white',(60,40),20)
circle(cloud,'black',(60,40),20,1)
circle(cloud,'white',(80,40),20)
circle(cloud,'black',(80,40),20,1)
#дерево
tree=pygame.Surface((60,100))
tree=pygame.Surface.convert_alpha(tree)
tree.fill((0,0,0,0))
rect(tree,(100,50,0),(25,50,10,50))
circle(tree,(0,100,0),(30,20),20)
circle(tree,(0,0,0),(30,20),20,1)
circle(tree,(0,100,0),(20,30),20)
circle(tree,(0,0,0),(20,30),20,1)
circle(tree,(0,100,0),(40,30),20)
circle(tree,(0,0,0),(40,30),20,1)
circle(tree,(0,100,0),(30,40),20)
circle(tree,(0,0,0),(30,40),20,1)
circle(tree,(0,100,0),(20,50),20)
circle(tree,(0,0,0),(20,50),20,1)
circle(tree,(0,100,0),(40,50),20)
circle(tree,(0,0,0),(40,50),20,1)
#солнце
sun=pygame.Surface((100,100))
sun=pygame.Surface.convert_alpha(sun)
sun.fill((0,0,0,0))
r1=50
r2=45
alpha=0
number_of_rays=30
sunrays=[(0,0)]*number_of_rays
for i in range (0,number_of_rays):
    if i%2==0:
        sunrays[i]=(r1*m.cos(alpha)+50,r1*m.sin(alpha)+50)
    else:
        sunrays[i]=(r2*m.cos(alpha)+50,r2*m.sin(alpha)+50)
    alpha+=2*m.pi/number_of_rays
polygon(sun,'yellow',sunrays)
polygon(sun,'black',sunrays,1)
#отрисовка обьектов в формате screen.blit(pygame.transform.scale(название обьекта,(х размер,у размер)),(у координата,х координата))
screen.blit(pygame.transform.smoothscale(house,(200,200)),(100,300))
screen.blit(pygame.transform.smoothscale(tree,(180,250)),(500,280))
screen.blit(pygame.transform.smoothscale(cloud,(200,120)),(350,100))
screen.blit(pygame.transform.smoothscale(sun,(100,100)),(600,85))
#события
pygame.display.update()
clock = pygame.time.Clock()
finished = False

while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True

pygame.quit()
