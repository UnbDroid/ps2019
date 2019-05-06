# ps2019
Git utilizado para centralizar códigos e o que mais for desenvolvido para o Processo Seletivo de 2019 da Equipe Droid em conjunto com a ESC

# Sobre o desenvolvimento:
Para a sala onde seria realizada a dinâmica da Droid foram previstas a criação de 4 estações eletrônicas onde são permitidas interações dos jogadores, as estações desenvolvidas foram nomeadas como "Hacker", "Comunicação", "Controle" e "Cronômetro":

## Estação "Hacker":
### Função:
Conta com uma interface simples que após ser destravada permite aos jogadores navegarem pelo suposto sistema de dados da base e adquirir diversas informações.

### Hardware:
8 botões, 1 LED, 1 monitor e 1 raspberry.

### Como funciona:
O raspberry é o cérebro de toda a sala, ele gera um servidor de comunicação TCP/IP que permite a comunicação entre todas as estações, o código dentro da pasta "Hacker" chamado "geral.sh" cuida da inicialização dessa estação. Este código é um script simples que inicializa em background o código em python que gerencia o servidor e em foreground o código "main.py", que cuida da sequência dos 8 botões, caso a sequência correta seja inserida o código será finalizado e será iniciado o código "menu_hacker.py", que gerencia o menu de navegação com informações da base de lançamento.

### Como rodar:
Após configurar o Raspberry para gerar uma rede, seguindo o tutorial em https://www.raspberrypi.org/documentation/configuration/wireless/access-point.md, e lembrando de inicializar o serviço hostapd na inicialização do raspberry, basta enviar os códigos da pasta "Hacker" para o raspberry e na pasta dos códigos rodar o comando "./geral.sh", caso o arquivo não seja executável, rodar "chmod +x geral.sh".

## Estação "Comunicação":
