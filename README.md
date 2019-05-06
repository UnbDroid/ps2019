# ps2019
Git utilizado para centralizar códigos e o que mais for desenvolvido para o Processo Seletivo de 2019 da Equipe Droid em conjunto com a ESC

# Sobre o desenvolvimento:
Para a sala onde seria realizada a dinâmica da Droid foram previstas a criação de 4 estações eletrônicas onde são permitidas interações dos jogadores, as estações desenvolvidas foram nomeadas como "Hacker", "Comunicação", "Controle" e "Cronômetro". Para finalizar a sala é necessário também um computador denominado de "Main" que controla o início da sala e o envio de dicas.

## OBS: 
Todos os programas foram rodados e testados somente em sistema operacional do tipo GNU/Linux.

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
### Função:
Exibir na tela os vídeos de explicação e do lançamento com áudio, transmitindo também as dicas quando estas forem requisitadas.

### Hardware:
1 monitor, 2 saídas de áudio, 1 amplificador, 1 arduino e 1 computador.

### Como funciona:
O arduino é responsável por fazer a leitura do estado da luz de emergência e do botão de dicas e enviar esses dados ao computador. O computador roda o código de cliente para se conectar ao servidor gerado pelo raspberry e atualiza os vídeos e áudios passados no monitor e saídas de áudio.

### Como rodar:
Enviar ao arduino o código "com.ino" na pasta "Comunicação", garantindo que a luz de emergência esteja acesa, o arduino utiliza as duas portas de interrupção 2 e 3 para realizar a leitura do botão de dicas e do nível de tensão da lâmpada utilizando um regulador de tensão para converter o 12V de alimentação da lâmpada em 5V. No computador juntar em uma mesma pasta o código "esc_cliente_v2.py" e todos os vídeos e áudios relativos à esta estação, que são todos do link **INSERIR LINK** exceto o "chronos.mp4". Após centralizar tudo isso em uma mesma pasta rodar o comando "python2.7 esc_cliente_v2.py" nessa mesma pasta e selecionar a opção "2" quando requisitado no código. Após o surgimento do frame inicial do vídeo, centralizar manualmente a janela do vídeo de maneira ótima no monitor e aguardar o comando "start" do computador main.

## Estação "Controle":
### Função:
Exibir na tela os dados sobre angulação e velocidade de lançamento e verificar a corretude do lançamento final do foguete.

### Hardware:

### Como funciona:

### Como rodar:

## Estação "Cronômetro":
### Função:
Exibir na tela um vídeo com o crônometro da sala, 30 minutos em contagem regressiva.

### Hardware:
3 switches, 1 fonte de 12V, 1 luz rotacional laranja 12V, um botão de dicas, 1 sistema de acionamento com chave e botão, 1 monitor e 1 computador (Pode ser o mesmo que o computador da estação Controle).

### Como funciona:
O computador é conectado ao monitor e controla o vídeo do cronometro. Um sistema elétrico comanda a luz laranja com um sistema redundante com os 3 switches em paralelo, assim, enquanto pelo menos 1 switch estiver ligado a lâmpada funcionará. 

### Como rodar:
Colocar no computador o código "esc_cliente_v2.py" em uma mesma pasta com o vídeo "chronos.mp4" do link **INSERIR LINK** e utilizar o comando "python2.7 esc_cliente_v2.py" e selecionar a opção 4 quando requisitado (Para utilizar juntamente com outra estação inserir o número 4 no código de seleção). Posicionar a tela com o primeiro frame no centro do monitor e esperar o sinal de início do computador main.

## Computador "Main":
### Função:
Enviar o sinal de início da sala e monitorar o pedido de dicas e enviá-las quando requisitadas.

### Hardware:
1 computador.

### Como funciona:
Envia o sinal de "start" para todas as estações, iniciando a sala e detecta pedidos de dicas e transmite as dicas para a sala.

### Como rodar:
Em um computador pessoal fora da sala, mas ainda conectado à rede gerada pelo raspberry, rodar o código "esc_cliente_v2.py" com o comando "python2.7 esc_cliente_v2.py" e escolher a opção 6 quando requisitado. Após garantir que todas as estações estão prontas, simplesmente escrever "start" e apertar enter, enviando o sinal de início para as estações.
