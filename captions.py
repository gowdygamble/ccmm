import random

from constants import *


class background:
    def __init__(self, color):
        self.color = color
        self.color_rgb = color_rgb_values[color]


class moving_shape:
    def __init__(self, color, shape, direction):
        self.color = color
        self.color_rgb = color_rgb_values[color]

        self.shape = shape

        self.direction = direction
        self.direction_vector = direction_vectors[direction]

        s = "a " + self.color + " " + self.shape
        s += " moving " + self.direction
        self.caption_string = s


#mos = moving_shape_string()
#print(mos.caption_string)