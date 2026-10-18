#include <Arduino.h>
#include <NewPing.h>
// put function declarations here:

NewPing sonar(10, 9, 999);

float distance = 0;
float lapse = 0;
float fDistance = 0;
float Sdistance = 0;
float speed = 0;

void setup() {
// put your setup code here, to run once:
Serial.begin(9600);
Serial.println("Measuring distance and speed");

}

void loop() {
// put your main code here, to run repeatedly:

delay(100);
  distance = sonar.ping_cm();
  lapse = sonar.ping();
  fDistance = sonar.convert_cm(sonar.ping_median(5));
Serial.print("Distance:");
Serial.println(distance);
Serial.println();
  speed = (distance-Sdistance)/0.1;
Serial.print("Speed");
Serial.print(speed);
if (speed > 0){
  Serial.print("The object is getting away");
} else if (speed < 0) {
  Serial.print("The object is getting closer");
}

  Sdistance = distance;
}
