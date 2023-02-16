import random


color_rgb_values = {
    "red": (255,0,0),
    "blue": (0,0,255),
    "green": (0,255,0),
    "yellow": (255,0,0),
    "orange": (255,0,0),
    "purple": (255,0,0)
}

shapes = [
    "circle",
    "square",
    "triangle"
]


direction_vectors = {
    "up": (0,-1),
    "down": (0,1),
    "left": (-1,0),
    "right": (1,0)
}

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