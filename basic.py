import numpy as np
import matplotlib.pyplot as plt
import cv2

def create_blank_frame(size=32):
    blank_frame=np.zeros((size,size,3))
    return blank_frame

def draw_circle(img):
    cv2.circle(img, (16,16), 12, (255,0,0), lineType=8, thickness=-1) #thickness=1, 
    return img

def create_frame_stack(nb_frames, size=32):
    frame_stack = [create_blank_frame(size) for _ in range(nb_frames)]
    return frame_stack

frames = create_frame_stack(10)
print(len(frames))