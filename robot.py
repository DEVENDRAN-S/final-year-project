import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

GPIO.setup(12,GPIO.OUT)
GPIO.setup(16,GPIO.OUT)
GPIO.setup(13,GPIO.OUT)
GPIO.setup(21,GPIO.OUT)

GPIO.setwarnings(False)

def Front():
        GPIO.output(12,True)
        GPIO.output(16,False)
        GPIO.output(13,True)
        GPIO.output(21,False)
        #time.sleep(Delay)
        #GPIO.output(12,False)
        #GPIO.output(20,False)
def Back():
        GPIO.output(16,True)
        GPIO.output(12,False)
        GPIO.output(21,True)
        GPIO.output(13,False)
        #time.sleep(Delay)
        #GPIO.output(16,False)
        #GPIO.output(21,False)
def Right():
        GPIO.output(12,True)
        GPIO.output(16,False)
        GPIO.output(13,False)
        GPIO.output(21,False)
        time.sleep(5)
        GPIO.output(12,False)
        GPIO.output(21,False)
def Left():
        GPIO.output(12,False)
        GPIO.output(16,True)
        GPIO.output(13,True)
        GPIO.output(21,False)
        time.sleep(5)
        GPIO.output(16,False)
        GPIO.output(13,False)
def Stop():
        GPIO.output(12,False)
        GPIO.output(16,False)
        GPIO.output(13,False)
        GPIO.output(21,False)

#Front()
#Right()
#Left()
#Stop()

