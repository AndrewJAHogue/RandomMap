import sys
from pygame.math import Vector2
import math
import pygame
import numpy as np
from settings import *
from level import Level

class Game:
    def __init__(self):
        pygame.init()
        self.surface = pygame.display.set_mode(SCREEN_SIZE)
        pygame.display.set_caption('Random Map Design')
        self.clock = pygame.time.Clock()
        self.running = True
        
        self.level = Level()

    def run(self):
        while self.running:
            for e in pygame.event.get():
                if e.type == pygame.QUIT:
                    self.running = False
                    pygame.quit() 
                    sys.exit()

            self.surface.fill(COLORS['white'])

            self.level.run()



            pygame.display.update()
            self.clock.tick(FPS)

if __name__ == '__main__':
    game = Game()
    game.run()


