import pygame
import numpy as np
from settings import *

class Tile(pygame.sprite.Sprite):
    def __init__(self, pos,color):
        # super().__init__(groups)
        # self.image = pygame.image.load().convert_alpha()
        display_surface = pygame.display.get_surface()

        self.rect = pygame.Rect(pos, pixel_ratio)

        pygame.draw.rect(display_surface, color, self.rect)
        