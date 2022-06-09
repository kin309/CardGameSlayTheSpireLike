import pygame.draw
from pygame import Rect
from screen import screen1
from text import Text
from rectangle import Rectangle

class Button(Rectangle):
    def __init__(self, x, y, width, height):
        super(Button, self).__init__(x, y, width, height)

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
    def __init__(self, text, x=10, y=10, width=200, height=120):
        super(InterfaceButton, self).__init__(x, y, width, height)

        self.text = Text(text, self.rect.x+(self.rect.width/2), self.rect.y+self.rect.height/2, 50, "center")

    def draw_text(self):
        self.text.draw()

    def check_mouse_collide(self):
        if self.rect.collidepoint(pygame.mouse.get_pos()):
            self.color = (245, 00, 00)
            self.border_color = pygame.color.Color("gray")
            return True
        else:
            self.color = pygame.color.Color("darkred")
            self.border_color = pygame.color.Color("gray")
            return False
