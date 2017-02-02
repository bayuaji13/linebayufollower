import RPi.GPIO as GPIO
import time

pin1 = 3;
pin2 = 10;
pin3 = 7;
pin4 = 8;

pink1 = 15;
pink2 = 13;
pink3 = 11;
pink4 = 12;
kiri = 0;
kanan = 0;
GPIO.setmode(GPIO.BOARD);

GPIO.setup(pin1, GPIO.IN);
GPIO.setup(pin2, GPIO.IN);
GPIO.setup(pin3, GPIO.IN);
GPIO.setup(pin4, GPIO.IN);
GPIO.setup(pink1, GPIO.IN);
GPIO.setup(pink2, GPIO.IN);
GPIO.setup(pink3, GPIO.IN);
GPIO.setup(pink4, GPIO.IN);

i=0;
t_end = time.time() + 20;
# while time.time() < t_end:
while 1:
	i = i+1;
	if (not GPIO.input(pin1)) :
		# print("1");
		kiri = kiri + 8;
	if (not GPIO.input(pin2)) :
		# print("2");
		kiri = kiri + 4;
	if (not GPIO.input(pin3)) :
		# print("3");
		kiri = kiri + 2;
	if (not GPIO.input(pin4)) :
		# print("4");
		kiri = kiri + 1;
	# print(bin(kiri));
	# kiri = 0;
	if (not GPIO.input(pink1)) :
		# print("5");
		kanan = kanan + 8;
	if (not GPIO.input(pink2)) :
		# print("6");
		kanan = kanan + 4;
	if (not GPIO.input(pink3)) :
		# print("7");
		kanan = kanan + 2;
	if (not GPIO.input(pink4)) :
		# print("8");
		kanan = kanan + 1;
	# print(bin(kanan));
	print "kiri = %d kanan = %d " % (kiri, kanan);
	# print "kiri = %s kanan = %s " % (bin(kiri), bin(kanan));
	kanan = 0;
	kiri = 0;
	# print(i);
	time.sleep(0.5);
print(i);