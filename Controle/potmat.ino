#include <Keypad.h>
const byte qtdLinhas = 4; //QUANTIDADE DE LINHAS DO TECLADO
const byte qtdColunas = 3; //QUANTIDADE DE COLUNAS DO TECLADO

//CONSTRUÇÃO DA MATRIZ DE CARACTERES
char matriz_teclas[qtdLinhas][qtdColunas] = {
  {'1','2','3'},
  {'4','5','6'},
  {'7','8','9'},
  {'*','0','#'}
};

#define pot A15
#define botao 2
byte PinosqtdLinhas[qtdLinhas] = {3, 4, 5, 6}; //PINOS UTILIZADOS PELAS LINHAS
byte PinosqtdColunas[qtdColunas] = {8, 9, 10}; //PINOS UTILIZADOS PELAS COLUNAS
int contador_mat = 0;
int contador_pot = 0;
int validacao = 1;
int valor = 0;
volatile bool estado = true;
char v[4];
char tecla_pressionada;
 
//INICIALIZAÇÃO DO TECLADO
Keypad meuteclado = Keypad( makeKeymap(matriz_teclas), PinosqtdLinhas, PinosqtdColunas, qtdLinhas, qtdColunas); 
 
void setup(){

  pinMode(botao, INPUT);
  attachInterrupt(digitalPinToInterrupt(botao), collect_data, RISING);
  Serial.begin(9600); //INICIALIZA A SERIAL
  Serial.println("Aperte uma tecla..."); //IMPRIME O TEXTO NO MONITOR SERIAL
  Serial.println(); //QUEBRA UMA LINHA NO MONITOR SERIAL

  
}
  
void loop(){
  if(contador_pot <10){
    tecla_pressionada = meuteclado.getKey(); //VERIFICA SE ALGUMA DAS TECLAS FOI PRESSIONADA
    delay(500);
    valor = analogRead(pot); 
    valor = map(valor,0,1023,0,255);
    //analogWrite(porta, valor);
      Serial.println(valor);
    if(valor == 34) { 
      contador_pot++;
      if(contador_pot == 9){
        Serial.println("Parabens");
        contador_pot++;
      }
    }else{
      contador_pot = 0;    
    }
  }
}

void collect_data() {
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
