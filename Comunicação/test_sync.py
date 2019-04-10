import cv2
import numpy as np
import pygame
import time

try:
    cv2.namedWindow('Comunicacao', cv2.WINDOW_NORMAL)

    cap = cv2.VideoCapture('Imersao_final.mp4') # Path to the first video

    ret, frame = cap.read()

    # Begin of first video

    # Start audio
    pygame.init()
    pygame.mixer.init()
    
    pygame.mixer.music.load('Imersao_final.wav')
    pygame.mixer.music.play()

    while cap.isOpened():
        ret, frame = cap.read()

        if ret == True:
            cv2.imshow('Comunicacao', frame)

            cv2.waitKey(39)
        else:
            break

    # End of first video

    cap = cv2.VideoCapture('Thiago.mp4') # Path to the second video
    
    # Begin of second video
    # Start audio
    pygame.mixer.music.load('Thiago_voz.wav')
    pygame.mixer.music.play()

    while cap.isOpened():
        ret, frame = cap.read()

        if ret == True:
            cv2.imshow('Comunicacao', frame)

            cv2.waitKey(35)
        else:
            break
except KeyboardInterrupt:
    cap.release()