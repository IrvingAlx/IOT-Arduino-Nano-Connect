#include<SoftwareSerial.h>    
SoftwareSerial ARD_305(2, 3); 
int led = 9;                  

void setup() {
  Serial.begin(9600);           //inicialización del monitor serie
  ARD_305.begin(9600);          //inicialización del módulo bluetooth
  pinMode(led, OUTPUT);         //definir "led" como salida
}
void loop() {
  if (ARD_305.available() > 0) {      //si hay un caracter se guarda en la variabe "dato"
    char lectura = ARD_305.read();    //la variable "lectura" guarda el caracter 
    if (lectura == 'p')   {           //si el caracter es 'p' entonces:
      digitalWrite(led, HIGH);        //se enciende el LED y
      Serial.println("led prendido");   //se muestra en el monitor serie la frase indicada
    }
    if (lectura == 'a') {             //si el caracter es 'a' entonces:
      digitalWrite(led, LOW);         //se apaga el LED y
      Serial.println("led apagado");  //se muestra en el monitor serie la frase indicada
    }
  }
}
