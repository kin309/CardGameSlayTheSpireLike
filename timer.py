from pygame import time

class Timer:
    def __init__(self):
        self.clock = time.Clock()

    def get_ms_time(self):
        return time.get_ticks()

timer1 = Timer()