import pygame.draw
from pygame import Rect
from screen import screen1
from text import Text
from rectangle import InteractiveRectangle
from colors import Color

class Button(InteractiveRectangle):
    def __init__(self, x, y, width, height, border=False):
        super(Button, self).__init__(x, y, width, height, Color.green, border, Color.red)

    def check_mouse_collide(self):
        if self.rect.collidepoint(pygame.mouse.get_pos()):
            return True
        else:
            return False

    def check_mouse_pressed(self):
        if self.check_mouse_collide() and pygame.mouse.get_pressed()[0]:
            return True
        else:
            return False

    def check_mouse_click(self, event):
        if self.check_mouse_collide() and event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            return True
        else:
            return False


class InterfaceButton(Button):
    def __init__(self, text, x=10, y=10, width=200, height=120, font_size = 40):
        super(InterfaceButton, self).__init__(x, y, width, height, True)

        self.font_size = font_size
        self.text = Text(text, self.rect.x+(self.rect.width/2), self.rect.y+self.rect.height/2, self.font_size, "center")
        if self.rect.width < self.text.area[0]:
            self.resize(self.text.area[0]+10, self.text.area[1]+10)
            self.text = Text(text, self.rect.x+(self.rect.width/2), self.rect.y+self.rect.height/2, self.font_size, "center")

        if self.rect.height < self.text.area[1]:
            self.resize(self.text.area[0]+10, self.text.area[1]+10)
            self.text = Text(text, self.rect.x+(self.rect.width/2), self.rect.y+self.rect.height/2, self.font_size, "center")

    def draw_button(self):
        self.draw_border()
        self.draw()
        self.text.draw()


    def check_mouse_collide(self):
        if self.rect.collidepoint(pygame.mouse.get_pos()):
            self.color = (245, 00, 00)
            self.border_color = Color.darkgray
            return True
        else:
            self.color = pygame.color.Color("darkred")
            self.border_color = Color.lightgray
            return False
