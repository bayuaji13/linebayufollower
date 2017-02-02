from __future__ import division

import sys
import math


# membership functions
class SugenoFuzzyControl:

    def __init__(self,minimal,maksimal):
        self.fast = 66.666667
        self.slow = 33.333333
        #33.11128072,68.58773251
        self.minimal = minimal
        self.maksimal = maksimal

    def largeNegative(self,x):
        if x >= -50 and x <= 0:
            return -2*x
        else:
            return 0

    def smallNegative(self,x):
        if x >= -50 and x <= 5:
            return (1.8*x) + 90
        elif x >= 5 and x <= 50:
            return 100

    def largePositive(self,x):
        if x >= -50 and x <= 0:
            return 0
        else:
            return 2*x

    def smallPositive(self,x):
        if x >= -50 and x <= -5:
            return 100
        elif x >= -5 and x <= 50:
            return 91 - (1.8*x)

    def calibrate(self,x):
        return self.minimal + (((x - self.slow) / (self.fast - self.slow)) * (self.maksimal - self.minimal))

    #Rule buat RM 
    def rightMotor(self,x):
        first = self.largePositive(x) * self.slow + self.smallPositive(x) * self.fast
        second = self.largePositive(x) + self.smallPositive(x)
        try:
            hasil = first / second
        except ZeroDivisionError:
            hasil = first
        return self.calibrate(hasil)

    #Rule buat LM
    def leftMotor(self,x):
        first1 = self.largeNegative(x) * self.slow + self.smallNegative(x) * self.fast
        second1 = self.largeNegative(x) + self.smallNegative(x)
        try:
            hasil = first1 / second1
        except ZeroDivisionError:
            hasil = first1
        return self.calibrate(hasil)

