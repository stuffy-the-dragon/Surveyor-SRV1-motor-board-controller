# srv1motordriver

A python class that controls the motor control board of the Surveyor SRV-1 tracked robot from a Raspberry Pi.

The SRV-1 motor control board has two DC motors connected and two laser diodes. This class can PWM control the motors and switch on the lasers.

The connected GPIO pins are currently hard coded, so feel free to update to suit your wiring.

Here is the board schematic:
https://web.archive.org/web/20120525180739/http://www.surveyor.com/blackfin/bfin-radiomotor-v3.png
