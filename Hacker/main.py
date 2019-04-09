import RPi.GPIO as GPIO
import time
from os import system

botao_0 = 37
botao_1 = 35
botao_2 = 33
botao_3 = 31
botao_4 = 29
botao_5 = 40
botao_6 = 38
botao_7 = 36
led = 11

GPIO.setmode(GPIO.BOARD)

x = 0

GPIO.setup(botao_0, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(botao_1, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(botao_2, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(botao_3, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(botao_4, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(botao_5, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(botao_6, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(botao_7, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(led, GPIO.OUT)

sequence = [botao_5, botao_3, botao_7, botao_4, botao_1, botao_2, botao_6, botao_0]

reset = True

def not_right(x, i):
	if(i<x):
		return sequence[i]
	else:
		return sequence[i+1]	


try:
	GPIO.output(led, GPIO.LOW)
	last_time = time.time()
	while x<8:
		if time.time() - last_time > 5: #Verificar esse tempo
			reset = True
		if reset is True:
			system('clear')
			last_time = time.time()
			reset = False
			print("HAHAHA you didn't say the magic word...")
								
		if x == 0:
			if GPIO.input(sequence[x]) == 1:
				system('clear')
				print("Voce nunca conseguira descobrir a sequencia correta...")
				x = 1
				last_time = time.time()
				time.sleep(0.4)
			elif GPIO.input(not_right(x, 0)) or GPIO.input(not_right(x, 1)) or GPIO.input(not_right(x, 2)) or GPIO.input(not_right(x, 3)) or GPIO.input(not_right(x, 4)) or GPIO.input(not_right(x, 5)) or GPIO.input(not_right(x, 6)):
				reset = True
				x = 0
				GPIO.output(led, GPIO.HIGH)
				time.sleep(0.4)
				GPIO.output(led, GPIO.LOW)
		if x == 1:
			if GPIO.input(sequence[x]) == 1:
				system('clear')
				print("Suas tentativas sao em vao...")
				x = 2
				last_time = time.time()
				time.sleep(0.4)
			elif GPIO.input(not_right(x, 0)) or GPIO.input(not_right(x, 1)) or GPIO.input(not_right(x, 2)) or GPIO.input(not_right(x, 3)) or GPIO.input(not_right(x, 4)) or GPIO.input(not_right(x, 5)) or GPIO.input(not_right(x, 6)):
				reset = True
				x = 0
				GPIO.output(led, GPIO.HIGH)
				time.sleep(0.4)
				GPIO.output(led, GPIO.LOW)
		if x == 2:
			if GPIO.input(sequence[x]) == 1:
				system('clear')
				print("Ta frio...")
				x = 3
				last_time = time.time()
				time.sleep(0.4)
			elif GPIO.input(not_right(x, 0)) or GPIO.input(not_right(x, 1)) or GPIO.input(not_right(x, 2)) or GPIO.input(not_right(x, 3)) or GPIO.input(not_right(x, 4)) or GPIO.input(not_right(x, 5)) or GPIO.input(not_right(x, 6)):
				reset = True
				x = 0
				GPIO.output(led, GPIO.HIGH)
				time.sleep(0.4)
				GPIO.output(led, GPIO.LOW)
		if x == 3:
			if GPIO.input(sequence[x]) == 1:
				system('clear')
				print("Voces vao mesmo deixar o foguete explodir?")
				x = 4
				last_time = time.time()
				time.sleep(0.4)
			elif GPIO.input(not_right(x, 0)) or GPIO.input(not_right(x, 1)) or GPIO.input(not_right(x, 2)) or GPIO.input(not_right(x, 3)) or GPIO.input(not_right(x, 4)) or GPIO.input(not_right(x, 5)) or GPIO.input(not_right(x, 6)):
				reset = True
				x = 0
				GPIO.output(led, GPIO.HIGH)
				time.sleep(0.4)
				GPIO.output(led, GPIO.LOW)
		if x == 4:
			if GPIO.input(sequence[x]) == 1:
				system('clear')
				print("As mentes brilhantes do Brasil nao sao de nada...")
				x = 5
				last_time = time.time()
				time.sleep(0.4)
			elif GPIO.input(not_right(x, 0)) or GPIO.input(not_right(x, 1)) or GPIO.input(not_right(x, 2)) or GPIO.input(not_right(x, 3)) or GPIO.input(not_right(x, 4)) or GPIO.input(not_right(x, 5)) or GPIO.input(not_right(x, 6)):
				reset = True
				x = 0
				GPIO.output(led, GPIO.HIGH)
				time.sleep(0.4)
				GPIO.output(led, GPIO.LOW)
		if x == 5:
			if GPIO.input(sequence[x]) == 1:
				system('clear')
				print("Pare de tentar isso...")
				x = 6
				last_time = time.time()
				time.sleep(0.4)
			elif GPIO.input(not_right(x, 0)) or GPIO.input(not_right(x, 1)) or GPIO.input(not_right(x, 2)) or GPIO.input(not_right(x, 3)) or GPIO.input(not_right(x, 4)) or GPIO.input(not_right(x, 5)) or GPIO.input(not_right(x, 6)):
				reset = True
				x = 0
				GPIO.output(led, GPIO.HIGH)
				time.sleep(0.4)
				GPIO.output(led, GPIO.LOW)
		if x == 6:
			if GPIO.input(sequence[x]) == 1:
				system('clear')
				print("Se voce errar agora todo mundo morrera!")
				x = 7
				last_time = time.time()
				time.sleep(0.4)
			elif GPIO.input(not_right(x, 0)) or GPIO.input(not_right(x, 1)) or GPIO.input(not_right(x, 2)) or GPIO.input(not_right(x, 3)) or GPIO.input(not_right(x, 4)) or GPIO.input(not_right(x, 5)) or GPIO.input(not_right(x, 6)):
				reset = True
				x = 0
				GPIO.output(led, GPIO.HIGH)
				time.sleep(0.4)
				GPIO.output(led, GPIO.LOW)
		if x == 7:
			if GPIO.input(sequence[x]) == 1:
				system('clear')
				print("Aaaaarrghh, voce passou por isso, mas o foguete ainda explodira...")
				x = 8
				last_time = time.time()
				time.sleep(0.4)
			elif GPIO.input(not_right(x, 0)) or GPIO.input(not_right(x, 1)) or GPIO.input(not_right(x, 2)) or GPIO.input(not_right(x, 3)) or GPIO.input(not_right(x, 4)) or GPIO.input(not_right(x, 5)) or GPIO.input(not_right(x, 6)):
				reset = True
				x = 0
				GPIO.output(led, GPIO.HIGH)
				time.sleep(0.4)
				GPIO.output(led, GPIO.LOW)
	GPIO.cleanup()

except KeyboardInterrupt:
	print("Fugiu ne?")
	GPIO.cleanup()

