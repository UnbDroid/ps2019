# Basic imports
import socket
import select
import string
import sys
import time
import os
import threading
import serial 
import cv2
import numpy as np
import pygame
import texts

# Variavel global de leitura
data = ""

final_result = ""

last_switch = '1'

start = False
stop = False
need_help = False
response = False

# Global variables
close = False

file_name = ""

def clear_screen():
    os.system("clear")

# Responsavel por firmalizar a conexao com o servidor
def get_conn():
	global data

	data = ""

	# Utiliza o modulo select para verificar se alguma informacao esta disponivel
	ready = select.select([station_socket], [], [], 5)
	if ready[0]:
		data = station_socket.recv(256)
		if data == "":
			# Server esta fechado, fechar conexao necessariamente
			print "Conexao fechada pelo servidor!"
			global close
			close = True
			return False

	if data == "":
		print "Timeout!"
		return False
	else:
		if data == "Ok":
			print "Conectado com sucesso!"
			return True
		else:
			print "Erro na conexao!"
			return False	

def number_print(number):
    number = str(number)

    for i in range(1, 8):
        for digit in number:
            func_name = 'print_{digit}_{i}'
            func = getattr(texts, func_name)
            result = func()
        print("")

def update_screen_info(ang, vel):
    clear_screen()

    texts.print_ship()
    texts.print_vel()
    # print_1_1()
    number_print(speed)
    print("")
    print("")
    print("")

    texts.print_angle()
    number_print(angle)

def arduino_read(Station_name):
    global final_result
    global last_switch
    global need_help
    global response

    try:
        arduinoSerial = serial.Serial('/../../dev/ttyUSB0', 9600)
    except serial.SerialException:
        # Probably already configured
        pass

    arduinoSerial.write('o')
    last_time = time.time()
    while(1):
        if arduinoSerial.inWaiting() > 0:
            read_char = arduinoSerial.read()
            if '3' in Station_name:
                if read_char == 'p' : # Valor do potenciometro
                    read_char = arduinoSerial.read()
                    ang = int(read_char.encode('hex'), 16)
                    
                    read_char = arduinoSerial.read()
                    if read_char != 't':
                        #print("Communication error! Expecting p identifier")
                        arduinoSerial.flush()
                        arduinoSerial.write('o')
                        pass

                    vel = ""
                    read_char = arduinoSerial.read()
                    vel = vel + read_char
                    read_char = arduinoSerial.read()
                    vel = vel + read_char
                    read_char = arduinoSerial.read()
                    vel = vel + read_char
                    update_screen_info(ang, vel)

                elif read_char == 'e':
                    read_char = arduinoSerial.read()
                    final_result = read_char
                    break

                else:
                    pass
                    #print("Communication error! Expecting other")
            elif '2' in Station_name:
                if read_char == 'd' : # Valor da dica
                    read_char = arduinoSerial.read()
                    tip = read_char

                    read_char = arduinoSerial.read()
                    if read_char != 's':
                        #print("Communication error! Expecting p identifier")
                        arduinoSerial.flush()
                        arduinoSerial.write('o')
                        pass

                    read_char = arduinoSerial.read()
                    switch = read_char

                    if tip == '1':
                        need_help = True     
                        break
                    if switch != last_switch and last_switch == '1':
                        last_switch = switch
                        break
                    if response == True:
                        break

                    last_switch = switch    

        elif time.time() - last_time > 5:
            #print("Not receiving anything!")
            arduinoSerial.write('o')   

def get_answer(Station_name):
    global data
    global close
    global answered
    global start
    global response

    data = ""

    while True:
        try:
            ready = select.select([station_socket], [], [], 1)
            if ready[0]:
                data = station_socket.recv(256)
                if data == "":
                    # Server esta fechado, fechar conexao necessariamente
                    print "Conexao fechada pelo servidor!"
                    close = True
                    break
                else:
                    if answered is 0:
                        answered = 1

                    if data == "exit":
                        close = True
                        print "Conexao finalizada!"
                        sys.exit()
                        break			

                    elif data == "start":
                        start = True

                    elif data == "stop":
                        stop = True

                    else:
                        # Assumes this is the response of the ask for help
                        response = True

                    #elif '6' not in Station_name:            
                    #    print "\n\033[31m" + data	+ "\033[0m\033[K"	
        except (KeyboardInterrupt):
            break
        except socket.error:
            print "Erro na conexao! Finalizando programa"
            sys.exit()
            break	
        except IOError:
            break	

def play_time(e, s):
    cap = cv2.VideoCapture('chronos.mp4') # Path to the video of the chronometer

    cv2.namedWindow('Tempo', cv2.WINDOW_NORMAL)

    ret, frame = cap.read()

    if ret == True:
        while not e.isSet():
            cv2.imshow('Tempo', frame)
            cv2.waitKey(100)

    while cap.isOpened():
        ret, frame = cap.read()

        if s.isSet():
            while True:
                print("Maintaining video")
                pass

        if ret == True:
            cv2.imshow('Tempo', frame)
            cv2.waitKey(100)
        else:
            break

    cap.release()        

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

def play_rocket(e, s, r, a):
    global data
    siren = True
    
    cv2.namedWindow('Comunicacao', cv2.WINDOW_NORMAL)

    cap = cv2.VideoCapture('Imersao_final.mp4') # Path to the first video

    ret, frame = cap.read()

    if ret == True:
        while not e.isSet():
            cv2.imshow('Comunicacao', frame)
            cv2.waitKey(35)

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

            cv2.waitKey(35)
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

    # End of second video

    cap = cv2.VideoCapture('Aguarda_lancamento.mp4') # Path to the third video

    # Begin of third video
    # Start big siren audio
    pygame.mixer.music.load('sirene.wav')
    pygame.mixer.music.play()

    while cap.isOpened():
        ret, frame = cap.read()

        if ret == True:
            cv2.imshow('Comunicacao', frame)

            # Checks for ending flag
            if s.isSet():
                break

            # Checks the help flag
            if r.isSet():
                # Make a black screen the size of the screen we are using
                frame = np.zeros((frame.shape[0], frame.shape[1], frame.shape[2]), np.uint8)

                # Draw a label in the message
                __draw_label(frame, data, (20,20), (255,0,0))

                cv2.imshow('Comunicacao', frame)
                cv2.waitKey(8000)
                r.clear()

            if a.isSet() and siren == True:
                # Change to other audio
                pygame.mixer.music.load('Aguarda_lancamento.wav')
                pygame.mixer.music.play()
                siren = False        

            cv2.waitKey(40)
        else:
            break

    # End of third video

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

# Checa se e o modulo principal chamado
if __name__ == "__main__":
    #
    #   Begin of Client Setup
    #

    if len(sys.argv) == 3:
        # Usuario informou o IP e a porta
        host = sys.argv[1]
        port = int(sys.argv[2])
    elif len(sys.argv) == 2:
        # Usuario informou apenas o IP
        host = sys.argv[1]
        port = 42188 # Escolhida aleatoriamente
    else:		
        print "Erro! Correta utilizacao do programa: \"python2.7 chat_client.py endereco_ip_servidor [porta_servidor]\" "
        sys.exit(0)

    clear_screen()

    # Configura o socket orientado a conexoes TCP
    station_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    #
    #   End of Client Setup
    #

    # Tentativa de se conectar ao servidor
    try:
        station_socket.connect((host, port))	# Try connection
    except:
        print "Nao foi possivel se conectar ao servidor, tente novamente mais tarde."
        sys.exit(0)

    clear_screen()
    print "Conectado ao servidor."
    time.sleep(1)

    # Leitura do nome (funcao) do PC que esta se conectando

    possibles = ['1', '2', '3', '4', '5', '6']
    Station_name = ""
    while not any(possible in Station_name for possible in possibles):
        Station_name = raw_input("Informe o nome dessa estacao:\n1-Hacker\n2-Communication\n3-Control\n4-Clock\n5-Projector\n6-Main\n\t")

    success = False

    # Tentativa repetitiva de cadastro
    while success is False:
        try:
            station_socket.send("%s" % Station_name)	# Envia o nome para cadastro
            success = get_conn()

            if close == True:
                break

            if success is False:
                again = "v"
                while again != "s" and again != "n": 
                    again = raw_input("Tentar novamente? (s/n): ")

                if again.lower() == "n":
                    sys.exit()
        except (KeyboardInterrupt):
            client_socket.close()
            break
        except socket.error:
            #print "Nao foi possivel se conectar ao servidor!"
            sys.exit()	

    # Conexao sucedida

    # Comeca uma thread pra ficar lendo dados do servidor
    thread_read = threading.Thread(target=get_answer, args=[Station_name])
    thread_read.start()

    # Eventos que controlam threads
    e = threading.Event() # Flag para iniciar
    s = threading.Event() # Flag para finalizar e chavear videos
    r = threading.Event() # Flag para mostrar dica na tela
    a = threading.Event() # Flag para chavear audio

    # Estacao de cronometro comeca o video para posicionamento na tela e espera pelo evento de iniciar
    if '4' in Station_name:
        # Start the thread with the cronometer video
        thread_chronos = threading.Thread(target=play_time, args=[e, s])
        thread_chronos.start()

    # Estacao de comunicacao comeca a sequencia de videos para posicionamento na tela e espera pelo evento de iniciar
    if '2' in Station_name:
        # Start the screen with the start and rocket videos
        thread_rocket = threading.Thread(target=play_rocket, args=[e, s, r, a])
        thread_rocket.start()   

    # If it's not the main control computer, only start when the signal to start is sent
    if '6' not in Station_name:
        answered = 0
        while answered == 0 or start == False:
            #print(str(answered) + str(start))
            pass

        # Awaken both videos, chronometer and rocket
        e.set()

    # Starts a thread in the control pc and wont leave until it sends the end signal, result is saved "final_result"
    if '3' in Station_name:
        thread_serial_arduino = threading.Thread(target=arduino_read, args=[Station_name])
        thread_serial_arduino.start()
        thread_serial_arduino.join()
        #print(final_result)

    while True:
        # Estado idle infinito

        # Marca que nao foi respondido e nao esta esperando
        answered = -1

        # Estacao de cronometro verificacao de continuacao
        if '4' in Station_name:
            # Stop chronometer
            if stop == True:
                s.set() # Evento para pausar o video
                while True:
                    pass

        # Estacao de controle verificacao de continuacao
        if '3' in Station_name:
            # Freeze screen with current data
            if stop == True:
                s.set() # Evento para pausar a tela
                while True:
                    pass

        # Estacao de comunicacao verificacao de continuacao
        if '2' in Station_name:
            # Reads arduino serial until a change in the switches ir detected or they ask for help
            thread_serial_arduino = threading.Thread(target=arduino_read, args=[Station_name])
            thread_serial_arduino.start()
            thread_serial_arduino.join()

        # Envia a requisicao ao servidor
        try:
            if '2' in Station_name:
                # Envia uma mensagem de dicas ou valor dos switches
                
                # Pedido de dicas
                if need_help == True:
                    station_socket.send("d1")
                    need_help = False
                elif response == True:
                    # Do the transition between videos and print the 'data' variable
                    
                    # Sets the flags that start the event that switch videos and show the help message
                    r.set()
                    response = False
                else:
                    # Change audio
                    if last_switch == '0':
                        # Turn normal audio on
                        a.set()

            if '3' in Station_name:
                # Envia a mensagem
                if final_result != "":
                    station_socket.send("e%s" % final_result) 

            if '6' in Station_name:
                msg = ""
                while not msg:
                    msg = raw_input("$: ")
                station_socket.send("%s" % msg)

            # Waiting for answer
            answered = 0

            # Waits for the server to answer something!
            while answered is 0:
                pass

            time.sleep(1)

            if close == True:
                break		
        except (KeyboardInterrupt):		
            station_socket.close()
            break		
        except socket.error:
            #print "Conexao perdida!"
            sys.exit()