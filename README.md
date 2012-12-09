# Code Club - Mini Band Project

Make your own mini band! 
You and your friends can form your own finger-sized band and rock out using Raspberry Pi and Arduino. 
Learn how to build circuits with sensors and outputs and write a simple programme to control your instruments.

## You will make:

* A guitar
* A keyboard
* A set of drums
* A pair of maracas

## You will need:

* 1 x Raspberry Pi (plus monitor and power supply)
* USB hub
* 2 x Arduino Uno boards (with USB cables)
* 1 x strip potentiometer
* 2 x tilt sensors
* 4 x piezo buzzers (the type in greetings cards, easy to get from Maplin)
* 10K resistors
* Bread boards (1 per instrument)
* Card
* Sugru (or some other modelling material)


## Software requirements:

* Scratch
* IDE developer environment for Arduino
* Py Serial library

## Drum Kit

### 1. Make your drums

Take your 4 piezo buzzers and attach a ring of Sugru (or other modelling material) as shown in the picture. 
This will increase the flexibility and resonance of the sensors. Let the sugru set.


### 2. Make the circuit

Piezo buzzers generate a small charges when you tap them, so they don’t need a power source.
Connect one lead from your buzzer to one of your analogue inputs, and connect the other lead to ground.
Repeat for each of your drums. It is easiest to use a bread board for making your circuit. 
Look at the picture for an example.



## Pull-down Resistors

You’ll find your analogue inputs receive signal when you don’t expect them to.
This is because there’s electricty floating around in the system, or something like that.

To fix this, you need to wire each input to ground, through a 10KΩ resistor.

A better explanation can be found [here](http://arduino.cc/en/Tutorial/DigitalPins).
