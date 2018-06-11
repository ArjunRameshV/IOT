#Final traffic raspberry code : #Basic traffic system model to analyse approach of an object 
import time                         
import RPi.GPIO as GPIO 
GPIO.setmode(GPIO.BOARD)            # Use board numbering pin 
GPIO.setwarnings(False)
#Red  --- R and g
#Yellow --- Y and 13
#Green --- G and y
#Ir ---- I and 12
r = 11
y = 15
g = 13
ir = 3
GPIO.setup(r,GPIO.OUT)
GPIO.setup(y,GPIO.OUT)
GPIO.setup(g,GPIO.OUT)
GPIO.setup(ir,GPIO.IN) 

# sleep time 

""" R = 0 
Y = 0 
G = 0 """ 


def traffic_1() :
    GPIO.output(g,True)
    print("ya")
    time.sleep(10)
    GPIO.output(g,False)
    GPIO.output(y,True)
    print("YO")
    time.sleep(2)
    GPIO.output(y,False)
    GPIO.output(r,True)
    print("Ha")
    time.sleep(8)
    GPIO.output(r,False)

def traffic_2() :
    GPIO.output(r,True)
    time.sleep(8)
    GPIO.output(r,False)
    GPIO.output(y,True)
    time.sleep(0)
    GPIO.output(y,False)
    GPIO.output(g,True)
    time.sleep(0) 
    GPIO.output(g,False)

while(True) :
    if(GPIO.input(ir) == True) :
        print("ob is there")
        traffic_1()
    else :
        print("ob is not there")
        traffic_2()
