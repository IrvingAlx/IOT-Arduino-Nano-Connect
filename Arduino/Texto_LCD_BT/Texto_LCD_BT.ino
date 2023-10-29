#include <LiquidCrystal.h>                   
LiquidCrystal lcd(A0, A1, A2, A3, A4, A5);   
#include <SoftwareSerial.h>                  
SoftwareSerial BT(2, 3);                     
String TEXTO;                                

void setup() {
  BT.begin(9600);                            
}

void loop() {
  int i = 0;                                 
  char escritura[32];   
  if (BT.available()) {                      
    delay(100);
    while ( BT.available() && i < 16) {      
      escritura[i++] = BT.read();             
    }
    escritura[i++] = '\0';                   
  }
  if (i > 0)                              
    BT.println((char*)escritura);            
  lcd.print((char*)escritura);               
  delay(1000);
  lcd.clear();
}
