import RPi.GPIO as GPIO
import time 
from gpiozero import LED
from time import sleep
GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)
ir = 3 
GPIO.setup(ir,GPIO.IN)
#GPIO.setup(LED,GPIO.OUT) 
yellow = LED(17)
red = LED(27)
green = LED(22)
y = 0 
r = 0
g = 0

while(True) :
    
    if(GPIO.input(ir) == 1) :
        #GPIO.output(LED,True)
        y = 2
        g = 10
        r = 8
    else:
        #GPIO.output(LED,False)
        y =0
        r = 20 
        g = 0
        
    yellow.on()
    print("Yellow") 
    sleep(y)
    yellow.off()
    #sleep(1) 
    red.on()
    print("Red")
    sleep(r)
    red.off()
    #sleep(10)
    green.on()
    print("Green")
    sleep(g)
    green.off()
    #sleep(4)
    
   
