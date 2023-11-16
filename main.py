import pygame
import neat
from ball import Ball
from player import Player
import sys

#Comments will be more elaborate, as this is my first time working with pygame.

def ball_animation(ball):
    #Reverse ball speed when collision occurs with screen or player
    if ball.rect.top <= 0 or ball.rect.bottom >= screen_height:
        ball.ball_speed_y *= -1
        
    if ball.rect.left <= 0:
        player1.score()
        ball.score_timer = pygame.time.get_ticks()

    if ball.rect.right >= screen_width:
        player2.score()
        ball.score_timer = pygame.time.get_ticks()

    if ball.rect.colliderect(player1) or ball.rect.colliderect(player2):
        ball.ball_speed_x *= -1


#prevent player from going out of bounds
def player_animation():
    #only need to use y since players can only move up and down
    player1.rect.y += player1.player_speed
    if player1.rect.top <= 0:
        player1.rect.top = 0
    if player1.rect.bottom >= screen_height:
        player1.rect.bottom = screen_height
    

pygame.init() #initiates all pygame modules, required for all pygame code
clock = pygame.time.Clock()


#set up main window
screen_width = 1280
screen_height = 960
screen = pygame.display.set_mode((screen_width, screen_height)) #returns a display surface object which is store in "screen"
pygame.display.set_caption('Pong') #title of window


#draw the ball and play in center of screen. 
ball = Ball(screen_width/2 - 15, screen_height/2 - 15, 30, 30) #have to subtract 15 since Rect places on top left, not center
player1 = Player(screen_width - 20, screen_height/2 - 70, 10, 140)
player2 = Player(10, screen_height/2 - 70, 10, 140)

#Can use RGB values for color argument or pygame.Color. Will be used for drawing objects
color = pygame.Color('white')

#font used for score
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
                player1.move(7)
            if event.key == pygame.K_w:
                player1.move(-7)
            if event.key == pygame.K_q:
                pygame.quit()
                sys.exit()
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_s:
                player1.move(-7)
            if event.key == pygame.K_w:
                player1.move(7)
            


    ball_animation(ball)
    ball.move()
    player_animation()

    #background color
    screen.fill((20,20,20))
    #Getting the ball and pongs on the screen
    ball.draw(screen)
    player1.draw(screen)
    player2.draw(screen)
    #line that seperates each side of the screen
    pygame.draw.aaline(screen, color, (screen_width/2,0), (screen_width/2, screen_height))


    #render the score in the middle of the screen
    player1_text = font.render(f"{player1.player_score}", True, color)
    screen.blit(player1_text, (660, 470))
    player2_text = font.render(f"{player2.player_score}", True, color)
    screen.blit(player2_text, (600, 470))
    


    #using pythons ability to change types, check if we set the timer back to None
    #if so, restart the ball.
    if ball.score_timer:
        current_time = pygame.time.get_ticks()
        if current_time - ball.score_timer < 1000:
            countdown3 = font.render("3", True, color)
            screen.blit(countdown3, (screen_width/2 - 10, screen_height/2 + 20))
        if 1000 < current_time - ball.score_timer < 2000:
            countdown2 = font.render("2", True, color)
            screen.blit(countdown2, (screen_width/2 - 10, screen_height/2 + 20))
        if 2000 < current_time - ball.score_timer < 3000:
            countdown1 = font.render("1", True, color)
            screen.blit(countdown1, (screen_width/2 - 10, screen_height/2 + 20))
        ball.restart_ball()
        


    pygame.display.flip() #Take everything from the loop and draw a picture of it
    clock.tick(60) #limits how fast the code runs