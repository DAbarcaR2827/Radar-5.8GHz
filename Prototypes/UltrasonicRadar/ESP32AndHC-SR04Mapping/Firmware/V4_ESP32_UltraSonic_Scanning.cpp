#include <Arduino.h>
#include <NewPing.h>
#include <ESP32Servo.h>

// put function declarations here:

NewPing sonar(26, 27, 200);
NewPing sonar2(32, 33, 200);

float fDistance = 0;
float fDistance2 = 0;
float Sdistance = 0;
float speed = 0;

int AzAngle = 0;
int ElAngle = 0;
int Xstep = 1;
int Ystep = 5;

unsigned long Stopwatch = millis();
float Lapse;
unsigned long LastTime = 0;

Servo Azimut;
#define AzPin 18
Servo Elevation;
#define ElPin 19

void setup() {
// put your setup code here, to run once:
Azimut.attach(AzPin);
Elevation.attach(ElPin);
Serial.begin(9600);

Azimut.write(AzAngle);
Elevation.write(ElAngle);
Serial.println("Creating map.");
delay(1000);

}

void loop() {
  // put your main code here, to run repeatedly:
Stopwatch = millis();
delay(0);
 
AzAngle += Xstep;
if (AzAngle >= 180 or AzAngle <= 0) {
  Xstep = -Xstep; 
  ElAngle += Ystep;
  if (ElAngle >= 90 or ElAngle <= 0) {
  Ystep = -Ystep; 
  }
}
Azimut.write(AzAngle);
Elevation.write(ElAngle); 

fDistance = sonar.convert_cm(sonar.ping_median(3));
fDistance2 = sonar2.convert_cm(sonar2.ping_median(3));

Serial.print("Azimut:");
Serial.print(AzAngle);
Serial.print(" | Elevation:");
Serial.print(ElAngle);
Serial.print(" | distance:");
Serial.print(fDistance);
Serial.print(" | Second distance:");
Serial.println(fDistance2);


if (fDistance > 0) {
  Lapse = (Stopwatch - LastTime) / 1000.0;
  speed = (fDistance-Sdistance)/Lapse;
  LastTime = Stopwatch;
  Serial.print("Speed:");
  Serial.println(speed);   

if (speed > 0){
  Serial.println("The object is getting away");
 } else if (speed < 0) {
  Serial.println("The object is getting closer");
 }

}
Sdistance = fDistance;
}


