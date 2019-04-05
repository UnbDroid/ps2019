#define botao 2

void setup(){
  pinMode(botao, INPUT);
  attachInterrupt(digitalPinToInterrupt(botao), collect_data, RISING); 
}

void loop(){
}

void collect_data() {
}
