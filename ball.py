import pygame
import math
import random


class Ball():

    #init method that takes in arguments necessary to make the ball
    def __init__(self, x, y, width, height):
        #store original location to use for resetting ball
        self.x = self.original_x = x
        self.y = self.original_y = y

        #ball parameters
        self.rect = pygame.Rect(x, y, width, height)
        self.ball_speed_x = 6
        self.ball_speed_y = 6
        self.score_timer = None


    #method for adding the balls speed to itself
    def move(self):
        self.rect.x += self.ball_speed_x
        self.rect.y += self.ball_speed_y

    
    def draw(self, screen):
        pygame.draw.ellipse(screen, (255,255,255), self.rect)


    #set ball back to original position and modify what direction it launches in
    def restart_ball(self):
        self.rect.x = self.original_x
        self.rect.y = self.original_y

        current_time = pygame.time.get_ticks()

        if current_time - self.score_timer < 3100:
            self.ball_speed_x, self.ball_speed_y, = 0, 0
        else:
            self.ball_speed_y = 7 * random.choice((1, -1))      
            self.ball_speed_x = 7 * random.choice((1, -1))
            self.score_timer = None