import RPi.GPIO as GPIO
 
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
        input_str = input("Enter a number from 0 to 255 ('q' to exit) >> ")
        if input_str == 'q':
            break
        elif input_str.isdigit() and int(input_str) <= levels:
            value = int(input_str)
            dec2dac(value)
        else:
            print("Enter a positive number in [0, 255]")
            continue
finally:
    GPIO.output(dac, GPIO.LOW)
    GPIO.cleanup(dac)
    print("Cleanup has completed")
