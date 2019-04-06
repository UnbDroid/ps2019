# Basic imports
import socket
import select
import string
import sys
import time
import os
import threading

# Variavel global de leitura
data = ""

# Global variables
close = False

file_name = ""

def clear_screen():
    os.system("clear")

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
"""
def file_send():
	# Save file_name
	global file_name
	local_file_name = file_name # In case the user tries to send another file
	
	my_file = open(local_file_name, 'r')
	
	msg = "-file"
	while msg != "":
		msg = my_file.read(1019)
		if msg != "":
			msg = "-file" + msg
			client_socket.send(msg)
			time.sleep(1)
			
	client_socket.send("--file")		
	my_file.close()		
"""
def get_answer():
	global data
	global close
	global answered
	
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
						
					else:			
						print "\n\033[31m" + data	+ "\033[0m\033[K"	
		except (KeyboardInterrupt):
			break
		except socket.error:
			print "Erro na conexao! Finalizando programa"
			sys.exit()
			break	
		except IOError:
			break	

# Checa se e o modulo principal chamado
if __name__ == "__main__":

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

    # Tentativa de se conectar ao servidor
    try:
        station_socket.connect((host, port))	# Try connection
    except:
        print "Nao foi possivel se conectar ao servidor, tente novamente mais tarde."
        sys.exit(0)

    clear_screen()
    print "Conectado ao servidor."
    time.sleep(1)

    Station_name = ""
    while not Station_name:
        Station_name = raw_input("Informe o nome dessa estacao:\nHacker\nCommunication\nControl\nClock\n\t")

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
            print "Nao foi possivel se conectar ao servidor!"
            sys.exit()	

    # Conexao sucedida

    # Comeca uma thread pra ficar lendo
    thread_read = threading.Thread(target=get_answer)
    thread_read.start()

    global answered

    while True:
        # Estado idle infinito

        # Marca que nao foi respondido e nao esta esperando
        answered = -1

        msg = ""

        # Envia a requisicao ao servidor
        try:
            # Recebe do arduino as informacoes a se passar ao servidor MODIFICAR
            while not msg:
                msg = raw_input("$: ")

                # if msg[0:2] == "-f":
                # 	my_list = msg.split(' ')
                # 	file_name = my_list[1]

                # Envia a mensagem
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
            print "Conexao perdida!"
            sys.exit()