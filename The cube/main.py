import pygame
import math
import sys

pygame.init()

sc = pygame.display.set_mode((1200, 700))
pygame.display.set_caption("Huterr")

player = pygame.image.load("PL1.png")
Cube = pygame.image.load("Stena.png")
Gun = pygame.image.load("Drobash.png")
bg = pygame.image.load("background.jpeg")

# player
x = 148
y = 550
speed = 5

#gun
Gx = 150
Gy = 552

clock = pygame.time.Clock()

run = True

while(run):
    clock.tick(30)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    #Controll Cube
    keys = pygame.key.get_pressed()
    if keys[pygame.K_d]:
        x += speed
        print("1")
    elif keys[pygame.K_a]:
        x -= speed
        print("2")
    elif keys[pygame.K_w]:
        y -= speed
        print("3")
    elif keys[pygame.K_s]:
        y += speed
        print("0")
    if keys[pygame.K_ESCAPE]:
        exit()

    sc.blit(bg, (0, 0))
    sc.blit(Gun,(Gx, Gy))
    sc.blit(player, (x, y))
    pygame.display.update()

pygame.quit()