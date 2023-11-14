import pygame
import math
import random

class Player():

    def __init__(self, x, y, width, height):
        """Take in player arguments and store original position"""
        #story original position in a variable
        self.x = self.original_x = x
        self.y = self.original_y = y

        self.rect = pygame.Rect(x, y, width, height)
        #player speed must be 0 unless a key is pressed
        self.player_speed = 0
        self.player_score = 0


    def move(self, speed):
        """Change speed on y axis based on what key was pressed"""
        if speed == 7:
            self.player_speed += 7
        elif speed == -7:
            self.player_speed -= 7

    def draw(self, screen):
        pygame.draw.rect(screen, (255,255,255), self.rect)

    
    def score(self):
        self.player_score += 1
