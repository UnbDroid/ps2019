from os import system
from time import sleep
import RPi.GPIO as GPIO

#clear = lambda: system('clear')

botao_vermelho = 33
botao_azul = 35
botao_verde = 37
botao_amarelo = 31

GPIO.setmode(GPIO.BOARD)

GPIO.setup(botao_vermelho, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(botao_azul, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(botao_verde, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(botao_amarelo, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)


S = 'oie'
V = 5
G = 53

def head():
    n = 3
    while n:
        system('clear')
        print("LOADING.")
        sleep(.3)
        system('clear')
        print("figlet -r LOADING..")
        sleep(.3)
        system('clear')
        print("figlet -r LOADING...")
        sleep(.3)
        system('clear')
        n = n-1

def menu_principal():
    system('clear')
    opcao = 0 #Apagar quando for para o rasp

    print("\t\tSeja bem vindo a central de controle da agencia espacial brasileira")
    print(" ")
    print("\t\tSou uma inteligencia artificial e estou aqui para realizar seu pedido")
    print(" ")
    print(" ")

    #print(" -'-'-'-'-'-'-'-'-'-'-'-'-'-'-'-'-'-'-'-'-'-'-'-'-'-'-'-'-'-'-'-'-'-'-'-'-'-'-'-'-'-'-'-'-'-'-'-'-'-'-'-'-'-'-'-'-'-'-'-'-'-'-'-'-'-'-'-'-'-'-'-'")

    print(" ")
    print(" ")
    print(" ")
    print("\n\033[32m" + "Verde - Lancamentos anteriores" + "\033[0m\n")
    print(" ")
    print(" ")
    print(" ")
    print("\n\033[34m" + "Azul - Informacoes do foguete" + "\033[0m\n")
    print(" ")
    print(" ")
    print(" ")
    print("\n\033[31m" + "Vermelho - Informacoes dos funcionarios" + "\033[0m\n")
    print(" ")
    print(" ")
    print(" ")
    print("\n\033[33m" + "Amarelo - Informacoes adicionais" + "\033[0m\n")
    print(" ")
    print(" ")
    print(" ")

    #print(" -'-'-'-'-'-'-'-'-'-'-'-'-'-'-'-'-'-'-'-'-'-'-'-'-'-'-'-'-'-'-'-'-'-'-'-'-'-'-'-'-'-'-'-'-'-'-'-'-'-'-'-'-'-'-'-'-'-'-'-'-'-'-'-'-'-'-'-'-'-'-'-'")

    print(" ")
    print(" ")
    print(" ")
    #print("\t\tUsando os botoes redondos, clique em uma cor.")
    print("\t\tAperte um botao para acessar uma das opcoes acima")

    opcao = ''

    while True:
        if GPIO.input(botao_vermelho):
            opcao = '1'
            sleep(.4)
            break
        if GPIO.input(botao_azul):
            opcao = '2'
            sleep(.4)
            break
        if GPIO.input(botao_verde):
            opcao = '3'
            sleep(.4)
            break
        if GPIO.input(botao_amarelo):
            opcao = '4'
            sleep(.4)
            break

    if(opcao == '1'):
        funcionarios()
        system('clear')
    elif(opcao == '2'):
        foguete()
        system('clear')
    elif(opcao == '3'):
        lacamentos()
        system('clear')
        opcao = 0
    elif(opcao == '4'):
        informacoes()
        system('clear')
        opcao = 0


def funcionarios():
    while GPIO.input(botao_vermelho):
        pass

    system('clear')
    print("Funcionarios:")
    print(" ")
    print(" ")
    print("Area: Planejamento, orçamento e administracao")
    print("\t\tNome completo: Ana Carolina Paulino")
    print("\t\tIdade: 26 anos")
    print("\t\tEstado civil: Casado")
    print("\t\tNacionalidade: Brasileiro")
    print("\t\tTempo dentro da empresa: 10 anos")
    print("\t\tFormacao: Engenheira de Controle e Automacao")
    print("\t\tInformacoes Complementares: Atenciosa, paciente e extremamente fofa.")
    print(" ")
    print(" ")
    print("\t\tNome completo: Thiago Queiroz Holanda")
    print("\t\tIdade: 24 anos")
    print("\t\tEstado civil: Solteiro")
    print("\t\tNacionalidade: Brasileiro")
    print("\t\tTempo dentro da empresa: 5 anos")
    print("\t\tFormacao: Estudante de Engenharia de Controle e Automacao")
    print("\t\tInformacoes Complementares: Analista de comportamento humano")
    print(" ")
    print(" ")
    print("Area: Politica espacial e investimentos estrategicos")
    print("\t\tNome completo: Felipe de Paula Lima")
    print("\t\tIdade: 30 anos")
    print("\t\tEstado civil: Solteiro")
    print("\t\tNacionalidade: Brasileiro")
    print("\t\tTempo dentro da empresa: 10 anos")
    print("\t\tFormacao: Engenheiro de Controle e Automacao")
    print("\t\tInformacoes Complementares: Especialista em hardware e focado no trabalho")
    print(" ")
    print(" ")
    print("Area: Satelites, aplicacoes e desenvolvimento")
    print("\t\tNome completo: Giordano Melo Gois")
    print("\t\tIdade: 30 anos")
    print("\t\tEstado civil: Casado")
    print("\t\tNacionalidade: Brasileiro")
    print("\t\tTempo dentro da empresa: 10 anos")
    print("\t\tFormacao: Engenheiro de Controle e Automacao")
    print("\t\tInformacoes Complementares: Excelente programador e fissurado por LEDs")
    print(" ")
    print(" ")
    print("\t\tNome completo: Sara Gomes Cardoso")
    print("\t\tIdade: 22 anos")
    print("\t\tEstado civil: Solteiro")
    print("\t\tNacionalidade: Brasileiro")
    print("\t\tTempo dentro da empresa: 4 anos")
    print("\t\tFormacao: Estudante de Engenharia de Controle e Automacao")
    print("\t\tInformacoes Complementares: Especialista em tirar xerox de documentos importantes")
    print(" ")
    print(" ")
    print("Area: Transporte espacial e licenciamento")
    print("\t\tNome completo: Marcela Pinheiro de Carvalho")
    print("\t\tIdade: 26 anos")
    print("\t\tEstado civil: Casado")
    print("\t\tNacionalidade: Brasileiro")
    print("\t\tTempo dentro da empresa: 10 anos")
    print("\t\tFormacao: Engenharia de Controle e Automacao")
    print("\t\tInformacoes Complementares: Emgraçada e especialista em montagens e edição e imagens")
    print(" ")
    print(" ")

    print("Para sair pressione o botao vermelho")
    while not GPIO.input(botao_vermelho):
        pass
    sleep(.4)
    menu_principal()



def foguete():
    while GPIO.input(botao_azul):
        pass

    system('clear')
    print("E um veiculo lancador de satelites que utiliza motores-foguetes carregados com propelente solido")
    print(" do tipo composite (perclorato de amonio, aluminio em po e polibutadieno) em todos os estagios,")
    print(" com capacidade para colocar satelites de ate 350kg em orbitas baixas que variam de 250 km a ")
    print("1000 km e com varias possibilidades de inclinacoes quando lancado do Centro de Lancamento de Alcantara (CLA).")
    print(" ")
    print(" ")
    print("O VLS-1 e composto de sete grandes subsistemas: Primeiro estagio (quatro motores), segundo estagio, terceiro estagio,")
    print(" quarto estagio, coifa ejetavel, redes eletricas e redes pirotecnicas.")
    print(" ")
    print(" ")
    print("As suas principais caracteristicas sao:")
    print("\t\tNumero de estagios: 4")
    print("\t\tComprimento total: 19.7m")
    print("\t\tDiametro dos propulsores: 1m")
    print("\t\tMassa total: 50 T")
    print("\t\tMassa de propelento do 1 estagio: 38.6 T (4 propulsores S 43)")
    print("\t\tMassa de propelento do 2 estagio: 7.2 T (1 propulsor S 43)")
    print("\t\tMassa de propelento do 3 estagio: 4.4 T (1 propulsor S 40)")
    print("\t\tMassa de propelento do 4 estagio: 0.8 T (1 propulsor S 44)")
    print("\t\tCarga util (media): 200 kg")
    print("\t\tOrbita media: 750 km")
    print("\t\tPropelente Solido Perclorato de Amonio, Polibutadieno e Aluminio po")
    print(" ")
    print(" ")
    print(" ")
    print("Para sair pressione o botao azul")
    while not GPIO.input(botao_azul):
        pass
    sleep(.4)
    menu_principal()

def lacamentos():
    while GPIO.input(botao_verde):
        pass

    system('clear')
    print(" 21 de Fevereiro de 1990 -> Sonda 2 XV-53 -> Alcantara Ionosfera -> 101 km")
    print(" ")
    print(" 26 de Novembro de 1990 -> Sonda 2 XV-54 -> Manival Ionosfera -> 91 km")
    print(" ")
    print(" 9 de Dezembro de 1991 -> Sonda 2 XV-55 -> Aguas Belas Ionosfera -> 88 km")
    print(" ")
    print(" 1 de Junho de 1992 -> Sonda 3 XV-24 -> Aeronomy -> 282 km")
    print(" ")
    print(" 31 de Outubro de 1993 -> Sonda 2 XV-56 -> Ponta de Areia Ionosfera -> 32 km")
    print(" ")
    print(" 22 de Marco de 1993 -> Sonda 2 XV-57 -> Maruda Ionosfera -> 102 km")
    print(" ")
    print(" 2 de Abril de 1994 -> VS-40 PT-01 -> MALTED/CADRE Ionosfera -> 950 km")
    print(" ")
    print(" 19 de Agosto de 1995 -> Sonda 2 XV-53 -> Ionosfera -> 140 km")
    print(" ")
    print(" 20 de Agosto de 1995 -> Nike Orion -> Operacao San Marcos -> 250 km")
    print(" ")
    print(" 24 de Agosto de 1996 -> Nike Orino -> Lencois Maranhenses -> 270 km")
    print(" ")
    print(" 25 de Agosto de 1997 -> Nike Orion -> Baronesa -> Falha 250 km")
    print(" ")
    print(" 9 de Setembro de 1997 -> Black Brant -> Piraperna Ionosfera -> Destruido durante o lancamento")
    print(" ")
    print(" 21 de Setembro de 1997 -> Nike Tomahawk -> Cuma -> 315 km")
    print(" ")
    print(" 23 de Setembro de 1998 -> VS-40 -> Iguaiba -> 259 km")
    print(" ")
    print(" 1 de Novembro de 1998 -> VS-30/Orion -> Aeronomy -> 282 km")
    print(" ")
    print(" 31 de Dezembro de 1998 -> Orion -> Ponta de Areia Ionosfera -> 80 km")
    print(" ")
    print(" 22 de Marco de 1999 -> Sonda 8 XV-60 -> Maruda Ionosfera -> 102 km")
    print(" ")
    print(" 27 de Abril de 1999 -> VS-55 PT-01 -> MALTED/CADRE Ionosfera -> 670 km")
    print(" ")
    print(" 19 de Agosto de 2000 -> Sonda 2 XV-53 -> Ionosfera -> 140 km")
    print(" ")
    print(" 20 de Janeiro de 2001 -> SACI-2 -> Operacao San Marcos -> 245 km")
    print(" ")
    print(" 24 de Fevereiro de 2002 -> Maracati l -> Lencois Maranhenses -> 270 km")
    print(" ")
    print(" ")
    print(" ")
    print(" ")
    print("Para sair pressione o botao verde")
    while not GPIO.input(botao_verde):
        pass
    sleep(.4)
    menu_principal()

def informacoes():
    while GPIO.input(botao_amarelo):
        pass

    system('clear')
    print("Informacoes extras")
    print("Velocidade de lancamento: 117km/h ")
    print(" ")
    print(" ")
    print("Para sair pressione o botao amarelo")
    while not GPIO.input(botao_amarelo):
        pass
    sleep(.4)
    menu_principal()

if __name__ == "__main__":
    head()
    system('clear')
    menu_principal()
