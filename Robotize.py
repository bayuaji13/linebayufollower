from time import sleep
from Motor import Motor
import threading
from random import randint

from SugenoFuzzyControl import SugenoFuzzyControl

max_speed = 50
min_speed = 10
motor = Motor(16,20,19,26,0)
fuzzy = SugenoFuzzyControl(min_speed,max_speed)
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
        speed_kiri = fuzzy.leftMotor(sensor_input)
        speed_kanan = fuzzy.rightMotor(sensor_input)
        motor.setSpeed(speed_kiri,speed_kanan)
        print sensor_input,' - ',speed_kiri,' - ',speed_kanan
        sleep(0.05)
except KeyboardInterrupt:
    print 'done!'