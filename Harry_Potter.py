from random import *


class HarryPotter:

    def __init__(self, mlist):
        self.ml = mlist

    def rand_l(self):
        nl = []
        for i in range(3):
            wlv = choice(self.ml)
            nl.append(wlv)
            y = nl
        count = 0
        for i in self.ml:
            if i in y:
                count += 1
            if count >= 2:
                return f"{y} You Win"
            else:
                return f"{y} You Lose"


x = HarryPotter(["Avada Kedavra", "Crucio", "Imperio"])
y = x.rand_l()
print(y)
