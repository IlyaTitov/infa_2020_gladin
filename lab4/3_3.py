import pygame
from pygame.draw import *
 

def guy(people , x, y):
    '''
        The function draws people 
        
        people - type of people
        x - coordinate of people
        y - coordinate of head( for female and male is head_y, for child is head_y_child)
    '''
    k = 0
    feet(people, x, y,k )
    

    if people == 'male':
        ellipse(screen, pygame.Color(167, 147, 172), ((x - 3 * h // 22, y), (3 * h // 11, 6 * h // 11))) # draw body
        k = h // 22
    if people == 'female':
        polygon(screen, pygame.Color(255, 85, 221), ((x, head_y),
        (x - 3 * h // 22, head_y + 6 * h // 11 - h // 55), (x + 3 * h // 22, head_y + 6 * h // 11 - h // 55)))    #bodies
        
    if people == 'child_female':
        polygon(screen, pygame.Color(255, 85, 221), ((x, head_y_child),
            (x - 3 * h // 44, head_y_child + 6 * h // 22 - h // 55), (x + 3 * h // 44, head_y_child + 6 * h // 22 - h // 55))) 
    if people == 'child_male':
        ellipse(screen, pygame.Color(167, 147, 172), ((x - 3 * h // 44, head_y_child), (3 * h // 22, 6 * h // 22))) # draw body  
        k = h // 44

    head(people, x, y)
    arms(people, x)

   
def feet(people, x, y,k):
    if (people == 'female') or (people == 'male'):
        line(screen, pygame.Color("BLACK"), (x + h // 22, y + 6 * h // 11 - h // 55), (x + h // 22 + k // 3, y + 9 * h // 11))              
        line(screen, pygame.Color("BLACK"), (x - h // 22, y + 6 * h // 11 - h // 55), (x - h // 22 - k, y + 9 * h // 11))
        line(screen, pygame.Color("BLACK"), (x + h // 22 + k // 3, y + 9 * h // 11), (x + h // 22 + 4 * h // 55 + k // 3, y + 9 * h // 11))
        line(screen, pygame.Color("BLACK"), (x - h // 22 - k, y + 9 * h // 11), (x - h // 22 - 4 * h // 55 - k, y + 9 * h // 11)) 

    if people == 'child_male' or people == 'child_female':
        line(screen, pygame.Color("BLACK"), (x + h // 22, y +  2.5* h // 11 ), (x + h // 22 + k // 3, y + 4 * h // 11))              
        line(screen, pygame.Color("BLACK"), (x - h // 22, y + 2.5* h // 11 - h // 55), (x - h // 22 - k, y + 4 * h // 11))
        line(screen, pygame.Color("BLACK"), (x + h // 22 + k // 3, y + 4 * h // 11), (x + h // 11 + k // 3, y + 4 * h // 11))
        line(screen, pygame.Color("BLACK"), (x - h // 22 - k, y + 4 * h // 11), (x - h // 11 - k, y+ 4 * h // 11)) 

def head(people,x,y ):
    if (people == "child_male") or (people == "child_female"):
        circle(screen, pygame.Color(244, 227, 215), (x, y - 2 * h // 55), h // 20)
    else:
         circle(screen, pygame.Color(244, 227, 215), (x, y - 4 * h // 55), h // 10)
        

def arms(people, x):
    '''
        The function draw arms of people
        people - type of people
        x - coordinate of people
    '''
    if people == "female":
        line(screen, pygame.Color("BLACK"), (x - f * 3 * h // 110, head_y + 4 * h // 55), (x - f * 4 * h // 11, head_y + 19 * h // 55))              
        line(screen, pygame.Color("BLACK"), (x + f * 3 * h // 110, head_y + 4 * h // 55), (x + f * 23 * h // 110, head_y + 12 * h // 55))
        line(screen, pygame.Color("BLACK"), (x + f * 23 * h // 110, head_y + 12 * h // 55), (x + f * 4 * h // 11 - 9 * f, head_y + 4 * h // 55))
    elif people == "male":
        line(screen, pygame.Color("BLACK"), (x - 4 * h // 55, head_y + 4 * h // 55), (x - 16 * h // 55, head_y + 19 * h // 55))              
        line(screen, pygame.Color("BLACK"), (x + 4 * h // 55, head_y + 4 * h // 55), (x + 16 * h // 55 , head_y + 19 * h // 55))    #making arms
        if x == p[0]: #draw arm of fist male
            line(screen, pygame.Color("BLACK"), (p[0] - 16 * h // 55, head_y + 19 * h // 55), (p[0] - 16 * h // 55 - 10, head_y + 19 * h // 55 - 80))

    elif people == "child_female":
        line(screen, pygame.Color("BLACK"), (x - h // 55, head_y_child + 4 * h // 55), (x - 5*h // 55, head_y_child + 12 * h // 55))              
        line(screen, pygame.Color("BLACK"), (x +  h // 55, head_y_child + 4 * h // 55), (x + 5 * h // 55, head_y_child + 12 * h // 55))  

    elif people == "child_male":
        line(screen, pygame.Color("BLACK"), (x - 3*  h // 55, head_y_child + 4 * h // 55), (x - 5* h // 55, head_y_child + 12* h // 55))              
        line(screen, pygame.Color("BLACK"), (x +  3*h // 55, head_y_child + 4 * h // 55), (x + 5* h // 55, head_y_child + 12 * h // 55))  

    

def ice_cream(x, y, side, k):
    
 
    polygon(screen, pygame.Color(255, 204, 0), ((x, y), (x, y - 50 * k), (x + 42 * side * k, y - 25 * k)))
    circle(screen, pygame.Color(85, 0, 0), (x + 29 * side * k, y - 33 * k), 12 * k)    #side turns ice cream to the left or to the right (-1, 1) 
    circle(screen, pygame.Color(255, 0, 0), (x + 14 * side * k, y - 42 * k), 12 * k)
    circle(screen, pygame.Color(255, 255, 255), (x + 33 * side * k, y - 50 * k), 12 * k)    #making ice cream

def heart(x, y, side, k):
    
    polygon(screen, pygame.Color(255, 0, 0), ((x, y), (x, y - 50 * k), (x + 42 * side * k, y - 25 * k)))
    circle(screen, pygame.Color(255, 0, 0), (x + 29 * side * k, y - 32 * k), 15 * k)    
    circle(screen, pygame.Color(255, 0, 0), (x + 14 * side * k, y - 42 * k), 15 * k)    #making heart
    

        
    
pygame.init()

FPS = 30
HIGHT = 768
WIDTH = 1032
screen = pygame.display.set_mode((WIDTH, HIGHT))
p = [180, 250, 330, 395, 635, 720, 790, 860]    # list of  people's x coordinate 

h = 350    # height of people
head_y = 240    #y coordinate  of heads
head_y_child = 400 
f = 1    #flag for arms of the 2nd woman

screen.fill(pygame.Color(55, 200, 113))
rect(screen, pygame.Color(170, 238, 255), (0, 0, WIDTH, HIGHT // 2))    #making sky and grass

guy('male', p[0],head_y) 
guy('female', p[3],head_y)
guy('child_male', p[1], head_y_child)
guy('child_male', p[2], head_y_child)


f = -1
guy('female', p[4],head_y)
guy('child_female', p[5],head_y_child)
guy('child_female', p[6],head_y_child)
guy('male', p[7],head_y)    #making men and women

ice_cream(p[7] + 16 * h // 55, head_y + 19 * h // 55, 1, 1)
heart(p[0] - 16 * h // 55 - 10, head_y + 19 * h // 55 - 80, -1, 1)
# делаем соединение мороженного и рук
line(screen, pygame.Color("BLACK"), (p[3] + 4 * h // 11 - 9, head_y + 4 * h // 55), (p[3] + 4 * h // 11 - 9 - 10, head_y + 4 * h // 55 - 110))
ice_cream(p[3] + 4 * h // 11 - 9 - 10, head_y + 4 * h // 55 - 110, -1, 2)

pygame.display.update()
clock = pygame.time.Clock()
finished = False

while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True

pygame.quit()
