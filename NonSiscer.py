from time import sleep
from Motor import Motor
import threading
from random import randint


max_speed = 50
min_speed = 10
motor = Motor(16,20,19,26,0)
sensor_input = 50

def updateSensor():
  global sensor_input
  threading.Timer(0.1, updateSensor).start()
  sensor_input = randint(-50,50)
  print 'updated!'


updateSensor()
motor.startMotor()
try :
    while 1:
        if (sensor_input < 0):
            speed_kiri = max_speed
            speed_kanan = min_speed
        else if (sensor_input > 0):
            speed_kiri = min_speed
            speed_kanan = max_speed
        else if (sensor_input = 0):
            speed_kiri = max_speed;
            speed_kanan = max_speed;
        motor.setSpeed(speed_kiri,speed_kanan)
        print sensor_input,' - ',speed_kiri,' - ',speed_kanan
        sleep(0.05)
except KeyboardInterrupt:
    print 'done!'