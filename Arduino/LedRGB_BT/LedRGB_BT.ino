#include<SoftwareSerial.h>    
SoftwareSerial ARD_305(2, 3);   //Rx, Tx

char dato;      
String comando;
char digito;    
String color;   
String brillo;  
int pwm[255];   

int R = 9;      
int G = 10;
int B = 11;


void setup() {
  Serial.begin(9600);                     
  ARD_305.begin(9600);
  pinMode(R, OUTPUT); analogWrite(R, 255);     
  pinMode(G, OUTPUT); analogWrite(G, 255);
  pinMode(B, OUTPUT); analogWrite(B, 255);
  for(int i = 0; i<=255; i++){                 
    pwm[i] = 255-i;
    }  
}

void loop() {
  leerPuertoSerie();            
  if(comando.length() > 0){     
    brillo = "";                
    color = comando.substring(0,1);     
    if(comando.length() > 3){           
        for(int i = 2; i<5; i++){       
          digito=comando.charAt(i);   
          if(isDigit(digito)){
          brillo+= digito; 
          }
        }
    }
    else{
      brillo+= comando.substring(2);    
      }
  
  int intensidad = brillo.toInt();      
  if(color == "r"){
    analogWrite(R, pwm[intensidad]);    
  }
    else if(color == "g"){
      analogWrite(G, pwm[intensidad]);
      }
      else if(color == "b"){
          analogWrite(B, pwm[intensidad]);
      }    
  }
}

void leerPuertoSerie() {                
  comando = "";                         
  while(ARD_305.available()){           
    delay(10);
    if (ARD_305.available() > 0){
      dato = ARD_305.read();
      comando += dato;                    
    }
  }
}
