import sys
import math
import RPi.GPIO as GPIO

# membership functions
class Motor:

    def __init__(self,pin1A,pin1B,pin2A,pin2B,speed):

        GPIO.setmode(GPIO.BCM)

        self.Motor1A = pin1A
        self.Motor1B = pin1B
        self.Motor2A = pin2A
        self.Motor2B = pin2B

        GPIO.setup(self.Motor1A,GPIO.OUT)
        GPIO.setup(self.Motor1B,GPIO.OUT)
        GPIO.setup(self.Motor2A,GPIO.OUT)
        GPIO.setup(self.Motor2B,GPIO.OUT)

        self.speed_awal = speed
        self.speed_kiri = speed
        self.speed_kanan = speed

        self.direction = 1

        self.maju_kanan = GPIO.PWM(self.Motor1B,500)
        self.maju_kiri = GPIO.PWM(self.Motor2B,500)
        self.mundur_kanan = GPIO.PWM(self.Motor1A,500)
        self.mundur_kiri = GPIO.PWM(self.Motor2A,500)

    def startMotor(self):
        self.maju_kanan.start(self.speed_kanan)
        self.maju_kiri.start(self.speed_kiri)
        self.direction = 1

    def setDirection(self,direction) :
        self.direction = direction
        if self.direction == 1 :
            self.mundur_kanan.stop()
            self.mundur_kiri.stop()

            self.maju_kanan.start(self.speed_awal)
            self.maju_kiri.start(self.speed_awal)
        elif self.direction == 2 :
            self.maju_kanan.stop()
            self.maju_kiri.stop()

            self.mundur_kanan.start(self.speed_awal)
            self.mundur_kiri.start(self.speed_awal)

    def setSpeed(self,speed_kiri,speed_kanan):
        self.speed_kiri = speed_kiri
        self.speed_kanan = speed_kanan
        if self.direction == 1 : #Maju
            self.maju_kanan.ChangeDutyCycle(self.speed_kanan)
            self.maju_kiri.ChangeDutyCycle(self.speed_kiri)

        if self.direction == 2 : #mundur
            self.mundur_kanan.ChangeDutyCycle(self.speed_kanan)
            self.mundur_kiri.ChangeDutyCycle(self.speed_kiri)

    def stopMotor(self):
        self.maju_kanan.ChangeDutyCycle(0)
        self.maju_kiri.ChangeDutyCycle(0)
        self.mundur_kanan.ChangeDutyCycle(0)
        self.mundur_kiri.ChangeDutyCycle(0)

    def motorCleanUp(self):
        self.maju_kanan.stop()
        self.maju_kiri.stop()
        self.mundur_kanan.stop()
        self.mundur_kiri.stop()
        GPIO.cleanup()

