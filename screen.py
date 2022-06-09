from pygame import display


class Screen:
    def __init__(self):
        self.width = 1600
        self.height = 960
        self.config = display.set_mode((self.width, self.height))


screen1 = Screen().config