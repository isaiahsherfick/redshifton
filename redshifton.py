import os
import datetime
import time


class redshifton:
    def __init__(self):
        self.time = datetime.datetime.now()
        self.enabled = False


    def updateTime(self):
        self.time = datetime.datetime.now()

    def getHour(self):
        return self.time.hour

    def isEnabled(self):
        return self.enabled

    def enable(self,val=None):
        if not self.isEnabled():
            if val == None:
                val = 4000
            print("\n\nREDUCING THE STRAIN ON YOUR EYES\n\n")
            self.disable()
            os.system(f"redshift -O {val}")
            self.enabled = True
        else:
            if val == None:
                val = 4000
            print("\n\nREDUCING THE STRAIN ON YOUR EYES\n\n")
            os.system(f"redshift -O {val}")
            self.enabled = True
    def disable(self):
        os.system("redshift -x")
        self.enabled = False

if __name__ == '__main__':
    on = False
    r = redshifton()
    while True:
        r.updateTime()
        if r.getHour() > 18:
            r.enable(4000)
        elif time.hour > 20:
            r.enable(3500)
        elif time.hour > 22:
            r.enable(3250)
        time.sleep(3600)

