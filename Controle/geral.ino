#include <Keypad.h>

/* Portas utilizadas */
#define pot A3 // Verificar porta do potenciometro
#define end_button 2 // Verificar porta do botao de fim
#define joystick_up 3
#define joystick_down 4
#define joystick_left 5
#define joystick_right 6

/*
 * Relacionado com o Keyboard
 */
const byte qtdLinhas = 4; //QUANTIDADE DE LINHAS DO TECLADO
const byte qtdColunas = 3; //QUANTIDADE DE COLUNAS DO TECLADO
char matriz_teclas[qtdLinhas][qtdColunas] = {
  {'1','2','3'},
  {'4','5','6'},
  {'7','8','9'},
  {'*','0','#'}
};
byte PinosqtdLinhas[qtdLinhas] = {7, 8, 9, 10}; //PINOS UTILIZADOS PELAS LINHAS
byte PinosqtdColunas[qtdColunas] = {11, 12, 13}; //PINOS UTILIZADOS PELAS COLUNAS

char tecla_pressionada; // Tecla retornada pelo teclado

//INICIALIZAÇÃO DO TECLADO
Keypad meuteclado = Keypad( makeKeymap(matriz_teclas), PinosqtdLinhas, PinosqtdColunas, qtdLinhas, qtdColunas); 

/* Relacionados ao joystick */
int up = 0;
int right = 0;
int down = 0;
int left = 0;
int sequence = 0;

/* For joystick */
#define UP 1
#define RIGHT 1<<1
#define DOWN 1<<2
#define LEFT 1<<3
#define max_sequence 4
long int last_time = 0;
int right_sequence[max_sequence] = {UP, UP | RIGHT, DOWN, DOWN | LEFT};

int valor = 0; // Valor de leitura do potenciometro
byte b_valor = 0; // Valor em byte para ser enviado

int contador_mat = 0;
int contador_pot = 0;
int validacao = 1;

volatile bool estado = true;
char v[4]; 
 
void setup()
  pinMode(end_button, INPUT); // Seta o botao de final como input
  attachInterrupt(digitalPinToInterrupt(end_button), end_room, RISING); // Seta a ISR do botao de fim

  pinMode(joystick_up, INPUT);
  pinMode(joystick_down, INPUT);
  pinMode(joystick_left, INPUT);
  pinMode(joystick_right, INPUT);
}
  
void loop(){
  /* Pega o valor do potenciometro */
  valor = analogRead(pot); 
  b_valor = (byte)map(valor,0,1023,0,180);  // 0 a 180 pois um foguete nao pode ser lançado mais do que isso

  tecla_pressionada = meuteclado.getKey(); //VERIFICA SE ALGUMA DAS TECLAS FOI PRESSIONADA

  joystick_check();

  // Envia os dados seriais
  send_serial(b_valor, tecla_pressionada);
}

// Funcao de leitura do joystick
void joystick_check(){

  if(sequence == max_sequence){
    // Abrir gaveta
    return;
  }

  if(sequence > 0){
    if(millis()-last_time >= 7000){ // Maximo de 7 segundos entre mudancas de estados
      sequence = 0;
    }
    return;
  }
  
  up = digitalRead(joystick_up);
  right = digitalRead(joystick_right)<<1;
  down = digitalRead(joystick_down)<<2;
  left = digitalRead(joystick_left)<<3;

  if(up || right || down || left){
    if(right_sequence[sequence] == (up | right | down | left)){
      sequence++;
      last_time = millis();
    }
    else {
      if(sequenca > 0){
        if(!(right_sequence[sequence--] == (up | right | down | left) && millis - last_time < 400)){
          sequence = 0;
          last_time = millis();
        }
      }
    }
  
    last_time = millis();
  }
}

// Funcao a ser chamada quando acham que terminaram a sala
void end_room(){
  // Envia o sinal de fim para o pc que vai modificar o video do projetor
}

void collect_data(){
 static unsigned long tempo_ant;
 if(contador_mat <4){
    unsigned long tempo = millis();
    if(tempo - tempo_ant > 200) {
       v[contador_mat] = tecla_pressionada;
       Serial.print("Tecla pressionada : "); //IMPRIME O TEXTO NO MONITOR SERIAL
       Serial.print(tecla_pressionada); //IMPRIME NO MONITOR SERIAL A TECLA PRESSIONADA
       contador_mat++;
       if(contador_mat == 3) {
        if(v[0] == '1' && v[1] == '1' && v[2] == '7') {
          Serial.println("PARABENS");
          contador_mat++;
          }
        else {
          contador_mat = 0;
          }
       }
    }
    tempo_ant = tempo;
     
 }
}
