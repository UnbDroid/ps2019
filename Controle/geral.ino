#include <Keypad.h>

/* Portas utilizadas */
#define pot A1 // Verificar porta do potenciometro
#define end_button 2 // Verificar porta do botao de fim
#define joystick_up A2
#define joystick_right A3
#define joystick_down A4
#define joystick_left A5
#define gaveta 10

/* Defines relacionados ao potenciometro */
#define POT_RIGHT 62
#define VEL_RIGHT_1 '1'
#define VEL_RIGHT_2 '1'
#define VEL_RIGHT_3 '7'

/* Defines relacionados ao joystick */
#define UP 1
#define RIGHT 1<<1
#define DOWN 1<<2
#define LEFT 1<<3
#define max_sequence 6

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
byte PinosqtdLinhas[qtdLinhas] = {9, 8, 7, 6}; //PINOS UTILIZADOS PELAS LINHAS
byte PinosqtdColunas[qtdColunas] = {5, 4, 3}; //PINOS UTILIZADOS PELAS COLUNAS

char tecla_pressionada; // Tecla retornada pelo teclado
char ultima_tecla = '0';
char penultima_tecla = '0';
char antepenultima_tecla = '0';

//INICIALIZAÇÃO DO TECLADO
Keypad meuteclado = Keypad( makeKeymap(matriz_teclas), PinosqtdLinhas, PinosqtdColunas, qtdLinhas, qtdColunas); 

/* Relacionados ao joystick */
int up = 0;
int right = 0;
int down = 0;
int left = 0;
int sequence = 0;
int last_result = 0;
int right_sequence[max_sequence] = {UP, UP, DOWN, DOWN, RIGHT, LEFT};
long int last_move_timestamp = 0;

/* Valores relacionados as leituras do potenciometro */
int valor = 0; // Valor de leitura do potenciometro
byte b_valor = 0; // Valor em byte para ser enviado

/* Valores para abertura da gaveta */
long int open_up = 0;

/* Valor de final da sala */
volatile bool the_end = false;
 
void setup(){
  Serial.begin(9600);
  pinMode(end_button, INPUT); // Seta o botao de final como input
  attachInterrupt(digitalPinToInterrupt(end_button), end_room, RISING); // Seta a ISR do botao de fim

  pinMode(joystick_up, INPUT);
  pinMode(joystick_down, INPUT);
  pinMode(joystick_left, INPUT);
  pinMode(joystick_right, INPUT);

  pinMode(gaveta, OUTPUT);
  digitalWrite(gaveta, LOW);
}
  
void loop(){
  /* Pega o valor do potenciometro */
  valor = analogRead(pot); 
  b_valor = (byte)map(valor,0,1023,45,135);  // 0 a 180 pois um foguete nao pode ser lançado mais do que isso

  tecla_pressionada = meuteclado.getKey(); //VERIFICA SE ALGUMA DAS TECLAS FOI PRESSIONADA
  if(tecla_pressionada){
    antepenultima_tecla = penultima_tecla;
    penultima_tecla = ultima_tecla;
    ultima_tecla = tecla_pressionada;
  }

  joystick_check();

  // Envia os dados seriais
  send_serial();
}

void send_serial(){
//  int b;
//  if(the_end){
//    while(1){
//      b = Serial.read();
//      if(b > 0){
//        Serial.write('e');
//        if(b_valor == POT_RIGHT && VEL_RIGHT_1 == antepenultima_tecla && VEL_RIGHT_2 == penultima_tecla && VEL_RIGHT_3 == ultima_tecla){
//          Serial.write('1');
//        }
//        else {
//          Serial.write('0');
//        }
//      }
//    }
//  }
//  else{
//    b = Serial.read();
//    if(b > 0){
//      Serial.write('p');
//      Serial.write(b_valor);
//      Serial.write('t');
//      Serial.write(antepenultima_tecla);
//      Serial.write(penultima_tecla);
//      Serial.write(ultima_tecla);
//    }
//  }
}

// Funcao de leitura do joystick
void joystick_check(){
  
  if(sequence == max_sequence){
    // Abrir gaveta
    if(open_up == 0){
      digitalWrite(gaveta, HIGH);
      open_up = millis();
    }
    if(millis()-open_up > 2000){
      digitalWrite(gaveta, LOW);
    }
    return;
  }
  
  up = digitalRead(joystick_up);
  right = digitalRead(joystick_right)<<1;
  down = digitalRead(joystick_down)<<2;
  left = digitalRead(joystick_left)<<3;

  int result = up | right | down | left;

  Serial.print("Resultado: ");
  Serial.println(result);
  Serial.print("Sequencia certa: ");
  Serial.println(right_sequence[sequence]);
  Serial.print("Valor sequencia: ");
  Serial.println(sequence);
  
  if(result && (last_result != result) && (millis()-last_move_timestamp > 200)){
    if(right_sequence[sequence] & result){
      sequence++;
    }
    else{
      sequence = 0;
    }
    last_move_timestamp = millis();
  }
  else{
    if(millis()-last_move_timestamp > 3000){
      sequence = 0;
      last_move_timestamp = millis();
    }
  }
  last_result = result;
}

// Funcao a ser chamada quando acham que terminaram a sala
void end_room(){
  // Envia o sinal de fim para o pc que vai modificar o video do projetor
  the_end = true;
}