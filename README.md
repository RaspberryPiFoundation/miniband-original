# Code Club - Mini Band Project

<img src="http://farm9.staticflickr.com/8338/8256708023_4a941566e9.jpg" width="500" height="375" alt="photo (2)">

Make your own mini band! 
You and your friends can form your own finger-sized band and rock out using Raspberry Pi and Arduino. 
Learn how to build circuits with sensors and outputs and write a simple programme to control your instruments.

## You will make:

* A guitar
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
* Electrical tape
* Plastic drinking straw
* Pencil
* Coloured pens (optional)


## Software requirements:

* Scratch
* IDE developer environment for Arduino
* Py Serial library


## Useful links:

* [Pictures](http://bit.ly/codeclubminiband) 
* [Ardunio code](https://github.com/KatJoyWhite/miniband/tree/master/arduino)



## Pull-down Resistors

You’ll find your analogue inputs receive signal when you don’t expect them to.
This is because there’s electricty floating around in the system, or something like that.

To fix this, you need to wire each input to ground, through a 10KΩ resistor.

A better explanation can be found [here](http://arduino.cc/en/Tutorial/DigitalPins).



## Drum Kit

<img src="http://farm9.staticflickr.com/8074/8257699966_7585ca06e7.jpg" width="375" height="500" alt="Code Club Miniband"><

### 1. Make your drums

Take your 4 piezo buzzers and attach a ring of Sugru (or other modelling material) as shown in the picture. 
This will increase the flexibility and resonance of the sensors. Let the sugru set.

<img src="http://farm9.staticflickr.com/8353/8256628815_6c3872d3ac.jpg" width="500" height="375" alt="Code Club Miniband">


### 2. Connect the circuit

Piezo buzzers generate a small charges when you tap them, so they don’t need a power source.
Connect one lead from your buzzer to one of your analogue inputs, and connect the other lead to ground.
Repeat for each of your drums. It is easiest to use a bread board for making your circuit. 
Look at the picture for an example.

<img src="http://farm9.staticflickr.com/8081/8256628955_f65a76b6fb.jpg" width="500" height="375" alt="Code Club Miniband">

### 3. Program the Arduino

Find the appropriate code from the respository and upload to your Ardunio board.


### 4. Set up in Scratch 

Find four different drum sounds (or whatever sounds you'd like your drums to make!). Upload the sounds to Scratch.


## Guitar

<img src="http://farm9.staticflickr.com/8070/8257698984_8471e4cf57.jpg" width="500" height="375" alt="Code Club Miniband">

### 1. Make your guitar

Grab your strip potentiomater, a piece of thin card, and a pencil. 
Lightly draw round your potentiometer on the card and then use this as a guide to draw out your guitar shape. 
(The potentiomater will be the fret board of your guitar).
Cut out and colour in the guitar and stick down the potentiomater.
Tape a pencil or stick to the back of the guitar to make it stiffen the fret board. 

### 2. Connect the circuit

The potentiomater strip adjusts resistance, so you will need to feed it some electricity.
Run +5V into one of the strip’s outer pins, and ground into the other outer pin.
It doesn’t matter which way around you connect these, but it will affect which the direction
the fretboard runs (high and the top, low at the bottom or vice-versa).

Signal will come from the centre pin, so connect that to one of your analogue inputs and you should be good to go.

<img src="http://farm9.staticflickr.com/8363/8257699194_a2645e0e06.jpg" width="500" height="375" alt="Code Club Miniband">

### 3. Program the Arduino

Find the appropriate code from the respository and upload to your Ardunio board.


### 4. Set up in Scratch

Find five different guitar sounds and upload to Scratch.


## Maracas

<img src="http://farm9.staticflickr.com/8346/8257698652_4a99ee24b4.jpg" width="500" height="375" alt="Code Club Miniband">

### 1. Make your maracas

Cut 2 short lengths of drinking straw for your maraca handles. 
Using Sugru (or other modelling material), make 2 maraca heads by rolling it up into balls.
Push the maraca heads onto the straws and mold into a maraca shape.
Connect lengths of wire to the connectors of the 2 tilt sensors and then push each sensor into a straw until it presses into the Sugru.
Leave the Sugru to set.

<img src="http://farm9.staticflickr.com/8222/8256627511_118192e52f.jpg" width="500" height="375" alt="Code Club Miniband">

### 2. Connect the circuit

Connect the +5V port on the Arduino board to one of the pins on the tilt switch (it doesn't matter which way round).
Connect the other pin to an empty digital input on the board. 

<img src="http://farm9.staticflickr.com/8348/8257698572_4157db0b20.jpg" width="500" height="375" alt="Code Club Miniband">

### 3. Program the Arduino

Find the appropriate code from the respository and upload to your Ardunio board.


### 4. Set up in Scratch

Find a maraca / shaker sound and upload to Scratch.


## Connecting to the Raspberry Pi

Set up your Raspberry Pi with a power supply and monitor. 
Connect all your Ardunio boards (it's easiest to have one per instrument!) to the Raspberry Pi using USB. 
You will probably need a USB hub.


## Python glueware

Download the music-maker-hander.py file from the repository. Run it with
 python music-maker-handler.py
This program sets up a listener for each instrument. When it detects that an instrument has been played, it sends a couple of signals to Scratch.
The first signal appears in Scratch as a sensor value and is the volume (for drums), pitch (for the guitar), or ignored (for the maracas).
The second signal is a broadcast message that makes Scratch play the sound in the instrument.


## Scratch front end

The Scratch file, music-maker, makes the sounds. It responds to the signals from the Python handler above by playing the appropriate sounds. It also does some visual feedback for the insturments. 

