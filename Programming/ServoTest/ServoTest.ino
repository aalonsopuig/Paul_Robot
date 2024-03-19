// Servo Test 1.0
// Move servo to position indicated via serial

#include <Servo.h>

Servo myservo;         // Define index servo

int pos = 90;    // variable to store the servo position 
char num[4];     // número enviado desde PC

void setup() { 
  myservo.attach(3);  // Set index servo to digital pin 3
  myservo.write(pos);
  Serial.begin(9600);
  Serial.println("Insert servo position in degrees between 0 and 180");

} 

void loop() {            // Loop through motion test  

  if (Serial.available()>0) {
    Serial.readBytes(num,3);
    Serial.print("Pos:");
    //Serial.println(num);
    pos=atoi (num);
    pos=constrain(pos,0,180);
    Serial.println(pos);
    num[0]=0;
    num[1]=0;
    num[2]=0;
    myservo.write(pos);
}
}

// Motion routines for handopen,handrest, handclose, grab...

/*
void handopen() {
  servoindex.write(10);
  
}

void handrest() {
  
  servoindex.write(45);
}


void handclose() {
  servoindex.write(90);
}


void grab() { 
  for(pos = 10; pos < 90; pos+=2)    // goes from 0 degrees to 180 degrees 
  {                                
  servoindex.write(pos);             // tell servo to go to position in variable 'pos'
    delay(50);                       // waits 15ms for the servo to reach the position 
  }
  for(pos =90; pos>=10; pos-=1)      // goes from 180 degrees to 0 degrees 
  {                                
    servoindex.write(pos);           // tell servo to go to position in variable 'pos' 
    delay(25);                        // waits 5ms for the servo to reach the position 
  } 
                                
 } 
   
 */
  



  
