import sys
import os

import math
import numpy as np
import pygame


pygame.init()

SCREEN_SIZE = (1000, 800)
BG_COLOR = (0, 0, 0)

screen = pygame.display.set_mode(SCREEN_SIZE, pygame.RESIZABLE)
pygame.display.set_caption('Snake <change the name> game by ... <our incredible team>')


class Game:
    def __init__(self, screen):
        self.screen = screen
        self.snake = [Snake()]
        self.nucleotides = []
        self.aminoacids = []
    
    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
    
    def draw(self, object_list):
        self.screen.fill(BG_COLOR)
        for objects in object_list:
            for obj in objects:
                self.screen.blit(obj.image, obj.rect)
        pygame.display.update()
    
    def move_objects(self, object_list):
        for objects in object_list:
            for obj in objects:
                obj.move()
    
    def run(self):
        while True:
            self.handle_events()
            self.draw([self.snake])
            self.move_objects([self.snake])

class Snake:
    def __init__(self):
        # initial postition is in the center of the screen
        self.pos = np.array([SCREEN_SIZE[0] / 2, SCREEN_SIZE[1] / 2])
        self.original_image = pygame.image.load(os.path.join("images", "snake.png"))
        self.original_image = pygame.transform.scale(self.original_image, (70, 70))
        self.image = self.original_image
        self.speed = np.array([0.0, 0.0])
        self.rect = self.image.get_rect(center=self.pos)
    
    def move(self):
        # follow the mouse
        mouse_pos = pygame.mouse.get_pos()
        direction = mouse_pos - self.pos
        angle = self.calculate_angle(mouse_pos)
        self.speed = direction / 40
        self.pos += self.speed
        self.image = pygame.transform.rotate(self.original_image, int(angle))
        self.rect = self.image.get_rect(center=self.pos)
    
    def calculate_angle(self, mouse_pos):
        rel_x, rel_y = mouse_pos - self.pos
        angle = math.degrees(-math.atan2(rel_y, rel_x)) - 90
        return angle


class Nucleotide:
    pass


class Aminoacid:
    pass


game = Game(screen)
game.run()
