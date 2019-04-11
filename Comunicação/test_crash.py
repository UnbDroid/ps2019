import cv2
import numpy as np
import pygame
import threading
import time

data = ""

def change_data():
    global data
    time.sleep(10)
    data = "e0"


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

        cv2.waitKey(2)
    else:
        break

# End of first video

cap.release()
cap = cv2.VideoCapture('Thiago.mp4') # Path to the second video

# Begin of second video
# Start audio
pygame.mixer.music.load('Thiago_voz.wav')
pygame.mixer.music.play()

while cap.isOpened():
    ret, frame = cap.read()

    if ret == True:
        cv2.imshow('Comunicacao', frame)

        cv2.waitKey(2)
    else:
        break

# End of second video

cap.release()
cap = cv2.VideoCapture('Aguarda_lancamento.mp4') # Path to the third video

# Begin of third video
# Start big siren audio
pygame.mixer.music.load('sirene.wav')
pygame.mixer.music.play()

thread_wait = threading.Thread(target=change_data)
thread_wait.start()

while cap.isOpened():
    ret, frame = cap.read()

    if not pygame.mixer.music.get_busy():
        pygame.mixer.music.rewind()
        pygame.mixer.music.play()

    if data != "":
        break

    if ret == True:
        cv2.imshow('Comunicacao', frame)

        cv2.waitKey(2)
    else:
        break

# End of third video

cap.release()
# Now we make a decision based on the 'data' captured
if data[1] == '1':
    # They won
    cap = cv2.VideoCapture('Good_end.mp4') # Path to the good ending video
    pygame.mixer.music.load('Good_end.wav')
    pygame.mixer.music.play()        
else:
    cap = cv2.VideoCapture('Bad_end.mp4') # Path to the bad ending video
    pygame.mixer.music.load('Bad_end.wav')
    pygame.mixer.music.play()
while cap.isOpened():
    ret, frame = cap.read()

    if ret == True:
        cv2.imshow('Comunicacao', frame)

        cv2.waitKey(40)
    else:
        break

cap.release()