#include <Arduino.h>
#include <NewPing.h>
#include <ESP32Servo.h>
// put function declarations here:

NewPing sonar(26, 27, 400);
NewPing sonar2(32, 33, 400);

float distance = 0;
float lapse = 0;
float fDistance = 0;
float fDistance2 = 0;

float Sdistance = 0;
float speed = 0;

int AzAngle = 0;
int ElAngle = 0;
int Xstep = 1;
int Ystep = 1;

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

delay(0);
 
AzAngle += Xstep;

if (AzAngle >= 180 || AzAngle <= 0) {
  Xstep = -Xstep; 
}
Azimut.write(AzAngle);

ElAngle += Ystep;

if (ElAngle >= 180 || ElAngle <= 0) {
  Ystep = -Ystep; 
}
Elevation.write(ElAngle); 

fDistance = sonar.convert_cm(sonar.ping_median(5));
fDistance2 = sonar2.convert_cm(sonar2.ping_median(5));

Serial.print("Azimut:");
Serial.print(AzAngle);
Serial.print(" | Elevation:");
Serial.print(ElAngle);
Serial.print(" | distance:");
Serial.print(fDistance);
Serial.print(" | Second distance:");
Serial.println(fDistance2);

if (fDistance > 0) {

 speed = (fDistance-Sdistance)/0.25;
 Serial.print("Speed:");
 Serial.println(speed);

 

if (speed > 0){
  Serial.println("The object is getting away");
 } else if (speed < 0) {
  Serial.println("The object is getting closer");
 }

 Sdistance = fDistance;
 }

}
