import RPi.GPIO as GPIO
import time

class Sensor:

    def __init__(self,pinLeft1,pinLeft2,pinLeft3,pinLeft4,pinRight1,pinRight2,pinRight3,pinRight4):

        GPIO.setmode(GPIO.BCM)

		self.sensorLeft1 = pinLeft1;
		self.sensorLeft2 = pinLeft2;
		self.sensorLeft3 = pinLeft3;
		self.sensorLeft4 = pinLeft4;

		self.sensorRight1 = pinRight1;
		self.sensorRight2 = pinRight2;
		self.sensorRight3 = pinRight3;
		self.sensorRight4 = pinRight4;

        GPIO.setup(self.sensorLeft1,GPIO.IN);
        GPIO.setup(self.sensorLeft2,GPIO.IN);
        GPIO.setup(self.sensorLeft3,GPIO.IN);
        GPIO.setup(self.sensorLeft4,GPIO.IN);

        GPIO.setup(self.sensorRight1,GPIO.IN);
        GPIO.setup(self.sensorRight2,GPIO.IN);
        GPIO.setup(self.sensorRight3,GPIO.IN);
        GPIO.setup(self.sensorRight4,GPIO.IN);
	
	def readSensor(self) :
		right = 0;
		left = 0;

		if (not GPIO.input(self.sensorLeft1)) :
			# print("1");
			left = left + 8;
		if (not GPIO.input(self.sensorLeft2)) :
			# print("2");
			left = left + 4;
		if (not GPIO.input(self.sensorLeft3)) :
			# print("3");
			left = left + 2;
		if (not GPIO.input(self.sensorLeft4)) :
			# print("4");
			left = left + 1;
		# print(bin(kiri));
		# kiri = 0;
		if (not GPIO.input(self.sensorRight1)) :
			# print("5");
			right = right + 8;
		if (not GPIO.input(self.sensorRight2)) :
			# print("6");
			right = right + 4;
		if (not GPIO.input(self.sensorRight3)) :
			# print("7");
			right = right + 2;
		if (not GPIO.input(self.sensorRight4)) :
			# print("8");
			right = right + 1;
		
		# Konversi ke skala -50,50
		hasil = right - left;

		return -50 + (((hasil - (-16)) / (16 - (-16))) * (50 - (-50)));