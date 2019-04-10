import cv2
import numpy as np
import threading
import time

cap = cv2.VideoCapture('chronos.mp4') # Path to the third video
r = threading.Event()

data = "Now even a large test with more shit written in before Big Test"

def wait_and_set():
    global r
    x = 0
    while x < 5:
        time.sleep(10)
        r.set()
        x = x+1

def __draw_label(img, text, pos, bg_color):
    font_face = cv2.FONT_HERSHEY_SIMPLEX
    scale = 1
    color = (255, 255, 255)
    thickness = cv2.FILLED
    margin = 2

    txt_size = cv2.getTextSize(text, font_face, scale, thickness)

    pos = (pos[0] - txt_size[0][0]/2 - margin/2, pos[1] + txt_size[0][1]/2 + margin/2)

    end_x = pos[0] + txt_size[0][0] + margin
    end_y = pos[1] - txt_size[0][1] - margin

    cv2.rectangle(img, pos, (end_x, end_y), bg_color, thickness)
    cv2.putText(img, text, pos, font_face, scale, color, 1, cv2.LINE_AA)

thread = threading.Thread(target=wait_and_set)
thread.start()

try:
    cv2.namedWindow('Comunicacao', cv2.WINDOW_NORMAL)

    while cap.isOpened():
        ret, frame = cap.read()

        print((frame.shape[0], frame.shape[1], frame.shape[2]))

        if ret == True:
            cv2.imshow('Comunicacao', frame)

            # Checks the help flag
            if r.isSet():
                # Make a black screen the size of the screen we are using
                frame = np.zeros((frame.shape[0], frame.shape[1], frame.shape[2]), np.uint8)

                # Draw a label in the message
                __draw_label(frame, data, (frame.shape[1]/2,frame.shape[0]/2), (0,0,255))

                cv2.imshow('Comunicacao', frame)
                cv2.waitKey(7000)
                r.clear()     

            cv2.waitKey(40)
        else:
            break
except KeyboardInterrupt:
    cap.release()