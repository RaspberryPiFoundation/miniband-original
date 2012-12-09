# This code is copyright ...... under the GPL v2.
# This code is derived from scratch_gpio_handler by Simon Walters, which
# is derived from scratch_handler by Thomas Preston
# Version 0.1: It's kind of working.

from array import *
import threading
import socket
import time
import sys
import struct
import serial
import io
import datetime as dt

'''
from Tkinter import Tk
from tkSimpleDialog import askstring
root = Tk()
root.withdraw()
'''

PORT = 42001
DEFAULT_HOST = '127.0.0.1'
BUFFER_SIZE = 240 #used to be 100
SOCKET_TIMEOUT = 1
DRUM_DEVICE = '/dev/ttyACM0'
GUITAR_DEVICE = '/dev/ttyUSB1'
MARACAS_DEVICE = '/dev/ttyACM1'
ARDUINO_BAUD_RATE = 57600

DRUM_INSTRUMENT_NAMES = {0: 'cymbal',
    1: 'hihat',
    2: 'slowdrum',
    3: 'snare',
    4: 'tomtom'}

DRUM_VALUE_NAMES = {0: 'drum-volume',
    1: 'drum-volume',
    2: 'drum-volume',
    3: 'drum-volume',
    4: 'drum-volume'}

GUITAR_INSTRUMENT_NAMES = {0: 'guitar'}
GUITAR_VALUE_NAMES = {0: 'guitar_pitch'}

GUITAR_INSTRUMENT_NAMES = {0: 'guitar'}
GUITAR_VALUE_NAMES = {0: 'guitar_pitch'}

MARACAS_INSTRUMENT_NAMES = {0: 'maracas', 2: 'maracas'}
MARACAS_VALUE_NAMES = {0: 'maracas_vigour', 2: 'maracas_vigour'}


class MyError(Exception):
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return repr(self.value)

class ScratchSender(threading.Thread):
    def __init__(self, socket):
        threading.Thread.__init__(self)
        self.scratch_socket = socket
        self._stop = threading.Event()


    def stop(self):
        self._stop.set()

    def stopped(self):
        return self._stop.isSet()

    def run(self):
        # Detect sensors here
        
        while not self.stopped():
            time.sleep(0.01) # be kind to cpu - not certain why :)

    def send_scratch_command(self, cmd):
        n = len(cmd)
        a = array('c')
        a.append(chr((n >> 24) & 0xFF))
        a.append(chr((n >> 16) & 0xFF))
        a.append(chr((n >>  8) & 0xFF))
        a.append(chr(n & 0xFF))
        self.scratch_socket.send(a.tostring() + cmd)


class ArduinoListener(threading.Thread):
    def __init__(self, device, speed, sender, instruments, values):
        threading.Thread.__init__(self)
        self.arduino_device = serial.Serial(device, speed)
        self._stop = threading.Event()
        self.scratch_sender = sender
        self.instruments = instruments
        self.values = values  

    def stop(self):
        self._stop.set()

    def stopped(self):
        return self._stop.isSet()

    def run(self):
        self.arduino_device.readline() # discard the first (partial) line
        while not self.stopped():
            try:
                pin_string, pin_value_string = self.arduino_device.readline().rstrip().split(',', 1)
                pin = int(pin_string)
                pin_value = int(pin_value_string)
                print dt.datetime.now(), 'Pin: %d, Value: %d' % (pin, pin_value)
                try:
                    print "sensor-update %s %d" % (self.values[pin], (pin_value * 100) / 1024)
                    self.scratch_sender.send_scratch_command("sensor-update %s %d" % (self.values[pin], (pin_value * 100) / 1024))
                except KeyError:
                    # Do nothing
                    pass
                try:
                    print "broadcast %s" % self.instruments[pin]
                    self.scratch_sender.send_scratch_command('broadcast %s' % self.instruments[pin])
                except KeyError:
                    # Do nothing
                    pass

            except serial.SerialException:
                print 'Serial exception'



def create_socket(host, port):
    while True:
        try:
            print 'Trying'
            scratch_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            scratch_sock.connect((host, port))
            break
        except socket.error:
            print "There was an error connecting to Scratch!"
            print "I couldn't find a Mesh session at host: %s, port: %s" % (host, port) 
            time.sleep(3)
            #sys.exit(1)

    return scratch_sock

def cleanup_threads(threads):
    for thread in threads:
        thread.stop()

    for thread in threads:
        thread.join()

if __name__ == '__main__':
    if len(sys.argv) > 1:
        host = sys.argv[1]
    else:
        host = DEFAULT_HOST


cycle_trace = 'start'
while True:
    if (cycle_trace == 'disconnected'):
        print "Scratch disconnected"
        cleanup_threads((listener, sender))
        time.sleep(1)
        cycle_trace = 'start'

    if (cycle_trace == 'start'):
        # open the socket
        print 'Starting to connect...' ,
        the_socket = create_socket(host, PORT)
        print 'Connected!'
        the_socket.settimeout(SOCKET_TIMEOUT)
##        data = the_socket.recv(BUFFER_SIZE)
##        print "Discard 1st data buffer" , data[4:].lower()
        sender = ScratchSender(the_socket)
        drum_listener = ArduinoListener(DRUM_DEVICE, ARDUINO_BAUD_RATE, sender, DRUM_INSTRUMENT_NAMES, DRUM_VALUE_NAMES)
        guitar_listener = ArduinoListener(GUITAR_DEVICE, ARDUINO_BAUD_RATE, sender, GUITAR_INSTRUMENT_NAMES, GUITAR_VALUE_NAMES)
        maracas_listener = ArduinoListener(MARACAS_DEVICE, ARDUINO_BAUD_RATE, sender, MARACAS_INSTRUMENT_NAMES, MARACAS_VALUE_NAMES)
        cycle_trace = 'running'
        print "Running...."
	sender.start()
        drum_listener.start()
        guitar_listener.start()
        maracas_listener.start()

        #pin = 1
        #pin_value = 512
        #print 'Sending:' "sensor-update %s %d" % (VOLUME_NAMES[pin], (pin_value * 100) / 1024)
        #sender.send_scratch_command("sensor-update %s %d" % (VOLUME_NAMES[pin], (pin_value * 100) / 1024))
        #print 'Sending:' 'broadcast %s' % INSTRUMENT_NAMES[pin]
        #sender.send_scratch_command('broadcast %s' % INSTRUMENT_NAMES[pin])

        #sender.send_scratch_command("sensor-update guitar-pitch 10")
	#sender.send_scratch_command("broadcast cymbal")
	#time.sleep(1)
	#sender.send_scratch_command("broadcast snare")
	#time.sleep(1)
        #sender.send_scratch_command("broadcast hihat")
	#time.sleep(1)
        #sender.send_scratch_command("broadcast slowdrum")
	#time.sleep(1)
        #sender.send_scratch_command("broadcast tomtom")
	#time.sleep(1)

    # wait for ctrl+c
    try:
        #just pause
        
#        else:
            time.sleep(0.1)
    except KeyboardInterrupt:
        cleanup_threads((sender, drum_listener, guitar_listener, maracas_listener))
        sys.exit()

