import pygame
from pygame.draw import *

def guy(s, x):
    k = 0
    if s == 'male':
        ellipse(screen, pygame.Color(167, 147, 172), ((x - 3 * h // 22, head_y), (3 * h // 11, 6 * h // 11)))
        arms(s, x)
        k = h // 22
    if s == 'female':
        polygon(screen, pygame.Color(255, 85, 221), ((x, 240),
        (x - 3 * h // 22, head_y + 6 * h // 11 - h // 55), (x + 3 * h // 22, head_y + 6 * h // 11 - h // 55)))    #bodies
        arms(s, x)
    line(screen, pygame.Color("BLACK"), (x + h // 22, head_y + 6 * h // 11 - h // 55), (x + h // 22 + k // 3, head_y + 9 * h // 11))              
    line(screen, pygame.Color("BLACK"), (x - h // 22, head_y + 6 * h // 11 - h // 55), (x - h // 22 - k, head_y + 9 * h // 11))
    line(screen, pygame.Color("BLACK"), (x + h // 22 + k // 3, head_y + 9 * h // 11), (x + h // 22 + 4 * h // 55 + k // 3, head_y + 9 * h // 11))
    line(screen, pygame.Color("BLACK"), (x - h // 22 - k, head_y + 9 * h // 11), (x - h // 22 - 4 * h // 55 - k, head_y + 9 * h // 11))    #legs
    circle(screen, pygame.Color(244, 227, 215), (x, 240 - 4 * h // 55), h // 10)   #making heads

def arms(s, x):
    if s == "female":
        line(screen, pygame.Color("BLACK"), (x - 3 * h // 110, head_y + 4 * h // 55), (x - 4 * h // 11, head_y + 19 * h // 55))              
        line(screen, pygame.Color("BLACK"), (x + 3 * h // 110, head_y + 4 * h // 55), (x + 23 * h // 110, head_y + 12 * h // 55))
        line(screen, pygame.Color("BLACK"), (x + 23 * h // 110, head_y + 12 * h // 55), (x + 4 * h // 11, head_y + 4 * h // 55))
        line(screen, pygame.Color("BLACK"), (x + 4 * h // 11, head_y + 4 * h // 55), (x + 4 * h // 11 + 30, head_y + 4 * h // 55 - 150))
        heart(x + 4 * h // 11 + 30, head_y + 4 * h // 55 - 150, 1)
    else:
        line(screen, pygame.Color("BLACK"), (x - 4 * h // 55, head_y + 4 * h // 55), (x - 16 * h // 55, head_y + 19 * h // 55))              
        line(screen, pygame.Color("BLACK"), (x + 4 * h // 55, head_y + 4 * h // 55), (x + 16 * h // 55 , head_y + 19 * h // 55))    #making arms
        ice_cream(x - 16 * h // 55, head_y + 19 * h // 55, -1)

def ice_cream(x, y, side):
    polygon(screen, pygame.Color(255, 204, 0), ((x, y), (x, y - 100), (x + 84 * side, y - 50)))
    circle(screen, pygame.Color(85, 0, 0), (x + 58 * side, y - 65), 25)    #side turns ice cream to the left or to the right (-1, 1) 
    circle(screen, pygame.Color(255, 0, 0), (x + 28 * side, y - 83), 25)
    circle(screen, pygame.Color(255, 255, 255), (x + 65 * side, y - 100), 25)    #making ice cream

def heart(x, y, side):
    polygon(screen, pygame.Color(255, 0, 0), ((x, y), (x, y - 100), (x + 84 * side, y - 50)))
    circle(screen, pygame.Color(255, 0, 0), (x + 58 * side, y - 65), 30)    
    circle(screen, pygame.Color(255, 0, 0), (x + 28 * side, y - 83), 30)
    
    
        
    
pygame.init()

FPS = 30
HIGHT = 768
WIDTH = 1032
screen = pygame.display.set_mode((WIDTH, HIGHT))
p = [340, 680]    #x coord of people
h = 550    #size
head_y = 240    #y coord of heads

screen.fill(pygame.Color(55, 200, 113))
rect(screen, pygame.Color(170, 238, 255), (0, 0, WIDTH, HIGHT // 2))    #making sky and grass

guy('male', p[0])
guy('female', p[1])    #making man and woman

pygame.display.update()
clock = pygame.time.Clock()
finished = False

while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True

pygame.quit()
