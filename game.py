import sys
import os
import random

import math
import numpy as np
import pygame


pygame.init()

SCREEN_SIZE = np.array([1000, 800])
BG_COLOR = (0, 0, 0)
RED = (255, 0, 0)
YELLOW = (255, 255, 102)
FONT_STYLE = pygame.font.SysFont(None, 50)

game_over = False

screen = pygame.display.set_mode(SCREEN_SIZE)
pygame.display.set_caption('Snake <change the name> game by ... <our incredible team>')

# clock = pygame.time.Clock()

class Game:
    
    def __init__(self, screen):
        self.screen = screen
        self.snake = [Snake()]
        self.nucleotides = [Nucleotide('A'),
                            Nucleotide('G'),
                            Nucleotide('C'),
                            Nucleotide('T'),
                            Nucleotide('U')]
        self.aminoacids = []
        self.seq = []
    
    def message(self, msg, color):
        mesg = FONT_STYLE.render(msg, True, color)
        self.screen.blit(mesg, [SCREEN_SIZE[0]/2, SCREEN_SIZE[1]/2])
        pygame.display.update()
    
    def handle_events(self):
        
        global game_over
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_q:
                    sys.exit()
                if event.key == pygame.K_a:
                    game_over = False
                    self.run()
    
    def draw(self, object_list):
        self.screen.fill(BG_COLOR)
        for objects in object_list:
            for obj in objects:
                self.screen.blit(obj.image, obj.rect)
    
    def move_objects(self, object_list):
        for objects in object_list:
            for obj in objects:
                obj.move()
                
    def Your_sequence(self, seq):
        value = FONT_STYLE.render("Your sequence: " + "".join(seq), True, YELLOW)
        self.screen.blit(value, [20, 20])
    
    def run(self):
        
        global game_over
        
        while not game_over:
            self.handle_events()
            self.draw([self.snake, self.nucleotides])
            self.move_objects([self.snake])
            self.Your_sequence(self.seq)
            pygame.display.update()
        else:
            self.screen.fill(BG_COLOR)
            self.message("You lost", RED)
            
class Snake:
    
    def __init__(self):
        # initial postition is in the center of the screen
        self.pos = np.array([SCREEN_SIZE[0] / 2, SCREEN_SIZE[1] / 2])
        self.original_image = pygame.image.load(os.path.join("images", "snake.png"))
        self.original_image = pygame.transform.scale(self.original_image, (100, 130))
        self.image = self.original_image
        self.speed = np.array([0.0, 0.0])
        self.rect = self.image.get_rect(center=self.pos)
    
    def move(self):
        # follow the mouse
        global game_over
        
        mouse_pos = pygame.mouse.get_pos()
        direction = mouse_pos - self.pos
        angle = self.calculate_angle(mouse_pos)
        self.speed = direction / 30
        self.pos += self.speed
        
        # check the boundaries
        if (self.pos >= SCREEN_SIZE - 30).any() or (self.pos <= np.zeros(2) + 30).any():
            game_over = True
            
        self.image = pygame.transform.rotate(self.original_image, int(angle))
        self.rect = self.image.get_rect(center=self.pos)
    
    def calculate_angle(self, mouse_pos):
        rel_x, rel_y = mouse_pos - self.pos
        angle = math.degrees(-math.atan2(rel_y, rel_x)) - 90
        return angle


class Nucleotide:
    
    def __init__(self, name):
        self.pos = np.array([int(random.randrange(150, SCREEN_SIZE[0] - 150)),
                             int(random.randrange(150, SCREEN_SIZE[1] - 150))])
        self.image = pygame.image.load(os.path.join("images", name + ".png"))
        self.image = pygame.transform.scale(self.image, (100, 100))
        self.rect = self.image.get_rect(center=self.pos)


class Aminoacid:
    pass


game = Game(screen)
game.run()


# clock.tick(30)
