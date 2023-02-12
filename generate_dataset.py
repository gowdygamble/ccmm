import captions 
from basic import *

import cv2

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
    cv2.circle(img, center, 12, color, lineType=8, thickness=-1) #thickness=1, 
    return img

def create_start_point_from_direction(direction_vector, frame_size=32):
    center_point = (int(frame_size/2), int(frame_size/2))
    start_point = center_point + -10 * direction_vector # cant add sets like vectors!
    return start_point

def apply_moving_object(frames, moving_object):
    direction_vector = moving_object.direction_vector
    color = moving_object.color_rgb
    shape = moving_object.shape

    start_vector = create_start_point_from_direction(direction_vector)
    for i in range(len(frames)):
        frame = frames[i]
        current_position = start_vector + direction_vector * i * 2
        draw_circle(frame, current_position, color)


moving_object = captions.moving_shape("green","square","down")
frames = create_frame_stack(10)
apply_moving_object(frames, moving_object)