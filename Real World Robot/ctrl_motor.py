import RPi.GPIO as GPIO          
from time import sleep


class motor_ctrl:
    def __init__(self):
        self.in1 = 24
        self.in2 = 23
        self.en = 25
        self.temp1=1

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
            self.p.ChangeDutyCycle(10+ self.vt)
            GPIO.output(self.in1,GPIO.LOW)
            GPIO.output(self.in2,GPIO.HIGH)
            speed = self.vt + 10
            
            print("backward")
        elif x==1:
            self.p.ChangeDutyCycle(5+ self.vt)
            GPIO.output(self.in1,GPIO.LOW)
            GPIO.output(self.in2,GPIO.HIGH)
            speed = self.vt +5
            print("backward")
                
        elif x==2:
            self.p.ChangeDutyCycle(2+ self.vt)
            GPIO.output(self.in1,GPIO.LOW)
            GPIO.output(self.in2,GPIO.HIGH)
            speed = self.vt +2
            print("backward")
                
        elif x==3:
            self.p.ChangeDutyCycle(1+ self.vt)
            GPIO.output(self.in1,GPIO.LOW)
            GPIO.output(self.in2,GPIO.HIGH)
            speed =self.vt +1
            print("backward")
               
        elif x==4:
            self.p.ChangeDutyCycle(0+ self.vt)
            GPIO.output(self.in1,GPIO.LOW)
            GPIO.output(self.in2,GPIO.LOW)
            speed = self.vt
            print("Still")
                
        elif x==5:
            self.p.ChangeDutyCycle(1+ self.vt)
            GPIO.output(self.in1,GPIO.HIGH)
            GPIO.output(self.in2,GPIO.LOW)
            speed = self.vt +1
            print("forward")
               
        elif x==6:
            self.p.ChangeDutyCycle(2+ self.vt)
            GPIO.output(self.in1,GPIO.HIGH)
            GPIO.output(self.in2,GPIO.LOW)
            speed = self.vt+2
            print("forward")
        
        elif x==7:
            self.p.ChangeDutyCycle(5+ self.vt)
            GPIO.output(self.in1,GPIO.HIGH)
            GPIO.output(self.in2,GPIO.LOW)
            speed = self.vt +5
            print("forward")
               
        else :
            self.p.ChangeDutyCycle(10+ self.vt)
            GPIO.output(self.in1,GPIO.HIGH)
            GPIO.output(self.in2,GPIO.LOW)
            speed = self.vt +10
            print("forward")
                
        #GPIO.output(self.in1,GPIO.LOW)
        #GPIO.output(self.in2,GPIO.LOW)
        self.vt = speed
        if x <= 4:
            return -speed
        else:
            return speed
        
        
'''
        while(1):

            x=input()
            
            if x=='r':
                print("run")
                if(temp1==1):
                 GPIO.output(in1,GPIO.HIGH)
                 GPIO.output(in2,GPIO.LOW)
                 print("forward")
                 x='z'
                else:
                 GPIO.output(in1,GPIO.LOW)
                 GPIO.output(in2,GPIO.HIGH)
                 print("backward")
                 x='z'


            elif x=='s':
                print("stop")
                GPIO.output(in1,GPIO.LOW)
                GPIO.output(in2,GPIO.LOW)
                x='z'

            elif x=='f':
                print("forward")
                GPIO.output(in1,GPIO.HIGH)
                GPIO.output(in2,GPIO.LOW)
                temp1=1
                x='z'

            elif x=='b':
                print("backward")
                GPIO.output(in1,GPIO.LOW)
                GPIO.output(in2,GPIO.HIGH)
                temp1=0
                x='z'

            elif x=='l':
                print("low")
                p.ChangeDutyCycle(25)
                x='z'

            elif x=='m':
                print("medium")
                p.ChangeDutyCycle(50)
                x='z'
            
            elif x=='h':
                print("high")
                p.ChangeDutyCycle(75)
                x='z'
             
            
            elif x=='e':
                GPIO.cleanup()
                break
            
            else:
                print("<<<  wrong data  >>>")
            print("please enter the defined data to continue.....")
            
'''
