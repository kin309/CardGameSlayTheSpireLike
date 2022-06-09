from pygame import Rect, draw, mouse, MOUSEBUTTONDOWN
from screen import screen1

class Rectangle:
    def __init__(self, x, y, width, height, colorz, border, border_color):
        self.pos = [x, y]
        self.area = [width, height]
        self.rect = Rect(self.pos, self.area)
        self.init_color = colorz
        self.color = colorz
        self.init_border_color = border_color
        self.border = border
        self.clicked = False
        if border is True:
            self.border_color = border_color
            self.border_width = 4
            self.border_rect = Rect(self.pos[0] - self.border_width, self.pos[1] - self.border_width,
                                self.area[0] + self.border_width * 2, self.area[1] + self.border_width * 2)

        self.original_width_size = self.rect.width
        self.original_height_size = self.rect.height
        self.resized_width = self.original_width_size*1.4
        self.resized_height = self.original_height_size*1.4
        self.normal_size = True

    def draw(self):
        if self.border is True:
            self.draw_border()
        draw.rect(screen1, self.color, self.rect)

    def draw_with_border(self):
        self.draw_border()
        self.draw()

    def draw_border(self):
        draw.rect(screen1, self.border_color, self.border_rect)

    def move_border(self):
        self.border_rect.x = self.rect.x - self.border_width
        self.border_rect.y = self.rect.y - self.border_width

class InteractiveRectangle(Rectangle):
    def __init__(self, x=0, y=0, width=10, height=10, color=(0,0,0), border=False, border_color=(0,0,0)):
        super(InteractiveRectangle, self).__init__(x, y, width, height, color, border, border_color)
        self.index = 0
        self.mouse_distancex = 0
        self.mouse_distancey = 0
        self.selected = False

    def move(self):
        self.rect.x = mouse.get_pos()[0] - self.mouse_distancex
        self.rect.y = mouse.get_pos()[1] - self.mouse_distancey
        try:
            self.move_border()
        except AttributeError:
            pass

    def move_border(self):
        self.border_rect.x = self.rect.x - self.border_width
        self.border_rect.y = self.rect.y - self.border_width

    def resize_border(self):
        self.border_rect.width = self.rect.width + self.border_width * 2
        self.border_rect.height = self.rect.height + self.border_width * 2

    def reposition_border(self):
        self.border_rect.x = self.rect.x - self.border_width
        self.border_rect.y = self.rect.y - self.border_width

    def resize(self, width, height):
        self.rect.width = width
        self.rect.height = height
        self.resize_border()
        self.reposition()

    def reposition(self):
        self.rect.x -= (self.resized_width - self.original_width_size)/2
        self.rect.y -= (self.resized_height - self.original_height_size)/2
        self.reposition_border()

    def go_to_initial_pos(self):
        self.rect.x = self.pos[0]
        self.rect.y = self.pos[1]
        self.move_border()

    def mouse_collide(self):
        if self.rect.collidepoint(mouse.get_pos()):
            return True
        else:
            return False

    def mouse_pressed(self):
        if self.mouse_collide() and mouse.get_pressed()[0]:
            return True
        else:
            return False

    def mouse_click(self, event):
        if self.mouse_collide() and (event.type == MOUSEBUTTONDOWN and event.button == 1):
            return True
        else:
            return False

    def redefine_init_pos(self):
        self.pos[0] = self.rect.x
        self.pos[1] = self.rect.y