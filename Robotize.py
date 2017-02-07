from time import sleep
from Motor import Motor
import threading
from random import randint

from SugenoFuzzyControl import SugenoFuzzyControl
from Sensor import Sensor

max_speed = 50
min_speed = 10
motor = Motor(21,23,22,24,0)
sensor = Sensor(3,5,7,8,12,11,13,15)
fuzzy = SugenoFuzzyControl(min_speed,max_speed)
sensor_input = 50

updateSensor()
motor.startMotor()
try :
    while 1:
        sensor_input = sensor.readSensor()
        speed_kiri = fuzzy.leftMotor(sensor_input)
        speed_kanan = fuzzy.rightMotor(sensor_input)
        motor.setSpeed(speed_kiri,speed_kanan)
        # print sensor_input,' - ',speed_kiri,' - ',speed_kanan
        # sleep(0.05)
except KeyboardInterrupt:
    print 'done!'