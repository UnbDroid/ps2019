import socket
import select
import threading
import os
import sys
import time

def clear_screen():
    os.system("clear")

start = False       # Start of the room
stop = False        # Stop of the room
need_help = False   # Asking for help
response = False    # Response for help
close = False       # Close connection
data = ""           # Data transmisted between sockets

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
                    print("GOT AN ANSWER")
                    if answered is 0:
                        print("answered")
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

    # If it's not the main control computer, only start when the signal to start is sent
    if '6' not in Station_name:
        answered = 0
        while answered == 0 or start == False:
            #print(str(answered) + str(start))
            pass

    while True:
        # Estado idle infinito

        # Marca que nao foi respondido e nao esta esperando
        answered = -1

        # Envia a requisicao ao servidor
        try: 

            msg = ""
            while not msg:
                msg = raw_input("$: ")
            station_socket.send("%s" % msg)

            # Waiting for answer
            answered = 0

            # Waits for the server to answer something!
            while answered is 0:
                print("Waiting for answer")
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