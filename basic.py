import numpy as np
import matplotlib.pyplot as plt
import cv2
import math

def create_blank_frame(size=32):
    blank_frame=np.zeros((size,size,3))
    return blank_frame

def draw_circle(img):
    cv2.circle(img, (16,16), 12, (255,0,0), lineType=8, thickness=-1) #thickness=1, 
    return img

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

def move_circle_up(frames):
    starting_position = (16,32)
    movement_vector = (0,-3)

    for i in range(len(frames)):
        pos_vector = (starting_position[0] + i * movement_vector[0], starting_position[1] + i * movement_vector[1])
        print(pos_vector)
        frames[i] = cv2.circle(frames[i], pos_vector, 12, (255,0,0), lineType=8, thickness=-1)

    return frames

frames = create_frame_stack(10)
frames = move_circle_up(frames)
print(len(frames))
display_frame_stack(frames)