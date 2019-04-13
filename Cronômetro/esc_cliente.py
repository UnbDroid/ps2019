# Basic imports
import socket
import select
import string
import sys
import time
import os
import threading
import cv2
#import pygame
#import 

# Variavel de porta do arduino
arduino_port = '/../../dev/ttyACM0'

# Global variables
final_result = ""   # Result of end-game button
start = False       # Start of the room
stop = False        # Stop of the room
response = False    # Response for help
close = False       # Close connection
data = ""           # Data transmisted between sockets
last_ang = 0
last_vel = "000"

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
    import texts
    number = str(number)

    for i in range(1, 8):
        for digit in number:
            if digit not in "0123456789":
                digit = '0'
            func_name = 'print_'+str(digit)+'_'+str(i)
            func = getattr(texts, func_name)
            result = func()
        print("")

def update_screen_info(ang, vel):
    import texts

    global last_ang
    global last_vel

    if ang != last_ang or vel != last_vel:
        clear_screen()
        texts.print_ship()
        texts.print_vel()
        # print_1_1()
        number_print(vel)
        print("")
        print("")
        print("")

        texts.print_angle()
        number_print(ang)

        last_vel = vel
        last_ang = ang

def arduino_read(Station_name, show_tip, stop_siren):
    try:
        import serial
    except:
        # Probably already imported
        pass

    global final_result
    global response
    global arduino_port

    try:
        arduinoSerial = serial.Serial(arduino_port, 9600)
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
                        return
                    if switch == '0' and not stop_siren.isSet():
                        stop_siren.set()
                    if response == True:
                        show_tip.set()
                        response = False

                else:
                    pass

        elif time.time() - last_time > 1:   # 1 second timeout
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
                        if data != "Ok":
                            response = True

                    if '6' in Station_name:            
                        print "\n\033[31m" + data	+ "\033[0m\033[K"	
        except (KeyboardInterrupt):
            break
        except socket.error:
            print "Erro na conexao! Finalizando programa"
            sys.exit()
            break	
        except IOError:
            break	

def play_time(end_room, start_timer):
    cap = cv2.VideoCapture('chronos.mp4') # Path to the video of the chronometer

    cv2.namedWindow('Tempo', cv2.WINDOW_NORMAL)

    # Get 3 frames to position the window
    ret, frame = cap.read()
    ret, frame = cap.read()
    ret, frame = cap.read()

    if ret == True:
        while not start_timer.isSet():
            cv2.imshow('Tempo', frame)
            cv2.waitKey(100)

    while cap.isOpened():
        ret, frame = cap.read()

        if end_room.isSet():
            while True:
                # Hold video position
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

def play_rocket(start_room, end_room, show_tip, stop_siren, start_timer):
    import pygame
    import numpy as np

    global data
    siren = True
    
    cv2.namedWindow('Comunicacao', cv2.WINDOW_NORMAL)

    cap = cv2.VideoCapture('Imersao_final.mp4') # Path to the first video

    ret, frame = cap.read()

    if ret == True:
        while not start_room.isSet():
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

    start_timer.set()

    cap = cv2.VideoCapture('Aguarda_lancamento.mp4') # Path to the third video

    # Begin of third video
    # Start big siren audio
    pygame.mixer.music.load('sirene.wav')
    pygame.mixer.music.play()

    while cap.isOpened():
        ret, frame = cap.read()

        if ret == True:
            cv2.imshow('Comunicacao', frame)

            # Restart the sound if it stops
            if not pygame.mixer.music.get_busy():
                pygame.mixer.music.rewind()
                pygame.mixer.music.play()

            # Checks for ending flag
            if end_room.isSet():
                break

            # Checks the help flag
            if show_tip.isSet():
                # Make a black screen the size of the screen we are using
                frame = np.zeros((frame.shape[0], frame.shape[1], frame.shape[2]), np.uint8)

                # Draw a label in the message
                __draw_label(frame, data, (frame.shape[1]/2,frame.shape[0]/2), (255,0,0))

                cv2.imshow('Comunicacao', frame)
                cv2.waitKey(8000)
                show_tip.clear()

            if stop_siren.isSet() and siren == True:
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
    start_room = threading.Event()  # Flag para iniciar
    end_room = threading.Event()    # Flag para finalizar e chavear videos
    show_tip = threading.Event()    # Flag para mostrar dica na tela
    stop_siren = threading.Event()  # Flag para chavear audio
    start_timer = threading.Event() # Flag para comecar video do cronometro

    # Estacao de cronometro comeca o video para posicionamento na tela e espera pelo evento de iniciar
    if '4' in Station_name:
        # Start the thread with the cronometer video
        thread_chronos = threading.Thread(target=play_time, args=[end_room, start_timer])
        thread_chronos.start()

    #Estacao de comunicacao comeca a sequencia de videos para posicionamento na tela e espera pelo evento de iniciar
    if '2' in Station_name:
        # Start the screen with the start and rocket videos
        thread_rocket = threading.Thread(target=play_rocket, args=[start_room, end_room, show_tip, stop_siren, start_timer])
        thread_rocket.start()

    # If it's not the main control computer, only start when the signal to start is sent
    if '6' not in Station_name:
        answered = 0
        while answered == 0 or start == False:
            #print(str(answered) + str(start))
            pass

        # Awaken both videos, chronometer and rocket
        start_room.set()

    # Starts a thread in the control pc and wont leave until it sends the end signal, result is saved "final_result"
    if '3' in Station_name:
        thread_serial_arduino = threading.Thread(target=arduino_read, args=[Station_name, show_tip, stop_siren])
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
                end_room.set() # Evento para pausar o video
                while True:
                    pass

        # Estacao de controle verificacao de continuacao
        if '3' in Station_name:
            # Freeze screen with current data
            if stop == True:
                end.room.set() # Evento para pausar a tela
                while True:
                    pass

        # Estacao de comunicacao verificacao de continuacao
        if '2' in Station_name:
            # Reads arduino serial until a change in the switches is detected or they ask for help
            thread_com = threading.Thread(target=arduino_read, args=[Station_name, show_tip, stop_siren])
            thread_com.run()

        # Envia a requisicao ao servidor
        try:
            if '2' in Station_name:
                # Se a thread acabou, significa pedido de dicas, envia uma mensagem pedindo
                    station_socket.send("d1")

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