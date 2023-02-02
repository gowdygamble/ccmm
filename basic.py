import numpy as np
import matplotlib.pyplot as plt

def create_blank_frame(size=32):
    blank_frame=np.zeros((size,size,3))
    return blank_frame


z = create_blank_frame()

plt.figure()
plt.imshow(z)
plt.show()