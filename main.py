import pygame
import neat
import time
import os
import sys
import random
#Comments will be more elaborate, as this is my first time working with pygame.

def ball_animation():
    #assign ball speed
    global ball_speed_x, ball_speed_y, player1_score, player2_score
    ball.x += ball_speed_x
    ball.y += ball_speed_y

    #Reverse ball speed when collision occurs with screen or player
    if ball.top <= 0 or ball.bottom >= screen_height:
        ball_speed_y *= -1
    if ball.left <= 0:
        player1_score += 1
        restart_ball()
    if ball.right >= screen_width:
        player2_score += 1
        restart_ball()
    if ball.colliderect(player1) or ball.colliderect(player2):
        ball_speed_x *= -1

    return ball

#prevent player from going out of bounds
def player_animation():
    player1.y += player_speed
    if player1.top <= 0:
        player1.top = 0
    if player1.bottom >= screen_height:
        player1.bottom = screen_height

def restart_ball():
    global ball_speed_x, ball_speed_y
    ball.center = (screen_width/2, screen_height/2)
    ball_speed_y *= random.choice((1, -1))      
    ball_speed_x *= random.choice((1, -1))

pygame.init() #initiates all pygame modules, required for all pygame code
clock = pygame.time.Clock()

#set up main window
screen_width = 1280
screen_height = 960
screen = pygame.display.set_mode((screen_width, screen_height)) #returns a display surface object which is store in "screen"
pygame.display.set_caption('Pong') #title of window


#draw the ball and play in center of screen. 
ball = pygame.Rect(screen_width/2 - 15, screen_height/2 - 15, 30, 30) #have to subtract 15 since Rect places on top left, not center
player1 = pygame.Rect(screen_width - 20, screen_height/2 - 70, 10, 140)
player2 = pygame.Rect(10, screen_height/2 - 70, 10, 140)

#Can use RGB values for color argument or pygame.Color. Will be used for drawing objects
color = pygame.Color('white')

#define speed of the ball and player object
ball_speed_x = 6
ball_speed_y = 6
#player speed must be 0 unless a key is pressed
player_speed = 0

#displaying score
player1_score = 0
player2_score = 0
font = pygame.font.Font('freesansbold.ttf', 32)


while True:
    #pygame calls all user interactions events
    for event in pygame.event.get():
        #if window is closed, application stops
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        #player movement
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_s:
                player_speed += 7
            if event.key == pygame.K_w:
                player_speed -= 7
            if event.key == pygame.K_q:
                pygame.quit()
                sys.exit()
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_s:
                player_speed -= 7
            if event.key == pygame.K_w:
                player_speed += 7
            


    ball_animation()
    player_animation()

    #background color
    screen.fill((96,96,96))
    #Getting the ball and pongs on the screen
    pygame.draw.ellipse(screen, color, ball) #use .ellipse to turn our rectangle into a circle
    pygame.draw.rect(screen, color, player1)
    pygame.draw.rect(screen, color, player2)
    #line that seperates each side of the screen
    pygame.draw.aaline(screen, color, (screen_width/2,0), (screen_width/2, screen_height))


    player1_text = font.render(f"{player1_score}", True, color)
    screen.blit(player1_text, (660, 470))
    player2_text = font.render(f"{player2_score}", True, color)
    screen.blit(player2_text, (600, 470))


    pygame.display.flip() #Take everything from the loop and draw a picture of it
    clock.tick(60) #limits how fast the code runs