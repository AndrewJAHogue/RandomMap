import pygame
import numpy as np
from settings import *
from tile import Tile

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
    
    # Randomization of the world map
    def GenerateMap(self):
        for row_i, row in enumerate(world_map):
            for col_i, col in enumerate(row):
                if self.make_map:
                    if col == 1 and row_i > 0 and col_i > 0:
                        chance = np.random.choice([0,1])
                        world_map[col_i, row_i] = chance
        

        # Ensure there's an entrance
        world_map[0,0] = 0
        world_map[1,0] = 0
        world_map[1,1] = 0
        # Ensure there's an exit
        world_map[world_map.shape[0] -1, world_map.shape[1] - 2:] = 0
        self.make_map = False
