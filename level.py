import pygame
import numpy as np
from settings import *

class Level():
    def __init__(self):
        # setup sprite groups
        self.visible_sprites = []
        self.obstacle_sprites = pygame.sprite.Group()

        # get display surface
        self.display_surface = pygame.display.get_surface
        self.make_map = True
        
    def run(self):
        self.GenerateMap()
        self.Map()
        
    # draw the map
    def Map(self):
        for row_i, row in enumerate(world_map):
            for col_i, col in enumerate(row):
                x = col_i * pixel_ratio[0]
                y = row_i * pixel_ratio[1]
                
                if col == 1:
                    Tile((x, y), COLORS['black'])
    
