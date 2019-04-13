# Basic imports
import socket
import select
import sys
import time
import threading 
import os

Stations = []
Remove = []

class Station():
    sname = "" # represents the station, "hacker", "communication", "control", "clock", "projector" or "main"
    ip = 0
    port = 0
    conn = ""

    def __init__(self, _ip, _port, _sname, _conn):
		self.ip = _ip
		self.port = _port
		self.sname = _sname
		self.conn = _conn        

# Unix command to clear screen, will not work with Windows
def clear_screen():
	os.system("clear")

def receive_name(sock):
	data = ""

	# Espera com um timeout de 1 minuto
	ready = select.select([sock], [], [], 60)
	if ready[0]:
		data = sock.recv(256)
		if data == "":
			# Conexao finalizada pelo usuario
			return data
		
	ip_client = sock.getpeername()[0]	
	port_client = sock.getpeername()[1]	
		
	if data == "":
		print("Cadastro nao finalizado! Finalizando conexao com " + str(ip_client) + "/" + str(port_client))
	else:
		print("Estacao " + data + " cadastrado com sucesso. (" + str(ip_client) + "/" + str(port_client) + ")")
		
	return data

def send_error(sock):
	sock.send("NOk")
	sock.close()
	
def send_ok(sock):
	sock.send("Ok")	

def list_remove():
	cont = 0
	for i in range(len(Remove)):
		del Stations[Remove[i]-cont]
		cont = cont + 1
	del Remove[:]

# Envia a todos os clientes conectados a mesma mensagem
def Broadcast(msg):
	for i in range(len(Stations)):
		try:
			Stations[i].conn.send(msg)
		except IOError:
			# To avoid broken pipe from stoping the broadcast
			Remove.append(i) # Flag the disconnected station for removal
		except socket.error:
			Remove.append(i) # Flag the disconnected station for removal
	list_remove()

# Sends a msg to a specific connected user
def send_specific(msg, usr):
	for i in range(len(Stations)):
		if usr in Stations[i].sname:
			try:
				Stations[i].conn.send(msg)
			except IOError:
				# To avoid broken pipe from stoping the broadcast
				Remove.append(i) # Flag the disconnected station for removal
			except socket.error:
				Remove.append(i) # Flag the disconnected station for removal
	
	list_remove()				

# Realiza a conexao e leitura dos diferentes clientes
def conecta(sock):
    # Conecta com um cliente

    # Checa se recebeu um nome
	# Nomes possiveis:
	#	'1' - Hacker			- Proprio rasp, que ja eh o servidor, entao nao precisamos nos preocupar com esse caso
	#	'2' - Communication		- PC responsavel por mostrar videos e pedir dicas
	#	'3' - Control			- PC de controle, conversa com o servidor informando o fim da sala
	#	'4' - Clock				- PC responsavel pelo video do cronometro
	#	'5' - Projector			- Por enquanto esta ideia nao esta sendo utilizada
	#	'6' - Main				- PC principal de controle, que inicia a sala e envia dicas

	sname = ""
	sname = receive_name(sock)

	# Response for communication start
	if sname == "":
        # Fail in receiving name
		send_error(sock)
	else:
		send_ok(sock)

    # Insere essa estacao na lista de estacoes conectadas
	Stations.append(Station(sock.getpeername()[0], sock.getpeername()[1], sname, sock))

	while True:
        # Escuta a conexao infinitamente
		ready = select.select([sock], [], [])	# Modulo que verifica se algo foi escrito pelo cliente
		if ready[0]:	
			# Se algo foi escrito

			data = sock.recv(256)	# Le a entrada, limitada em pacotes de 256 bytes

			if data == "":
				print("Conexao finalizada repentinamente pelo usuario!")
				break

			elif data == "start":	# Unica estacao que envia "start" eh a '6'
				Broadcast(data)	# Manda para todas as outras estacoes comecarem suas atividades

			elif data[0] == 'e':	# Final da sala
				send_specific("stop", '3')	# Para a atualizacao da tela de controle
				send_specific("stop", '4')	# Para o cronometro
				send_specific('e'+data[1], '2')	# Envia o sinal para chavear o video do foguete

			elif data[0] == 'd':	# Pedido de dicas
				send_ok(sock)		# Responde ao PC que pediu dicas com um simples OK "Sua dica esta vindo"
				send_specific("Need Help!", '6')	# Envia ao PC main o pedido de dicas

			else:
				Broadcast(data)	# So quem pode enviar mensagens aleatorias eh o '6', entao faz um broadcast para todos

# Terminal execution
if __name__ == "__main__":
	# 
	#	Start of Server setup
	#

    SERVER_IP = "0.0.0.0"	# Start IP as Unknown
    RECV_BUFFER = 256	# Buffer size for input

    if len(sys.argv) == 2:
        # Permite utilizar parametros para rodar o programa
        if sys.argv[1] == "--random_port":	
            # Utilizar uma porta aleatoria
            port = 0
        else:
            # Por padrao usa a porta 42188	
            port = 42188
    else:		
        port = 42188

    # Inicializa a porta para receber conexoes TCP
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # Prepara a porta
    server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR,1)

    # Conecta com a porta	
    server_socket.bind((SERVER_IP,port))	

	#
	#	End of Server
	#

    # Comeca a escutar
    server_socket.listen(10)

    IP = socket.gethostbyname(socket.gethostname())
    PORT = server_socket.getsockname()[1]	# Get the port the OS used

    clear_screen()
    print(IP)

    if port == 0:
        print("Conecte-se utilizando a porta " + str(PORT))

	#	The following is the part of the code that deals with the conections
	#	A thread is started for every connecting device

    while True:
    # Verifica se alguem tentou conectar
        try:
            # Aceita nova conexao
            sck, full_address = server_socket.accept()

            #print(sck, full_address)

            # Inicia uma thread para essa conexao
            thread_station = threading.Thread(target=conecta, args=[sck])
            thread_station.start()
        except (KeyboardInterrupt):
            sys.exit(0)