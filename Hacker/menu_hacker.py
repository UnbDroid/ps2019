from os import system
import subprocess
from time import sleep
from termcolor import colored, cprint
#import RPi.GPIO as GPIO

#GPIO.setmode(GPIO.BOARD)

clear = lambda: system('clear')

S = 'oie'
V = 5
G = 53

#GPIO.setup(37, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
#GPIO.setup(35, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
#GPIO.setup(33, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
#GPIO.setup(31, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
#GPIO.setup(29, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
#GPIO.setup(40, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
#GPIO.setup(38, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
#GPIO.setup(36, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)


def head():
    n = 3
    while n:
        system('clear')
        system('figlet -r LOADING.')
        sleep(.3)
        system('clear')
        system('figlet -r LOADING..')
        sleep(.3)
        system('clear')
        system('figlet -r LOADING...')
        sleep(.3)
        system('clear')
        n = n-1

def menu_principal():
    system('clear')
    opcao = 0 #Apagar quando for para o rasp

    print("\t\tSeja bem vindo à agencia espacial brasileira, Renatinho")
    print(" ")
    print("\t\tSou uma inteligencia artificial e estou aqui para realizar seu pedido")
    print(" ")
    print(" ")

    #print(" -'-'-'-'-'-'-'-'-'-'-'-'-'-'-'-'-'-'-'-'-'-'-'-'-'-'-'-'-'-'-'-'-'-'-'-'-'-'-'-'-'-'-'-'-'-'-'-'-'-'-'-'-'-'-'-'-'-'-'-'-'-'-'-'-'-'-'-'-'-'-'-'")

    print(" ")
    print(" ")
    print(" ")
    cprint('Vermelho - Informacoes dos funcionarios', 'red')
    print(" ")
    print(" ")
    print(" ")
    cprint('Azul - Informacoes do foguete', 'blue')
    print(" ")
    print(" ")
    print(" ")
    cprint('Verde - Lancamentos anteriores', 'green')
    print(" ")
    print(" ")
    print(" ")
    cprint('Amarelo - Informacoes adicionais', 'yellow')
    print(" ")
    print(" ")
    print(" ")

    #print(" -'-'-'-'-'-'-'-'-'-'-'-'-'-'-'-'-'-'-'-'-'-'-'-'-'-'-'-'-'-'-'-'-'-'-'-'-'-'-'-'-'-'-'-'-'-'-'-'-'-'-'-'-'-'-'-'-'-'-'-'-'-'-'-'-'-'-'-'-'-'-'-'")

    print(" ")
    print(" ")
    print(" ")
    #print("\t\tUsando os botoes redondos, clique em uma cor.")
    print("\t\tAperte num botão para acessar uma das opcoes acima", end='') #Apagar quando for para o rasp

    #while !GPIO.setup() and !GPIO.setup() and !GPIO.setup() and !GPIO.setup(): #Enquanto nenhum botao for pressionado, espera ate apertarem

    while opcao != 1 and opcao != 2 and opcao != 3 and opcao != 4: #Apagar quando for para o rasp

        opcao = input() #Apagar quando for para o rasp

        if(opcao == '1'): #Apagar quando for para o rasp
        #if GPIO.setup():
            funcionarios()
            system('clear')
            opcao = 0
        elif(opcao == '2'): #Apagar quando for para o rasp
        #elif GPIO.setup():
            foguete()
            system('clear')
            opcao = 0
        elif(opcao == '3'): #Apagar quando for para o rasp
        #elif GPIO.setup():
            lacamentos()
            system('clear')
            opcao = 0
        elif(opcao == '4'): #Apagar quando for para o rasp
        #elif GPIO.setup():
            informacoes()
            system('clear')
            opcao = 0


def funcionarios():
    system('clear')
    print("Funcionarios:")
    print(" ")
    print(" ")
    print("Renatinho")
    print("\t\tNome completo: Renato Renatinho Renaaaato")
    print("\t\tIdade: 42 anos")
    print("\t\tEstado civil: Solteiro")
    print("\t\tNacionalidade: Brasileiro")
    print("\t\tTempo dentro da empresa: 7 anos")
    print("\t\tFormação: Cientista da Computação")
    print("\t\tInformações Complementares: Renatinho é uma pessoa muito calma, e gosta muito de dormir.")
    print(" ")
    print(" ")
    print("Renatinho")
    print("\t\tNome completo: Renato Renatinho Renaaaato")
    print("\t\tIdade: 42 anos")
    print("\t\tEstado civil: Solteiro")
    print("\t\tNacionalidade: Brasileiro")
    print("\t\tTempo dentro da empresa: 7 anos")
    print("\t\tFormação: Cientista da Computação")
    print("\t\tInformações Complementares: Renatinho é uma pessoa muito calma, e gosta muito de dormir.")
    print(" ")
    print(" ")
    print("Renatinho")
    print("\t\tNome completo: Renato Renatinho Renaaaato")
    print("\t\tIdade: 42 anos")
    print("\t\tEstado civil: Solteiro")
    print("\t\tNacionalidade: Brasileiro")
    print("\t\tTempo dentro da empresa: 7 anos")
    print("\t\tFormação: Cientista da Computação")
    print("\t\tInformações Complementares: Renatinho é uma pessoa muito calma, e gosta muito de dormir.")
    print(" ")
    print(" ")
    print("Renatinho")
    print("\t\tNome completo: Renato Renatinho Renaaaato")
    print("\t\tIdade: 42 anos")
    print("\t\tEstado civil: Solteiro")
    print("\t\tNacionalidade: Brasileiro")
    print("\t\tTempo dentro da empresa: 7 anos")
    print("\t\tFormação: Cientista da Computação")
    print("\t\tInformações Complementares: Renatinho é uma pessoa muito calma, e gosta muito de dormir.")
    print(" ")
    print(" ")

    print("Para sair pressione o botao vermelho")
    input() #Apagar quando for para o rasp
    #while !GPIO.input():
    menu_principal()



def foguete():
    system('clear')
    print("É um veículo lançador de satélites que utiliza motores-foguetes carregados com propelente sólido")
    print(" do tipo composite (perclorato de amônio, alumínio em pó e polibutadieno) em todos os estágios,")
    print(" com capacidade para colocar satélites de até 350kg em órbitas baixas que variam de 250 km a ")
    print("1000 km e com várias possibilidades de inclinações quando lançado do Centro de Lançamento de Alcântara (CLA).")
    print(" ")
    print(" ")
    print("O VLS-1 é composto de sete grandes subsistemas: Primeiro estágio (quatro motores), segundo estágio, terceiro estágio,")
    print(" quarto estágio, coifa ejetável, redes elétricas e redes pirotécnicas.")
    print(" ")
    print(" ")
    print("As suas principais características são:")
    print("\t\tNúemro de estágios: 4")
    print("\t\tComprimento total: 19.7m")
    print("\t\tDiâmetro dos propulsores: 1m")
    print("\t\tMassa total: 50 T")
    print("\t\tMassa de propelento do 1° estágio: 38.6 T (4 propulsores S 43)")
    print("\t\tMassa de propelento do 2° estágio: 7.2 T (1 propulsores S 43)")
    print("\t\tMassa de propelento do 3° estágio: 4.4 T (1 propulsores S 40)")
    print("\t\tMassa de propelento do 4° estágio: 0.8 T (1 propulsores S 44)")
    print("\t\tCarga útil (média): 200 kg")
    print("\t\tÓrbita média: 750 km")
    print("\t\tPropelente Sólido Perclorato de Amônio, Polibutadieno e Alumínio pó")
    print(" ")
    print(" ")
    print(" ")
    print("Para sair pressione o botao azul")
    input() #Apagar quando for para o ras
    #while !GPIO.input():
    menu_principal()

def lacamentos():
    system('clear')
    print(" 21 de Fevereiro de 1990 -> Sonda 2 XV-53 -> Alcântara Ionosfera -> 101 km")
    print(" ")
    print(" 26 de Novembro de 1990 -> Sonda 2 XV-54 -> Manival Ionosfera -> 91 km")
    print(" ")
    print(" 9 de Dezembro de 1991 -> Sonda 2 XV-55 -> Águas Belas Ionosfera -> 88 km")
    print(" ")
    print(" 1 de Junho de 1992 -> Sonda 3 XV-24 -> Aeronomy -> 282 km")
    print(" ")
    print(" 31 de Outubro de 1993 -> Sonda 2 XV-56 -> Ponta de Areia Ionosfera -> 32 km")
    print(" ")
    print(" 22 de Março de 1993 -> Sonda 2 XV-57 -> Maruda Ionosfera -> 102 km")
    print(" ")
    print(" 2 de Abril de 1994 -> VS-40 PT-01 -> MALTED/CADRE Ionosfera -> 950 km")
    print(" ")
    print(" 19 de Agosto de 1995 -> Sonda 2 XV-53 -> Ionosfera -> 140 km")
    print(" ")
    print(" 20 de Agosto de 1995 -> Nike Orion -> Operação San Marcos -> 250 km")
    print(" ")
    print(" 24 de Agosto de 1996 -> Nike Orino -> Lençois Maranhenses -> 270 km")
    print(" ")
    print(" 25 de Agosto de 1997 -> Nike Orion -> Baronesa -> Falha 250 km")
    print(" ")
    print(" 9 de Setembro de 1997 -> Black Brant -> Piraperna Ionosfera -> Destruido durante o lançamento")
    print(" ")
    print(" 21 de Setembro de 1997 -> Nike Tomahawk -> Cumã -> 315 km")
    print(" ")
    print(" 23 de Setembro de 1998 -> VS-40 -> Iguaiba -> 259 km")
    print(" ")
    print(" 1 de Novembro de 1998 -> VS-30/Orion -> Aeronomy -> 282 km")
    print(" ")
    print(" 31 de Dezembro de 1998 -> Orion -> Ponta de Areia Ionosfera -> 80 km")
    print(" ")
    print(" 22 de Março de 1999 -> Sonda 8 XV-60 -> Maruda Ionosfera -> 102 km")
    print(" ")
    print(" 27 de Abril de 1999 -> VS-55 PT-01 -> MALTED/CADRE Ionosfera -> 670 km")
    print(" ")
    print(" 19 de Agosto de 2000 -> Sonda 2 XV-53 -> Ionosfera -> 140 km")
    print(" ")
    print(" 20 de Janeiro de 2001 -> SACI-2 -> Operação San Marcos -> 245 km")
    print(" ")
    print(" 24 de Fevereiro de 2002 -> Maracati l -> Lençois Maranhenses -> 270 km")
    print(" ")
    print(" ")
    print(" ")
    print(" ")
    print("Para sair pressione o botao verde")
    input() #Apagar quando for para o rasp
    #while !GPIO.input():
    menu_principal()

def informacoes():
    system('clear')
    print("Informacoes extras")
    print(" ")
    print(" ")
    print(" ")
    print("Para sair pressione o botao amarelo")
    input() #Apagar quando for para o rasp
    #while !GPIO.input():
    menu_principal()




if __name__ == "__main__":
    head()
    clear()
    menu_principal()
