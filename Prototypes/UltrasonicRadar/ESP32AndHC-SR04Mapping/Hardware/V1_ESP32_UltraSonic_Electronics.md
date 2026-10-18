# Ultrasonic Mapping Prototype — ESP32 Dual-Sensor System

## Objective
The main objective of this Prototype was to understand the pipeline and mechanical scanning logic before migrating to the 5.8 GHz FMCW radar. Also familiarize myself with the real-time data output by the sensors. 

## Hardware Setup

| ESP32 GPIO  | Component          | Function       | Purpose |
| :---------: | :----------------: | :------------: | :-----: |
| GPIO 26, 27 | HC-SR04 (Sensor 1) | Trigger / Echo | First sensor, forward-facing  |
| GPIO 32, 33 | HC-SR04 (Sensor 2) | Trigger / Echo | Second sensor, for dual-point mapping |
| GPIO 18     | Servo (Azimuth)    | PWM Control    | 180° horizontal scanning |
| GPIO 19     | Servo (Elevation)  | PWM Control    | 90° vertical scanning |

## Mechanical Setup

The servo-motors were mounted using hot glue and the sensors over their holder with adhesive tape for rapid iteration. Originally the servo-motor would be in a support, but it didn't have the correct spacing. 

This fragile setup had to improve:
- No more adhesive tape. It does not stick well to the metal. So I removed it.
- The measurements, the final design must have the precise measurements, especially for the Servo holder. So the piece has been redesigned.
- The final design must be rigid, centered, and easily adjustable. Therefore, I designed new pieces and implemented the use of screws.

## CAD Files & Prototype Photos
Prototype Photo:

3D Models Download:
[Ultra Sonic Sensor Holder](UltraSonicSensorHolder.stl)
[Servo-motor Holder](ServomotorHolder.stl)

