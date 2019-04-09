#define botao_dicas 2
#define chaves 3

volatile bool need_help = false;
bool noise = 0;

byte b;

void setup() {
  // put your setup code here, to run once:
  Serial.begin(9600);
  pinMode(botao_dicas, INPUT);
  pinMode(chaves, INPUT);

  attachInterrupt(digitalPinToInterrupt(botao_dicas), send_dicas, RISING);
}

void loop() {
  // put your main code here, to run repeatedly:
  noise = digitalRead(chaves);

  send_serial();
}

void send_serial(){
  b = Serial.read();
  if(b>0){
    Serial.write('d');
    if(need_help){
      Serial.write('1');
      need_help = false;
    }
    else {
      Serial.write('0');
    }
    Serial.write('s');
    if(noise){
      Serial.write('1');
    }
    else {
      Serial.write('0');
    }
  }
}

void send_dicas(){
  static unsigned long last_interrupt = 0;
  if(millis() - last_interrupt > 200){
    need_help = true;
  }
  last_interrupt = millis();
}
