import RPi.GPIO as GPIO
from time import sleep
import math

class motor_ctrl:
    def __init__(self):
        self.in1 = 24
        self.in2 = 23
        self.en = 25
        self.temp1=1
        self.speed=0
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(self.in1,GPIO.OUT)
        GPIO.setup(self.in2,GPIO.OUT)
        GPIO.setup(self.en,GPIO.OUT)
        GPIO.output(self.in1,GPIO.LOW)
        GPIO.output(self.in2,GPIO.LOW)
        self.p=GPIO.PWM(self.en,1000)
        self.p.start(25)
        print("\n")
        print("The default speed & direction of motor is LOW & Forward.....")
        print("r-run s-stop f-forward b-backward l-low m-medium h-high e-exit")
        print("\n")
        
        self.vt = 0
    def controller(self,x):
        if x ==0:
            self.speed = self.vt - 10
            self.p.ChangeDutyCycle(math.abs(self.speed))
            GPIO.output(self.in1,GPIO.LOW)
            GPIO.output(self.in2,GPIO.HIGH)
            
            print("backward")
        elif x==1:
            self.speed = self.vt -5
            
            self.p.ChangeDutyCycle(math.abs(self.speed))
            GPIO.output(self.in1,GPIO.LOW)
            GPIO.output(self.in2,GPIO.HIGH)
            print("backward")
        
        elif x==2:
            self.speed = self.vt -2
            self.p.ChangeDutyCycle(math.abs(self.speed))
            GPIO.output(self.in1,GPIO.LOW)
            GPIO.output(self.in2,GPIO.HIGH)
            print("backward")
        
        elif x==3:
            self.speed =self.vt -1
            self.p.ChangeDutyCycle(math.abs(self.speed))
            GPIO.output(self.in1,GPIO.LOW)
            GPIO.output(self.in2,GPIO.HIGH)
            print("backward")
        
        elif x==4:
            self.speed = self.vt
            self.p.ChangeDutyCycle(math.abs(self.speed))
            GPIO.output(self.in1,GPIO.LOW)
            GPIO.output(self.in2,GPIO.LOW)
            print("Still")
        
        elif x==5:
            self.speed = self.vt +1
            self.p.ChangeDutyCycle(math.abs(self.speed))
            GPIO.output(self.in1,GPIO.HIGH)
            GPIO.output(self.in2,GPIO.LOW)
            print("forward")
        
        elif x==6:
            self.speed = self.vt+2
            self.p.ChangeDutyCycle(math.abs(self.speed))
            GPIO.output(self.in1,GPIO.HIGH)
            GPIO.output(self.in2,GPIO.LOW)
            print("forward")
        
        elif x==7:
            self.speed = self.vt +5
            self.p.ChangeDutyCycle(math.abs(self.speed))
            GPIO.output(self.in1,GPIO.HIGH)
            GPIO.output(self.in2,GPIO.LOW)
            print("forward")
        
        else :
            self.speed = self.vt +10
            self.p.ChangeDutyCycle(math.abs(self.speed))
            GPIO.output(self.in1,GPIO.HIGH)
            GPIO.output(self.in2,GPIO.LOW)
            print("forward")
        
        #GPIO.output(self.in1,GPIO.LOW)
        #GPIO.output(self.in2,GPIO.LOW)
        self.vt = self.speed
        print (speed)
        return speed
