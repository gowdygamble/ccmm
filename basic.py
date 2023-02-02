import numpy as np
import matplotlib.pyplot as plt
import cv2

def create_blank_frame(size=32):
    blank_frame=np.zeros((size,size,3))
    return blank_frame

def draw_circle(img):
    cv2.circle(img, (16,16), 12, (255,0,0), lineType=8, shift=0, thickness=-1) #thickness=1, 
    return img

z = create_blank_frame()
z = draw_circle(z)

plt.figure()
plt.imshow(z)
plt.show()