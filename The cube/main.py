import pygame
import math
import sys
pygame.init()

sc = pygame.display.set_mode((1200, 700))
pygame.display.set_caption("Huterr")

player = pygame.image.load("PL1.png")
bg = pygame.image.load("background.jpeg")

# player
jump = 4
speed = 5

#gun
Gx = 150
Gy = 552

clock = pygame.time.Clock()

run = True
correction_angle = 90
while(run):
    clock.tick(30)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    player_pos  = sc.get_rect().center
    player_rect = player.get_rect(center = player_pos)

    mx, my = pygame.mouse.get_pos()
    dx, dy = mx - player_rect.centerx, my - player_rect.centery
    angle = math.degrees(math.atan2(-dy, dx)) - correction_angle

    rot_image = pygame.transform.rotate(player, angle)
    rot_image_rect = rot_image.get_rect(center = player_rect.center)

    sc.fill((55, 55, 55))
    sc.blit(rot_image, rot_image_rect.topleft)
    pygame.display.flip()
    pygame.display.update()
    pygame.quit
