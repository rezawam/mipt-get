import RPi.GPIO as GPIO
import time
 
dac = [26, 19, 13, 6, 5, 11, 9, 10]
bits = len(dac)
levels = 2**bits
maxVoltage = 3.3
 
def dec2bin(decimal):
    return [int(bit) for bit in bin(decimal)[2:].zfill(bits)]
 
def dec2dac(value):
    signal = dec2bin(value)
    GPIO.output(dac, signal)
 
GPIO.setmode(GPIO.BCM)
GPIO.setup(dac, GPIO.OUT, initial = GPIO.LOW)
 
try:
    while True:
        for i in range(0,256):
            dec2dac(i)
            time.sleep(0.005)
        for i in range(255, 1, -1):
            dec2dac(i)
            time.sleep(0.005)    
finally:
    GPIO.output(dac, GPIO.LOW)
    GPIO.cleanup(dac)
    print("\nCleanup has completed")
