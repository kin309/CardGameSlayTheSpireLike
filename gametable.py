from rectangle import Rectangle
from screen import screen1


class GameTable(Rectangle):
    def __init__(self, x=40, y=40, width=screen1.get_width()-80, height=screen1.get_height()-80, colorz=(60,40,10)):
        super(GameTable, self).__init__(x, y, width, height, colorz, border=False, border_color=(0,0,0))