# 5.8 GHz Biquad Antenna
## Purpose
The purpose of the TX antenna is to radiate electromagnetic waves into the air. When encountering an obstacle the waves reflect back with a lapse, then the other RX antenna will sense them, and the computer do the calculation​​s in here [README](/README.md), in order to know the distance between the antennas and the target.

## Calculating the legal parameters
Based on the Mexican Technical disposition IFT-017-2023, emitted by the IFT or "Instituto Federal de Telecomunicaciones", the maximum legal parameters are specified in [README](/README.md). I chose the central frequency of 5.8GHz because the range 5725 to 5875 MHz is an ISM band dedicated for the Industrial, Scientific and Medical usage; making it perfect for the operation of the radar. Also the CNAF or Cuadro Nacional de Atribución de Frecuencias, assigned this band to radiolocation, so has priority over other services.

| *Parameter*                        | *Limit*            | *What it means* |
| :--------------------------------: | :----------------: | :-------------: |
| Conducted power before the antenna | 1 W or +30dBm      | Is the power measured at the output of the power amplifier, before it reaches the antenna. |
| EIRP                               | 4 W or +36 dBm     | The power that a hypothetical isotropic antenna would have to radiate to produce the same power density as the actual system in the direction of maximum gain. |
| Spectral density                   | $≤ 200 mW/MHz$     | How much EIRP can be inside every MHz of bandwidth.  |
| Conducted spectral density         | $≤ 50 mW/MHz$      | The maximum spectral density conducted over every MHZ of signal, before the antenna. |
| Minimum bandwidth                  | 500 kHz            | The transmitted signal must work at least at this bandwidth”. |
| Reduction for gain                 | $G > 6 dBi$        | The conducted power must be reduced by 1 dB for every dB of gain above 6 dBi. |

## Specifications

Considering all those parameters, I have to design a 
