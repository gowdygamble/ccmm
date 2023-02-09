import random

# this isn't a good structure for the caption strings
# it should be a structure, a class
# that takes numbers and fills in

colors = [
    "red",
    "blue",
    "green",
    "yellow",
    "orange",
    "purple"
]

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

directions = [
    "up",
    "down",
    "left",
    "right"
]

direction_vectors = {
    "up": (0,-1),
    "down": (0,1),
    "left": (-1,0),
    "right": (1,0)
}


class moving_shape_string:
    def __init__(self, color, shape, direction):
        self.color = colors[color]
        self.shape = shapes[shape]
        self.direction = directions[direction]

        s = "a " + self.color + " " + self.shape
        s += " moving " + self.direction
        
        self.caption_string = s


#mos = moving_shape_string()
#print(mos.caption_string)