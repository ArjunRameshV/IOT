import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)
ir = 3
LEDG=11
LEDY=7
LEDR=9
GPIO.setup(ir,GPIO.IN)
GPIO.setup(LEDY,GPIO.OUT)
GPIO.setup(LEDR,GPIO.OUT)
GPIO.setup(LEDG,GPIO.OUT)
while True :
    if(GPIO.input(ir) == 1) :
        GPIO.output(LEDG,True)
        time.sleep(10)
        GPIO.output(LEDG,False)
        GPIO.output(LEDY,True)
        time.sleep(2)
        GPIO.output(LEDY,False)
        GPIO.output(LEDR,True)
        time.sleep(8)
        GPIO.output(LEDR,False)
        print"obstacle found"
    else:
        GPIO.output(LEDG,True)
        time.sleep(4)
        GPIO.output(LEDG,False)
        GPIO.output(LEDY,True)
        time.sleep(1)
        GPIO.output(LEDY,False)
        GPIO.output(LEDR,True)
        time.sleep(15)
        GPIO.output(LEDR,False)
        print"no obstacle found"
    time.sleep(0.1) 
