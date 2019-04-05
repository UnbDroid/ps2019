#define botao 2

void setup(){
  pinMode(botao, INPUT);
  attachInterrupt(digitalPinToInterrupt(botao), manda_dicas, RISING); 
}

void loop(){
}

void manda_dicas(){
}
