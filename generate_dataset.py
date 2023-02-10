import captions 
import cv2

z = len(captions.shapes) * len(captions.directions) * len(captions.colors)

print("Total combinations:", z)

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

def apply_moving_object(frames, moving_object):
    direction_vector = moving_object.direction_vector
    color = moving_object.color_rgb
    shape = moving_object.shape

    for i in range(len(frames)):

        



for s in range(len(captions.shapes)):
    for c in range(len(captions.colors)):
        for d in range(len(captions.directions)):
            moving_object = captions.moving_shape_string(c,s,d)
            #print(moving_object.caption_string)
