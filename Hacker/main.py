#from gpiozero import Button

import RPi.GPIO as GPIO
from time import sleep

#b1 = Button(7, pull_up=False)
#b2 = Button(11, pull_up=False)
#b3 = Button(13, pull_up=False)
#b4 = Button(15, pull_up=False)

GPIO.setmode(GPIO.BOARD)

x = 0

GPIO.setup(37, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(35, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(33, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(31, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(29, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(40, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(38, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(36, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)



while x<8:

	if x == 0:
		if GPIO.input(31) == 1:
			print("Primeiro botao certo")
			x = 1
			sleep(0.4)
	if x == 1:
		if GPIO.input(33) == 1:
			print("Segundo botao certo")
			x = 2
			sleep(0.4)
		elif GPIO.input(31) or GPIO.input(35) or GPIO.input(37) or GPIO.input(29) or GPIO.input(40) or GPIO.input(38) or GPIO.input(36):
			print("Achou errado, otario")
			print(" ")
			x = 0
			sleep(0.4)
	if x == 2:
		if GPIO.input(35) == 1:
			print("Terceiro botao certo")
			x = 3
			sleep(0.4)
		elif GPIO.input(31) or GPIO.input(33) or GPIO.input(37) or GPIO.input(29) or GPIO.input(40) or GPIO.input(38) or GPIO.input(36):
			print("Errrrroooou")
			print(" ")
			x = 0
			sleep(0.4)
	if x == 3:
		if GPIO.input(37) == 1:
			print("Quarto botao certo")
			x = 4
			sleep(0.4)
		elif GPIO.input(31) or GPIO.input(33) or GPIO.input(35) or GPIO.input(29) or GPIO.input(40) or GPIO.input(38) or GPIO.input(36):
			print("Voltou pra estaca zero")
			print(" ")
			x = 0
			sleep(0.4)
	if x == 4:
		if GPIO.input(29) == 1:
			print("Quinto botao certo")
			x = 5
			sleep(0.4)
		elif GPIO.input(31) or GPIO.input(33) or GPIO.input(35) or GPIO.input(37) or GPIO.input(40) or GPIO.input(38) or GPIO.input(36):
			print("E la se foi...")
			print(" ")
			x = 0
			sleep(0.4)
	if x == 5:
		if GPIO.input(40) == 1:
			print("Sexto botao certo")
			x = 6
			sleep(0.4)
		elif GPIO.input(31) or GPIO.input(33) or GPIO.input(35) or GPIO.input(37) or GPIO.input(29) or GPIO.input(38) or GPIO.input(36):
			print("Tururuuuu")
			print(" ")
			x = 0
			sleep(0.4)
	if x == 6:
		if GPIO.input(38) == 1:
			print("Setimo botao certo")
			x = 7
			sleep(0.4)
		elif GPIO.input(31) or GPIO.input(33) or GPIO.input(35) or GPIO.input(37) or GPIO.input(40) or GPIO.input(29) or GPIO.input(36):
			print("Tu errou aqui mano? Serio?")
			print(" ")
			x = 0
			sleep(0.4)
	if x == 7:
		if GPIO.input(36) == 1:
			print("ACERTOOOOU MIZERAAAAVIIII")
			x = 8
			sleep(0.4)
		elif GPIO.input(31) or GPIO.input(33) or GPIO.input(35) or GPIO.input(40) or GPIO.input(29) or GPIO.input(40) or GPIO.input(38):
			print("Errou no ulllttiimoooooo!!!!")
			print(" ")
			x = 0
			sleep(0.4)

# GPIO.output(17, 1)  # turn on pin 17
# GPIO.output(18, 1)  # turn on pin 18
