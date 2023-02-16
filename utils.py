import cv2
import numpy as np

def write_frames_to_video(frames, fps = 2):

    video_fn = "test.mp4"
    print(len(frames))

    out = cv2.VideoWriter(video_fn,
                            cv2.VideoWriter_fourcc(*'mp4v'), 
                            fps, 
                            (32,32))
    for i in range(len(frames)):
        # writing to a image array
        # its actually BGR
        # so "red" -> blue here
        out.write(np.array(frames[i]).astype('uint8'))
    out.release()

def prepare_row_for_csv(moving_object):
    pass
