import RPi.GPIO as GPIO          
from time import sleep
import math

class motor_ctrl:
    def __init__(self):
        self.in1 = 26
        self.in2 = 19
        self.en = 21
#        self.temp1=1                                                                                                          
        #self.in3=13
        #self.in4=6   
        #self.en1=5
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
        self.dutyCycle=0
        self.vt = 0
    def controller(self,x):
        if x ==0:
            self.dutyCycle = abs(95)
            self.p.ChangeDutyCycle(abs(self.dutyCycle)%100)
            GPIO.output(self.in1,GPIO.LOW)
            GPIO.output(self.in2,GPIO.HIGH)
            print("backward")

        elif x==1:
            self.dutyCycle = abs(85)
            self.p.ChangeDutyCycle(abs(self.dutyCycle)%100)

            GPIO.output(self.in1,GPIO.LOW)
            GPIO.output(self.in2,GPIO.HIGH)
            print("backward")

        elif x==2:
            self.dutyCycle = abs(75)
            self.p.ChangeDutyCycle(abs(self.dutyCycle)%100)
            GPIO.output(self.in1,GPIO.LOW)
            GPIO.output(self.in2,GPIO.HIGH)
            print("backward")

                
        elif x==3:
            self.dutyCycle = abs(65)
            self.p.ChangeDutyCycle(abs(self.dutyCycle)%100)

            GPIO.output(self.in1,GPIO.LOW)
            GPIO.output(self.in2,GPIO.HIGH)
            print("backward")
               
        elif x==4:
            self.dutyCycle = abs(2)%100
            self.p.ChangeDutyCycle(abs(self.dutyCycle)%100)

            print("NO CHANEGE")
                
        elif x==5:

            self.dutyCycle = abs(65)
            self.p.ChangeDutyCycle(abs(self.dutyCycle)%100)

            GPIO.output(self.in1,GPIO.HIGH)
            GPIO.output(self.in2,GPIO.LOW)
            print("forward")
               
        elif x==6:
            self.dutyCycle = abs(75)
            self.p.ChangeDutyCycle(abs(self.dutyCycle)%100)


            GPIO.output(self.in1,GPIO.HIGH)
            GPIO.output(self.in2,GPIO.LOW)
            print("forward")
        
        elif x==7:
            self.dutyCycle = abs(85)
            self.p.ChangeDutyCycle(abs(self.dutyCycle)%100)


            GPIO.output(self.in1,GPIO.HIGH)
            GPIO.output(self.in2,GPIO.LOW)
            print("forward")

               
        else :
            self.dutyCycle = abs(95)
            self.p.ChangeDutyCycle(abs(self.dutyCycle)%100)


            GPIO.output(self.in1,GPIO.HIGH)
            GPIO.output(self.in2,GPIO.LOW)
            print("forward")

        self.vt = self.dutyCycle*0.314
        return self.vt # change it as velocity
    
        
        
