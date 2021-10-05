import RPi.GPIO as GPIO
import time
 
dac = [26, 19, 13, 6, 5, 11, 9, 10]
bits = len(dac)
levels = 2**bits
maxVoltage = 3.3
troykaModule = 17
comparator  = 4
 
GPIO.setmode(GPIO.BCM)
GPIO.setup(dac, GPIO.OUT, initial = GPIO.LOW)
GPIO.setup(troykaModule, GPIO.OUT, initial=GPIO.HIGH)
GPIO.setup(comparator, GPIO.IN)

def dec2bin(decimal):
    return [int(bit) for bit in bin(decimal)[2:].zfill(bits)]
 
def dec2dac(value):
    signal = dec2bin(value)
    GPIO.output(dac, signal)
    return signal

def adc(): 
    for value in range(256):
        signal = dec2dac(value)
        time.sleep(0.0006)
        comparatorValue = GPIO.input(comparator)
        if comparatorValue == 0:
            return value
        else 
            return 256
 
try:
    while True:
        value = adc()
        if value is not None:
            #value = int(adc())
            print("Digital value: {:^3}, analog value: {:.2f} V".format(value, value * maxVoltage / levels))
except KeyboardInterrupt:
    print("\nThe program was stopped by keyboard")
finally:
    GPIO.output(dac, GPIO.LOW)
    GPIO.cleanup(dac)
    print("Cleanup has completed")