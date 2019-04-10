# Basic imports
import socket
import select
import sys
import time
import threading 
import os

Stations = []
# Users = []
# Salas = []
# salas_map = {}

class Station():
    sname = "" # represents the station, "hacker", "communication", "control" or "clock"
    ip = 0
    port = 0
    conn = ""

    def __init__(self, _ip, _port, _sname, _conn):
		self.ip = _ip
		self.port = _port
		self.sname = _sname
		self.conn = _conn        
"""
class User():
	ip = 0
	port = 0
	uname = ""
	sala = -1
	conn = ""
	
	def __init__(self, _ip, _port, _uname, _conn):
		self.ip = _ip
		self.port = _port
		self.uname = _uname
		self.sala = -1
		self.conn = _conn

class Sala():
	tipo = 0
	numero = 0
	senha = ""
	usuarios = []
	
	def __init__(self, _tipo, _numero, _senha=""):
		self.tipo = _tipo
		self.senha = _senha	
		self.numero = _numero
		self.usuarios = []
"""
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

# RETIRAR USUARIOS QUE JA SE DESCONECTARAM
def Broadcast(msg):
    for i in range(len(Stations)):
        Stations[i].conn.send(msg)
"""
def atualiza_dict(idx):
	# Todas as chaves no dicionario que apontam para um index maior do que idx devem ser decrementados por 1 unidade
	for key, value in salas_map.iteritems():
		if value > idx:
			salas_map[key] -= 1		

def file_broadcast(sala, idx):
	i = 0

	global file_info
	global file_name
	global file_reading
	
	# First broadcast to create file
	Broadcast(sala, idx, "-file creat " + file_name)
	time.sleep(1.5)	# Sincronia com o cliente

	while (i + 1000) <= len(file_info):
		msg = "-file" + file_info[i:i+1000]
		Broadcast(sala, idx, msg)
		i += 1000
		time.sleep(1.5)
	
	# Get remaining
	msg = "-file" + file_info[i:]
	Broadcast(sala, idx, msg)
	time.sleep(1.5) # Sincronia
	
	# End
	Broadcast(sala, idx, "-file close")

	file_info = ""
	file_reading = False
	file_name = ""

file_reading = False
file_name = ""
file_info = ""
"""
def send_specific(msg, usr):
    for i in range(len(Stations)):
		if usr in Stations[i].sname:
			Stations[i].conn.send(msg)	

def conecta(sock):
    # Conecta com um cliente

    # Checa se recebeu um nome
	sname = ""
	sname = receive_name(sock)

	global file_reading
	global file_name
	global file_info

	if sname == "":
        # Fail in receiving name
		send_error(sock)
	else:
		send_ok(sock)

    # Insere essa estacao na lista de estacoes conectadas
	Stations.append(Station(sock.getpeername()[0], sock.getpeername()[1], sname, sock))

    # # Guarda o index atual do usuario correspondente a esta thread
    # idx = len(Users) - 1

	while True:
        # Escuta a conexao infinitamente
		ready = select.select([sock], [], [])
		if ready[0]:
			data = sock.recv(256)

			print(data)

			if data == "":
				print("Conexao finalizada repentinamente pelo usuario!")
				break

			elif data == "start":
				Broadcast(data)

			elif data[0] == 'e':
				send_specific("stop", '3')
				send_specific("stop", '4')
				send_specific('e'+data[1], '2')

			elif data[0] == 'd':
				send_ok(sock)
				send_specific("d1", '6')

			else:
				Broadcast(data)

		# 		# Lista as salas	
		# 		if data[0:2] == "-l":
		# 			msg = "Salas disponives (" + str(len(Salas)) + "):\n"
		# 			for i in range(len(Salas)):
		# 				msg += "Sala " + str(Salas[i].numero) + ": "
		# 				if Salas[i].tipo == 0:
		# 					msg += "Publica, "
		# 				else:
		# 					msg += "Privada, "	
						
					
		# 				msg += str(len(Salas[i].usuarios)) + " conectados\n"
		# 			logging.info("Usuario " + uname + " requisitou uma lista de todas as salas. Endereco: " + str(Users[idx].ip) + "/" + str(Users[idx].port))
		# 			sock.send(msg)
					
		# 		# Entra em uma sala		
		# 		elif data[0:2] == "-e":
		# 			if Users[idx].sala != -1:
		# 				msg = "Voce deve primeiro sair da sua sala!"
		# 			else:	
		# 				if len(data) < 4:
		# 					# Nao tem chars suficientes
		# 					msg = "Nao foi possivel identificar a sala desejada!"
		# 				else:
		# 					my_list = data.split(' ')
				
		# 					# Checa se eh numero
		# 					if my_list[1].isdigit():
		# 						# Se realmente existe
		# 						if int(my_list[1]) in salas_map:
								
		# 							# Pega o index atraves do dicionario	
		# 							sala_idx = salas_map[int(my_list[1])]
		# 							# Checa se a sala eh privada:
		# 							if Salas[sala_idx].tipo == 1:
		# 								if len(my_list) < 3:
		# 									msg = "Senha incorreta!"
		# 									logging.info("Usuario " + uname + " tentou entrar na sala " + my_list[1] + ". Endereco: " + str(Users[idx].ip) + "/" + str(Users[idx].port))
		# 								else:
		# 									# Checa se a senha esta correta
		# 									if my_list[2] == Salas[sala_idx].senha:
		# 										Users[idx].sala = int(my_list[1])
		# 										Salas[sala_idx].usuarios.append(idx)
		# 										msg = "Movido para a sala " + my_list[1]
		# 										Broadcast(sala_idx, idx, "Usuario " + str(Users[idx].uname) + " entrou na sala!")												
		# 										logging.info("Usuario " + uname + " entrou na sala " + my_list[1] + ". Endereco: " + str(Users[idx].ip) + "/" + str(Users[idx].port))
		# 									else:
		# 										msg = "Senha incorreta!"
		# 										logging.info("Usuario " + uname + " tentou entrar na sala " + my_list[1] + ". Endereco: " + str(Users[idx].ip) + "/" + str(Users[idx].port))
		# 							else:
		# 								# Sala publica, qualquer um entra
		# 								Users[idx].sala = int(my_list[1])
		# 								Salas[sala_idx].usuarios.append(idx)
		# 								msg = "Movido para a sala " + my_list[1]
		# 								Broadcast(sala_idx, idx, "Usuario " + str(Users[idx].uname) + " entrou na sala!")
		# 								logging.info("Usuario " + uname + " tentou entrar na sala " + my_list[1] + ". Endereco: " + str(Users[idx].ip) + "/" + str(Users[idx].port))														
		# 						else:
		# 							msg = "Nao foi possivel identificar a sala desejada!"	
		# 					else:
		# 						msg = "Nao foi possivel identificar a sala desejada!"						
					
		# 			sock.send(msg)
		# 		elif data[0:2] == "-s":
		# 			if Users[idx].sala == -1:
		# 				msg = "Voce nao pode sair do menu principal!"
		# 			else:
		# 				sala_atual = salas_map[Users[idx].sala]
		# 				Salas[sala_atual].usuarios.remove(idx)
		# 				Broadcast(sala_atual, idx, "Usuario " + Users[idx].uname + " saiu da sala!")
		# 				msg = "Voce saiu da sala " + str(Users[idx].sala)
		# 				logging.info("Usuario " + uname + " saiu da sala " + str(Users[idx].sala) + ". Endereco: " + str(Users[idx].ip) + "/" + str(Users[idx].port))
		# 				Users[idx].sala = -1 
						
		# 			sock.send(msg)
		# 		# Lista os usuarios da sala	
		# 		elif data[0:2] == "-u":
		# 			if Users[idx].sala == -1:
		# 				msg = "Este comando deve ser usado quando dentro de uma sala!"
		# 			else:
		# 				msg = "Usuarios na sala " + str(Users[idx].sala) + ":\n"
		# 				logging.info("Usuario " + uname + " listou os usuarios na sala " + str(Users[idx].sala) + ". Endereco: " + str(Users[idx].ip) + "/" + str(Users[idx].port))
		# 				sala_idx = salas_map[Users[idx].sala]
		# 				for i in range(len(Salas[sala_idx].usuarios)):
		# 					msg += Users[Salas[sala_idx].usuarios[i]].uname + "\n"
						
		# 			sock.send(msg)
		# 		# Cria uma nova sala	
		# 		elif data[0:2] == "-c":
		# 			if Users[idx].sala != -1:
		# 				msg = "Voce deve primeiro sair da sua sala!"
		# 			else:
		# 				my_list = data.split(' ')

		# 				if len(my_list) == 3:
		# 					if my_list[1].isdigit():
		# 						if int(my_list[1]) in salas_map:
		# 							msg = "Identificador ja esta em uso!"
		# 							logging.info("Tentativa de recriar a sala " + my_list[1] + " pelo usuario " + uname + ". Endereco: " + str(Users[idx].ip) + "/" + str(Users[idx].port))
		# 						else:
		# 							Salas.append(Sala(1, int(my_list[1]), my_list[2]))
		# 							salas_map[int(my_list[1])] = len(Salas) - 1	
									
		# 							# Insere o usuario na sala
		# 							Salas[-1].usuarios.append(idx)
		# 							Users[idx].sala = int(my_list[1])
		# 							msg = "Sala criada e movido para a nova sala."
		# 							logging.info("Sala " + my_list[1] + " privada, criada pelo usuario " + uname + ". Endereco: " + str(Users[idx].ip) + "/" + str(Users[idx].port))
		# 							logging.info("Usuario " + uname + " entrou na sala " + my_list[1] + ". Endereco: " + str(Users[idx].ip) + "/" + str(Users[idx].port))
		# 					else:
		# 						msg = "Informe um identificador valido para a nova sala!"
							
		# 				elif len(my_list) == 2:
		# 					if my_list[1].isdigit():
		# 						if int(my_list[1]) in salas_map:
		# 							msg = "Identificador ja esta em uso!"
		# 							logging.info("Tentativa de recriar a sala " + my_list[1] + " pelo usuario " + uname + ". Endereco: " + str(Users[idx].ip) + "/" + str(Users[idx].port))
		# 						else:
		# 							Salas.append(Sala(0, int(my_list[1])))
		# 							salas_map[int(my_list[1])] = len(Salas) - 1	
									
		# 							# Insere o usuario na sala
		# 							Salas[-1].usuarios.append(idx)
		# 							Users[idx].sala = int(my_list[1])
		# 							msg = "Sala criada e movido para a nova sala."
		# 							logging.info("Sala " + my_list[1] + " publica, criada pelo usuario " + uname + ". Endereco: " + str(Users[idx].ip) + "/" + str(Users[idx].port))
		# 							logging.info("Usuario " + uname + " entrou na sala " + my_list[1] + ". Endereco: " + str(Users[idx].ip) + "/" + str(Users[idx].port))									
		# 					else:
		# 						msg = "Informe um identificador valido para a nova sala!"
													
		# 				else :
		# 					msg = "Numero de argumentos incorretos!"
					
		# 			sock.send(msg)
		# 		elif data[0:2] == "-a":
		# 			# Apaga a sala
		# 			if len(data) < 4:
		# 				# Nao tem chars suficientes
		# 				msg = "Nao foi possivel identificar a sala desejada!"
		# 			else:
		# 				my_list = data.split(' ')
		# 				# Checa se eh numero
		# 				if my_list[1].isdigit():
		# 					if int(my_list[1]) in salas_map:
		# 						# Sala existe
		# 						sala_idx = salas_map[int(my_list[1])]
		# 						if sala_idx != 0:
		# 							if len(Salas[sala_idx].usuarios) != 0:
		# 								msg = "Sala nao esta vazia, nao pode ser apagada!"
		# 								logging.info("Tentativa de apagar a sala " + my_list[1] + " pelo usuario " + uname + ". Endereco: " + str(Users[idx].ip) + "/" + str(Users[idx].port))
		# 							else:
		# 								# Delete by index
		# 								del Salas[sala_idx]
		# 								atualiza_dict(sala_idx)
		# 								del salas_map[int(my_list[1])]
									
		# 								msg = "Sala " + my_list[1] + " removida!"
		# 								# Insere no log
		# 								logging.info("Sala " + my_list[1] + " removida pelo usuario " + uname + ". Endereco: " + str(Users[idx].ip) + "/" + str(Users[idx].port))
		# 						else:
		# 							msg = "Esta sala nao pode ser apagada!"
		# 							logging.info("Tentativa de apagar a sala " + my_list[1] + " pelo usuario " + uname + ". Endereco: " + str(Users[idx].ip) + "/" + str(Users[idx].port))
		# 					else:
		# 						msg = "Nao foi possivel identificar a sala desejada!"
		# 						logging.info("Tentativa de apagar a sala " + my_list[1] + " pelo usuario " + uname + ". Endereco: " + str(Users[idx].ip) + "/" + str(Users[idx].port))		
		# 				else:
		# 					msg = "Nao foi possivel identificar a sala desejada!"
					
		# 			sock.send(msg)		
		# 		elif data[0:2] == "-h":
		# 			sock.send("MENU")
		# 		elif data[0:2] == "-f":
		# 			if data[2] == ' ':
		# 				if Users[idx].sala != -1 and file_reading == False:
		# 					msg = "-sendfileOK"
		# 					file_reading = True
		# 					my_list = data.split('/')
		# 					file_name = my_list[-1]
		# 				else:
		# 					msg = "Nao e possivel enviar arquivos neste momento!"
		# 				sock.send(msg)	
		# 			else:
		# 				# User sending file, concatenates into file string
		# 				file_info = file_info + data[5:]
		# 		elif data == "--file":
		# 			sock.send("Arquivo enviado!")
		# 			thread_file_broadcast = threading.Thread(target=file_broadcast, args=[Users[idx].sala, idx])
		# 			thread_file_broadcast.start()
				# elif data == "exit":
				# 	if Users[idx].sala != -1:
				# 		msg = "Por favor saia da sua sala primeiro!"
				# 		sock.send(msg)
				# 	else:	
				# 		print "Pedido de encerramento de conexao por " + str(Users[idx].ip) + "/" + str(Users[idx].port) + "."
				# 		sock.send(data)
				# 		time.sleep(2)
				# 		sock.close()
				# 		logging.info("Conexao finalizada pelo usuario " + uname + ". Endereco: " + str(Users[idx].ip) + "/" + str(Users[idx].port))
				# 		print "Conexao encerrada!"
				# 		break	
		# 		else:
		# 			# Mensagem no geral, so faz o broadcast pela sala
		# 			if Users[idx].sala != -1:
		# 				Broadcast(salas_map[Users[idx].sala], -1, Users[idx].uname + ": " + data)
		# 			else:
		# 				msg = "Entre em uma sala para trocar mensagens!"
		# 				sock.send(msg)             	

# Terminal execution
if __name__ == "__main__":
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

    # Comeca a escutar
    server_socket.listen(10)

    IP = socket.gethostbyname(socket.gethostname())
    PORT = server_socket.getsockname()[1]	# Get the port the OS used

    clear_screen()
    print(IP)

    if port == 0:
        print("Conecte-se utilizando a porta " + str(PORT))

    # Cria sala publica mestre
    # Salas.append(Sala(0, 0))
    # salas_map[0] = len(Salas) - 1

    while True:
    # Verifica se alguem tentou conectar
        try:
            # Aceita nova conexao
            sck, full_address = server_socket.accept()

            print(sck, full_address)

            # Inicia uma thread para essa conexao
            thread_station = threading.Thread(target=conecta, args=[sck])
            thread_station.start()
        except (KeyboardInterrupt):
            sys.exit(0)