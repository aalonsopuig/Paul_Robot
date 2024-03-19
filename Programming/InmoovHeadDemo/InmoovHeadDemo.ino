// InmoovHeadDemo 1.0
// Perform a demomovement of the head

#include <Servo.h>

#define POSMIN 0
#define POSRES 1
#define POSMAX 2

Servo ServoHeadPan, ServoHeadTilt, ServoEyesPan, ServoEyesTilt, ServoJaw;     

//Limits of movements por servos (in degrees)
byte LimitServoHeadPan[]={30,90,150};
byte LimitServoHeadTilt[]={32,100,175};
byte LimitServoEyesPan[]={60,80,100};
byte LimitServoEyesTilt[]={50,90,100};
byte LimitServoJaw[]={10,10,25};

//Actual positions
byte  PosServoHeadPan=LimitServoHeadPan[POSRES], 
      PosServoHeadTilt=LimitServoHeadTilt[POSRES], 
      PosServoEyesPan=LimitServoEyesPan[POSRES], 
      PosServoEyesTilt=LimitServoEyesTilt[POSRES], 
      PosServoJaw=LimitServoJaw[POSRES];
      
char num[4];     // número enviado desde PC

byte MoveDelay=20; //Delay of movement

void setup() { 
  //Attach servos to pins
  ServoHeadTilt.attach(12);  // Set index servo to digital pin
  ServoHeadPan.attach(13);  // Set index servo to digital pin
  ServoJaw.attach(26);  // Set index servo to digital pin
  ServoEyesPan.attach(22);  // Set index servo to digital pin
  ServoEyesTilt.attach(24);  // Set index servo to digital pin

//  Serial.begin(9600);
//  Serial.println("Insert servo position in degrees between 0 and 180");

  //Set servos to rest position
  ServoHeadPan.write(PosServoHeadPan);
  ServoHeadTilt.write(PosServoHeadTilt);
  ServoEyesPan.write(PosServoEyesPan);
  ServoEyesTilt.write(PosServoEyesTilt);
  ServoJaw.write(PosServoJaw);
} 

void loop() {            // Loop through motion test  

  //HeadPan
  for (PosServoHeadPan=LimitServoHeadPan[POSRES]; PosServoHeadPan<LimitServoHeadPan[POSMAX]; PosServoHeadPan++)
  {
    ServoHeadPan.write(PosServoHeadPan);
    delay(MoveDelay);
  }
  delay(1000);
  for (PosServoHeadPan=LimitServoHeadPan[POSMAX]; PosServoHeadPan>LimitServoHeadPan[POSMIN]; PosServoHeadPan--)
  {
    ServoHeadPan.write(PosServoHeadPan);
    delay(MoveDelay);
  }
  delay(1000);
  for (PosServoHeadPan=LimitServoHeadPan[POSMIN]; PosServoHeadPan<LimitServoHeadPan[POSRES]; PosServoHeadPan++)
  {
    ServoHeadPan.write(PosServoHeadPan);
    delay(MoveDelay);
  }

  //HeadTilt
  for (PosServoHeadTilt=LimitServoHeadTilt[POSRES]; PosServoHeadTilt<LimitServoHeadTilt[POSMAX]; PosServoHeadTilt++)
  {
    ServoHeadTilt.write(PosServoHeadTilt);
    delay(MoveDelay);
  }
  delay(1000);
  for (PosServoHeadTilt=LimitServoHeadTilt[POSMAX]; PosServoHeadTilt>LimitServoHeadTilt[POSMIN]; PosServoHeadTilt--)
  {
    ServoHeadTilt.write(PosServoHeadTilt);
    delay(MoveDelay);
  }
  delay(1000);
  for (PosServoHeadTilt=LimitServoHeadTilt[POSMIN]; PosServoHeadTilt<LimitServoHeadTilt[POSRES]; PosServoHeadTilt++)
  {
    ServoHeadTilt.write(PosServoHeadTilt);
    delay(MoveDelay);
  }

  //EyesPan
  for (PosServoEyesPan=LimitServoEyesPan[POSRES]; PosServoEyesPan<LimitServoEyesPan[POSMAX]; PosServoEyesPan++)
  {
    ServoEyesPan.write(PosServoEyesPan);
    delay(MoveDelay);
  }
  delay(1000);
  for (PosServoEyesPan=LimitServoEyesPan[POSMAX]; PosServoEyesPan>LimitServoEyesPan[POSMIN]; PosServoEyesPan--)
  {
    ServoEyesPan.write(PosServoEyesPan);
    delay(MoveDelay);
  }
  delay(1000);
  for (PosServoEyesPan=LimitServoEyesPan[POSMIN]; PosServoEyesPan<LimitServoEyesPan[POSRES]; PosServoEyesPan++)
  {
    ServoEyesPan.write(PosServoEyesPan);
    delay(MoveDelay);
  }

  //EyesTilt
  for (PosServoEyesTilt=LimitServoEyesTilt[POSRES]; PosServoEyesTilt<LimitServoEyesTilt[POSMAX]; PosServoEyesTilt++)
  {
    ServoEyesTilt.write(PosServoEyesTilt);
    delay(MoveDelay);
  }
  delay(1000);
  for (PosServoEyesTilt=LimitServoEyesTilt[POSMAX]; PosServoEyesTilt>LimitServoEyesTilt[POSMIN]; PosServoEyesTilt--)
  {
    ServoEyesTilt.write(PosServoEyesTilt);
    delay(MoveDelay);
  }
  delay(1000);
  for (PosServoEyesTilt=LimitServoEyesTilt[POSMIN]; PosServoEyesTilt<LimitServoEyesTilt[POSRES]; PosServoEyesTilt++)
  {
    ServoEyesTilt.write(PosServoEyesTilt);
    delay(MoveDelay);
  }

  //Jaw
  for (PosServoJaw=LimitServoJaw[POSRES]; PosServoJaw<LimitServoJaw[POSMAX]; PosServoJaw++)
  {
    ServoJaw.write(PosServoJaw);
    delay(MoveDelay);
  }
  for (PosServoJaw=LimitServoJaw[POSMAX]; PosServoJaw>LimitServoJaw[POSMIN]; PosServoJaw--)
  {
    ServoJaw.write(PosServoJaw);
    delay(MoveDelay);
  }
  for (PosServoJaw=LimitServoJaw[POSMIN]; PosServoJaw<LimitServoJaw[POSRES]; PosServoJaw++)
  {
    ServoJaw.write(PosServoJaw);
    delay(MoveDelay);
  }

/*  if (Serial.available()>0) {
    Serial.readBytes(num,3);
    Serial.print("Pos:");
    //Serial.println(num);
    pos=atoi (num);
    pos=constrain(pos,0,128);
    Serial.println(pos);
    num[0]=0;
    num[1]=0;
    num[2]=0;
    myservo.write(pos);
}
*/}

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
  



  
