from pygame.math import Vector2
import math
import pygame
import numpy as np

pygame.init()
game_map = np.full((16, 16),0)
game_map[0] = 1
game_map[15] = 1
game_map[:,0] = 1
game_map[:,15] = 1

screen_size = (800, 800)
surface = pygame.display.set_mode(screen_size)

screen_map_ratio = [int(screen_size[0] / 16), int(screen_size[1] / 16)]
print(screen_map_ratio)

SCREEN_COLORS = {
    "white": (255, 255, 255),
    "black": (0, 0, 0)
} 

game_map[3, 5] = 2
hero_position = np.array([3, 5])

print(game_map)
running = True
while running:
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            running = False
            pygame.quit() 
    surface.fill(SCREEN_COLORS['white'])

    for eye,y in enumerate(game_map):
        for ex, x in enumerate(y):
            if x == 1:
                black_rect = pygame.Rect((ex* 20, eye* 20),(20, 20))
                pygame.draw.rect(surface, (0,0,0,0),black_rect)

    pygame.display.flip()