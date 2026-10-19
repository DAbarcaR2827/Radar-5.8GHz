# FMCW Radar-5.8GHz

## General Overview
Some months ago, a drone intruded into my house, not once, but twice. I was scared, so I decided to build a DIY radar to detect drones near my home. P.S. the drone belongs to a neighborhood kid, but the incident made me realize how easily we and our properties are exposed.

The main objective of this project is to develop a radar capable of detecting drones flying over a small neighborhood. There are many news articles that confirm that criminals use drones to spy people and plan their attacks. With this tool, small communities can be aware of the movements a drone can make, for example intruding into a property at night. Also, this system is cheaper than any commercial radar and completely legal. As a starting point I found a similar project by Jeong and Kim (2021): https://www.mdpi.com/2079-9292/10/22/2758#sec2-electronics-10-02758 Here I found an example of a working 5.83Ghz to 5.94GHz radar. 
For the antennas the idea to use biquads was born when I saw this man building a WiFi antenna: https://www.youtube.com/watch?v=6odNBrwRM1k. Researching I found Vivaldi antenna would be better for this project, because it offers: wider bandwidth, better range resolution and 50Ω impedance . Nevertheless, I chose the biquad because it is easier to manufacture at home. In a future version I may migrate to Vivaldi antennas.

## How it works



Here I specify The components I'll use and why I changed them:

|  **Type** | **H. Jeong & S. Kim**    | **My component**              | **Why?** |
|---------------|:----------------:|:-----------------------------:|----------|
| VCO           | HMC431LP4ETR     | HMC358MS8GE                   | Availability and +11 dBm, integrated buffer. |
| PA1           | GRF2505          | —                             | Both replaced by single PA module. |
| PA2           | HMC407MS8GE      | —                             | Both replaced by single PA module. |
| PA            | —                | 5.8 GHz High Power Linear Amp | 2W Simpler, higher power extends range. |
| LNA           | QPL9503TR7       | QPL9503TR7                    | Same and enough  NF < 1 dB. |
| Mixer         | HMC218BMS8GE     | HMC219BMS8GETR                | Similar version, 40 dB isolation, 9 dB loss. |
| OpAmp         | TLE2062          | NE5532                        | Cheaper, 10 MHz GBW, enough for 48 kHz IF. |
| Power divider | PD4859J5050S2HF  | SCN-2-65+                     | Lower loss 0.5 vs 0.7 dB |
| LO Buffer     | —                | GVA-84+                       | Compensates splitter loss, delivers +13 to +16 dBm to mixer LO port.|
| ADC           | Arduino UNO      | PCM1808 module                | Faster, 24-bit vs 10-bit. |
| Controller    | PC (MATLAB)      | ESP32 and PC (MATLAB)         | ESP32 generates Vtune and controls switches. MATLAB is for digital signal processing. |
| Antennas      | Cylindrical horn | Biquad 5.8 GHz                | Easier to manufacture and focuses quite well the beam. |
| SP4T switches | —                | HMC7992LP3DE                  | Virtual MIMO sequential switching. |




First, I want to familiarize myself with the data this kind of project produces, so I started with an Arduino and an HC-SR04 ultrasonic sensor. Then I upgraded to an ESP32 WROOM and two HC-SR04, I even designed adjustable holders in Onshape. You can download them [here](https://cad.onshape.com/documents/22946c2de2ff62ec9e7e200f/w/714695cbcaa43d84e1a6a8b8/e/0db63b6bb4a4450c1f2c9957?renderMode=0&uiState=6ad41a46276830b495d96b97)

## References
1. Jeong, H.; Kim, S. Educational Low-Cost C-Band FMCW Radar System Comprising Commercial Off-the-Shelf Components for Indoor Through-Wall Object Detection. Electronics 2021, 10, 2758. https://doi.org/10.3390/electronics10222758
2. Kreosan English. How to Get Free Internet Access. Boosting of Wi-Fi
   Signals. *YouTube*, 25 August 2015. https://www.youtube.com/watch?v=6odNBrwRM1k
