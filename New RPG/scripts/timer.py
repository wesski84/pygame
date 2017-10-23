from scripts.globals import *


class Timer:
    def __init__(self, interval = 1):
        self.interval = interval
        self.value = 0
        self.lastInt = 0
        self.active = False
        self.onNext = None

    def update(self):
        if self.active:
            self.value += Globals.deltatime / self.interval
            if int(self.value) != int(self.lastInt):
                self.lastInt = int(self.value)
                if self.onNext != None:
                    self.onNext()

    def start(self):
        self.active = True

    def pause(self):
        self.active = False

    def stop(self):
        self.reset()
        self.active = False

    def reset(self):
        self.value = 0
        self.lastInt = 0
        self.active = True

