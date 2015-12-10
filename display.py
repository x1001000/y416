import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
#GPIO.setup(7, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
segments = (10, 9, 11, 5, 6, 13, 19, 26)
for segment in segments:
    GPIO.setup(segment, GPIO.OUT)
    GPIO.output(segment, 0)
digits = (3, 4, 17, 27)
for digit in digits:
    GPIO.setup(digit, GPIO.OUT)
    GPIO.output(digit, 0)
num = {' ':(0,0,0,0,0,0,0),
    '0':(1,1,1,1,1,1,0),
    '1':(0,1,1,0,0,0,0),
    '2':(1,1,0,1,1,0,1),
    '3':(1,1,1,1,0,0,1),
    '4':(0,1,1,0,0,1,1),
    '5':(1,0,1,1,0,1,1),
    '6':(1,0,1,1,1,1,1),
    '7':(1,1,1,0,0,0,0),
    '8':(1,1,1,1,1,1,1),
    '9':(1,1,1,1,0,1,1)}
for n in range(10):
        i = 0
        for on_or_off in num[str(n)]:
            #print on_or_off
            #time.sleep(0.5)
            GPIO.output(segments[i], on_or_off)
            i+=1
        time.sleep(.3)
GPIO.cleanup()
