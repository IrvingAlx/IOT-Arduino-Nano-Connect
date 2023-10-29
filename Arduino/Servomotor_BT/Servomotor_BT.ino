#include <SoftwareSerial.h> 
#include <Servo.h>          
SoftwareSerial bluetooth(9,10); 
Servo x;          
int grados=0;     

void setup()
{
  Serial.begin(9600);    
  bluetooth.begin(9600); 
  x.attach(11);    
}
void loop()
{
if (bluetooth.available()){    
  char Letra=bluetooth.read();  
  if (Letra =='i'){             
    grados=0;
    Serial.println("inicio lectura");   
  }
  else if (Letra == 'f'){       
    x.write(grados);            
    grados =0;
    Serial.println("° fin de lectura");    
  }
  if (Letra>= '0' && Letra<= '9'){  
    int Numero = int (Letra - '0'); 
    grados = grados *10 + Numero;
    Serial.print(" ");
    Serial.print(Numero);
  }
}
}
