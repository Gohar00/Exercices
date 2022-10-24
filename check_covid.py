from math import *


class Covid19:

    def __init__(self, temp):
        self.temp = temp

    def result(self):
        x = ceil(self.temp * pi)
        if (x >= 120) and (x <= 128):
            return "You have coronavirus"
        else:
            return "Everything is ok"


utemp = float(input("Enter your temperature: "))
y = Covid19(utemp)
print(y.result())