import pygame.draw

from rectangle import Rectangle
from screen import screen1
from gametable import GameTable


class GameInterface(Rectangle):
    def __init__(self, x=0, y=0, width=screen1.get_width(), height=100, colorz=(100,100,100)):
        super(GameInterface, self).__init__(x, y, width, height, colorz, border=False, border_color=(0,0,0))

        self.table = GameTable()

    def draw(self):
        self.table.draw()
        pygame.draw.rect(screen1, self.color, self.rect)