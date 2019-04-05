int botao_cima = 1;
int botao_direita = 2;
int botao_baixo = 3;
int botao_esquerda = 4;
int cima = 0;
int direita = 0;
int baixo = 0;
int esquerda = 0;
int sequencia = 0;

void setup() {
  // put your setup code here, to run once:
  pinMode(botao_cima, INPUT);
  pinMode(botao_direita, INPUT);
  pinMode(botao_baixo, INPUT);
  pinMode(botao_esquerda, INPUT);
  Serial.begin(9600);
}

void loop() {

    if(sequencia < 4){
    cima = digitalRead(botao_cima);
    direita = digitalRead(botao_direita);
    baixo = digitalRead(botao_baixo);
    esquerda = digitalRead(botao_esquerda);
  
    if(cima || direita || baixo || esquerda){
      delay(200);
      cima = digitalRead(botao_cima);
      direita = digitalRead(botao_direita);
      baixo = digitalRead(botao_baixo);
      esquerda = digitalRead(botao_esquerda);
  
      if(sequencia == 0){
        if(cima == 1 && direita != 1 && esquerda != 1){
          sequencia = 1;
          Serial.println("Primeiro botao correto");
        }else{
          Serial.println("Ja errou no primeiro?");
          }
      }
      else if(sequencia == 1){
            if(direita == 1 && cima != 1 && baixo != 1){
              sequencia = 2;
              Serial.println("E num é que tu ta mandando bem?")
            }else{
              sequencia = 0;
              Serial.println("Naaaaao, errou");
              }
      }
      else if(sequencia == 2){
            if(baixo == 1 && direita != 1 && esquerda != 1){
              sequencia = 3;
              Serial.println("Ta chegando lá");
            }else{
              sequencia = 0;
              Serial.println("Passou loooonge");
            }
      }
      else if(sequencia == 3){
            if(esquerda == 1 && cima != 1 && baixo != 1){
              sequencia = 4
              Serial.println("É isso meu bom!");
            }else{
              sequencia = 0;
              Serial.println("No ultimo cara!?!? Que bad");
              }
        }
    // put your main code here, to run repeatedly:
    }
  }
}
