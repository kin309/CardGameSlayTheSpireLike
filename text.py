import pygame
from screen import screen1

pygame.init()

class Text:
    def __init__(self, text_chars, x, y, font_size, align=""):
        self.text_chars = text_chars
        self.font_size = font_size
        self.font_color = (255,255,255)
        self.font = self.configure_font()
        self.font_rendered = self.font_render()
        self.rect = self.font_rendered.get_rect()
        self.area = self.rect[2], self.rect[3]
        self.align = align
        self.x = x
        self.y = y
        self.centerx, self.centery = self.x - self.area[0]/2, self.y - self.area[1]/2
        if self.align == "center":
            self.x = self.centerx
            self.y = self.centery


    def configure_font(self):
        return pygame.font.SysFont("verdana", self.font_size)

    def draw(self):
        screen1.blit(self.font_rendered, (self.x, self.y))

    def font_render(self):
        return self.font.render(self.text_chars, True, self.font_color)


# text1 = Text("Ola mundo!", 20, 10, 40)