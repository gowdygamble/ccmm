import captions 
import cv2
import numpy as np
import matplotlib.pyplot as plt
import math
import random

# plan:
# iterate over all combinations
# up to some maximum in case it gets crazy
# create the caption
# create the video
# save both with some id
# write id + combo to a csv
# can just write the caption to the csv...

# function
# input: object, color, direction, frames
# look up all the correct values and return the frames

def draw_circle(img, center, color):
    cv2.circle(img, center, 12, color, lineType=8, thickness=-1)

def draw_square(img, center, color):
    half_size = 6
    top_left = (center[0] - half_size, center[1] - half_size)
    bottom_right = (center[0] + half_size, center[1] + half_size)
    cv2.rectangle(img, top_left, bottom_right, color, thickness=-1)

def create_start_point_from_direction(direction_vector, frame_size=32):
    center_point = (int(frame_size/2), int(frame_size/2))
    start_point = (center_point[0] + -10 * direction_vector[0],
                    center_point[1] + -10 * direction_vector[1])
    return start_point

def apply_moving_object(frames, moving_object):
    direction_vector = moving_object.direction_vector
    color = moving_object.color_rgb
    shape = moving_object.shape

    start_vector = create_start_point_from_direction(direction_vector)
    for i in range(len(frames)):
        frame = frames[i]
        current_position = (start_vector[0] + direction_vector[0] * i * 2,
                            start_vector[1] + direction_vector[1] * i * 2)
        print(current_position, color)
        if shape == "circle":
            draw_circle(frame, current_position, color)
        else:
            draw_square(frame, current_position, color)


def create_blank_frame(size=32):
    blank_frame=np.zeros((size,size,3))
    return blank_frame

def create_frame_stack(nb_frames, size=32):
    frame_stack = [create_blank_frame(size) for _ in range(nb_frames)]
    return frame_stack

def display_frame_stack(frames, cols=5):

    fig, ax = plt.subplots(2, cols)

    for i in range(len(frames)):
        frame = frames[i]
        r = math.floor(i/cols)
        c = i%cols
        ax[r,c].imshow(frame)

    plt.show()

moving_object = captions.moving_shape("blue","circle","left")
frames = create_frame_stack(10)
apply_moving_object(frames, moving_object)
display_frame_stack(frames)