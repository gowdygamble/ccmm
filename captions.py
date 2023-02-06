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

class moving_shape_string:
    def __init__(self):
        self.color = random.randint(0,len(colors)-1)
        self.shape = random.randint(0,len(shapes)-1)
        self.direction = random.randint(0,len(directions)-1)

        s = "a " + colors[self.color] + " " + shapes[self.shape]
        s += " moving " + directions[self.direction]
        
        self.caption_string = s



mos = moving_shape_string()
print(mos.caption_string)