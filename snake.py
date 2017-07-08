# Author: Olufisayo Joseph Ayodele
# Description: Simple shooting game that deals with shooting targets
''' Notes: To run this program you have to have the pygame module, if not the program would not function as intented
           If you dont have pygame, you can go to this website "https://www.youtube.com/watch?v=MdGoAnFP-mU"  or 
           You are also going to need to run the following pip install color
'''

import time
import random
import pygame
from unittest.mock import right

#Pygame initialization
pygame.init()

#Color initialization
white = (255,255,255)
black = (0,0,0)
red = (255, 0, 0)
snake_color = (0, 180, 0)

#Constants intialization
x_width = 700
y_height = 500
snake_size = 14
change_rate = 5
Fps = 30

direction = "right"

smallFont = pygame.font.SysFont("comicsansms", 25) 
medFont = pygame.font.SysFont("comicsansms", 40) 
largeFont = pygame.font.SysFont("comicsansms", 80) 

#Display Screen
gameDisplay = pygame.display.set_mode((x_width, y_height))
pygame.display.set_caption('Snake Game')
    
#Snake head image
snakeImg = pygame.image.load('Snake Head.png')


def drawSnake(snake_size, snake_inc):
    #Rotate the snake head in the right direction
    if direction == "right":
        head = pygame.transform.rotate(snakeImg, 270)
    if direction == "left":
        head = pygame.transform.rotate(snakeImg, 90)
    if direction == "up":
        head = snakeImg
    if direction == "down":
        head = pygame.transform.rotate(snakeImg, 180)
    #
    
    #Snake head
    gameDisplay.blit(head, (snake_inc[-1][0], snake_inc[-1][1]))
    
    #Increase snake size
    for i in snake_inc[:-1]:
        #pygame.draw.rect(gameDisplay, red, [i[0], i[1], snake_size+2, snake_size+2])
        pygame.draw.rect(gameDisplay, snake_color, [i[0], i[1], snake_size, snake_size])   
        pygame.display.update()
    #

#Display message to the screem
def message_to_screen(msg, color, y_displace = 0, size = "small"):      
    if size == "small":
        textSurface = smallFont.render(msg, True, color)
    elif size == "medium":
        textSurface = medFont.render(msg, True, color)
    elif size == "large":
        textSurface = largeFont.render(msg, True, color)              
    #Displays a message to the center of the screen     
    text_display, textLength = textSurface, textSurface.get_rect()    
    textLength.center = (x_width/2), (y_height/2) + y_displace
    gameDisplay.blit(text_display, textLength)


def main():
    global direction
    direction = "right"    
    #Variable initializations
    snakeX = x_width/2
    snakeY = y_height/2
    x_change = 5
    y_change = 0
    gameExit = False
    gameOver = False
    snake_inc = []
    snakeLength = 10
    #Snakes food, appple x and y axis
    appleX = random.randrange(0, x_width-snake_size)
    appleY = random.randrange(0, y_height-snake_size)
    #Clock
    clock = pygame.time.Clock()
    
    #Game Play
    while not gameExit:
        #To restart or quit the game after the game is over
        while gameOver == True:
            gameDisplay.fill(white)
            message_to_screen("Game Over!", red, -50, "large")
            message_to_screen("Press R to restart, or  Q to quit", black, 50, "medium")
            pygame.display.update()
            #Key pressed
            for i in pygame.event.get():
                if i.type == pygame.KEYDOWN:
                    if i.key == pygame.K_q:     
                        gameExit = True
                        gameOver = False
                    if i.key == pygame.K_r:
                        main()
                        
        #Game events
        for i in pygame.event.get():
            if i.type == pygame.QUIT:
                gameExit = True
            #Keys pressed    
            if i.type == pygame.KEYDOWN:
                if i.key == pygame.K_LEFT:
                    direction = "left"
                    x_change =  -change_rate
                    y_change = 0
                elif i.key == pygame.K_RIGHT:
                    direction = "right"
                    x_change = change_rate
                    y_change = 0
                elif i.key == pygame.K_UP:
                    direction = "up"
                    y_change =  -change_rate
                    x_change = 0
                elif i.key == pygame.K_DOWN:
                    direction = "down"
                    y_change = change_rate
                    x_change = 0
                             
        #Movement    
        snakeX += x_change
        snakeY += y_change
                    
        #Boundary checking            
        if snakeX <= 0 or snakeX >= x_width or snakeY <= 0 or snakeY >= y_height:
            gameOver = True        
        
        #Background of the game        
        gameDisplay.fill(black)
        #Draw Apple
        apple = 14
        pygame.draw.rect(gameDisplay, red, [appleX, appleY, apple, apple])
        
        #Increasing the length of the snake
        snakeHead = []
        snakeHead.append(snakeX)
        snakeHead.append(snakeY)
        snake_inc.append(snakeHead) 
        
        if len(snake_inc)-1 > snakeLength:
            del snake_inc[0]     
            
        #Ends game if the snake bites itself    
        for eachSegment in snake_inc[:-1]:
            if eachSegment == snakeHead:
                gameOver = True
                
        #Draws the snake  
        drawSnake(snake_size, snake_inc)              
        #pygame.display.update()
        
        #Feeding the snake or collision detection
        if (snakeX >= appleX and snakeX <= appleX + apple) or (snakeX + snake_size >= appleX and snakeX + snake_size <= appleX + apple):
            if (snakeY >= appleY and snakeY <= appleY + apple) or (snakeY + snake_size >= appleY and snakeY + snake_size <= appleY + apple):
                appleX = round(random.randrange(0, x_width-snake_size)/10.0)*10.0
                appleY = round(random.randrange(0, y_height-snake_size)/10.0)*10.0              
                #snakeLength += 2
                pygame.display.update()           
        
        #Frames per second
        clock.tick(Fps)
        pygame.display.update()
        
    #Game Over message    
    gameDisplay.fill(white)
    message_to_screen("You Suck!", red, -50, "large")  
    pygame.display.update()  
    quit()
 
#Main function call        
main()

