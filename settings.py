import pygame
import numpy as np

FPS = 60
SCREEN_SIZE = (800, 800)


world_map = np.full((16, 16),1)
# world_map[0] = 1
# world_map[15] = 1
# world_map[:,0] = 1
# world_map[:,15] = 1
world_map[0,0] = 0
world_map[1,0] = 0

# exit 
world_map[world_map.shape[0] -1, world_map.shape[1] - 2:] = 0

pixel_ratio = [int(SCREEN_SIZE[0] / world_map.shape[0]), int(SCREEN_SIZE[1] / world_map.shape[1])]

# world_map[3, 5] = 2
# hero_position = np.array([3, 5])


COLORS = {
    "white": (255, 255, 255),
    "black": (0, 0, 0)
} 
# print(world_map)