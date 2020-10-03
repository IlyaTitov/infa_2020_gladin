import pygame
from pygame.draw import *

pygame.init()

FPS = 30
screen = pygame.display.set_mode((400, 400))
screen.fill(pygame.Color("GREY"))

circle(screen, pygame.Color("BLACK"), (200, 200), 101, 3)
circle(screen, pygame.Color("YELLOW"), (200, 200), 100)

circle(screen, pygame.Color("BLACK"), (165, 175), 21, 3)
circle(screen, pygame.Color("RED"), (165, 175), 20)
circle(screen, pygame.Color("BLACK"), (165, 175), 9)

circle(screen, pygame.Color("BLACK"), (230, 175), 19, 3)
circle(screen, pygame.Color("RED"), (230, 175), 18)
circle(screen, pygame.Color("BLACK"), (230, 175), 9)

rect(screen, pygame.Color("BLACK"), (150, 250, 100, 20))

polygon(screen, pygame.Color("BLACK"),
    ((114, 120), (193, 170), (196, 162), (118, 112)))

polygon(screen, pygame.Color("BLACK"),
    ((205, 161), (207, 168), (286, 139), (283, 132)))


pygame.display.update()
clock = pygame.time.Clock()
finished = False

while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True

pygame.quit()

