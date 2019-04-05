#define pot A15

int valor = 0;

void setup(){
}

void loop(){
  valor = analogRead(pot); 
  valor = map(valor,0,1023,0,255);
{
