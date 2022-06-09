from creature import Creature


class Enemy(Creature):
    def __init__(self, x=0, y=0, width=100, height=100, colorz=(40, 50, 10), border=True, border_color=(10, 10, 20)):
        super(Enemy, self).__init__(10, x, y, width, height, colorz, border, border_color)