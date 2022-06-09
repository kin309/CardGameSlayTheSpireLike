import pygame
from hand import hand
from rectangle import InteractiveRectangle
from pygame import mouse

class RectangleHandler:
    def __init__(self, rectangles_list):
        self.selected_rectangle = InteractiveRectangle()
        self.rectangles = rectangles_list
        self.set_index()
        self.colliding = False
        self.ready = False
        self.holding = False

    def set_index(self):
        for x in range(len(self.rectangles)):
            for rect in self.rectangles:
                if rect == self.rectangles[x]:
                    rect.index = x

    def count_collisions(self):
        num_of_collisions = 0
        for rect in self.rectangles:
            if rect.mouse_collide():
                num_of_collisions += 1
        if num_of_collisions == 0:
            self.colliding = False
        else:
            self.colliding = True

    def select_rectangle(self, event):
        self.check_click(event)
        self.count_collisions()
        for rect in self.rectangles:
            for rectos in self.rectangles:
                if rect.mouse_collide() and rectos.mouse_collide() and mouse.get_pressed()[0] is False:
                    if rect != rectos:
                        if rect.index > rectos.index:
                            self.selected_rectangle = rect
                        else:
                            self.selected_rectangle = rectos
                    else:
                        self.selected_rectangle = rect
        try:
            if self.selected_rectangle.mouse_collide() and self.selected_rectangle.normal_size is True:
                self.selected_rectangle.resize(self.selected_rectangle.resized_width, self.selected_rectangle.resized_height)
                self.selected_rectangle.normal_size = False
                self.selected_rectangle.set_text()
        except AttributeError:
            pass
        if event.type == pygame.MOUSEBUTTONUP:
            try:
                self.selected_rectangle.go_to_initial_pos()
            except AttributeError:
                pass
        try:
            for rect in self.rectangles:
                if rect.mouse_collide() is False and rect.normal_size is False and self.selected_rectangle.selected is False:
                    rect.resize(rect.original_width_size,
                                                   rect.original_height_size)
                    rect.go_to_original_font_size()
                    rect.go_to_initial_pos()
                    rect.normal_size = True
        except AttributeError:
            pass
        try:
            if self.colliding is False and self.selected_rectangle.selected is False or mouse.get_pressed()[2]:

                self.selected_rectangle.selected = False
                self.selected_rectangle = None
        except AttributeError:
            pass

        self.change_rectangle_color()
        try:
            if self.selected_rectangle.mouse_collide() and mouse.get_pressed()[0]:
                self.selected_rectangle.selected = True
            elif mouse.get_pressed()[1]:
                self.selected_rectangle.selected = False
        except AttributeError:
            pass

    def change_rectangle_color(self):
        for rect in self.rectangles:
            if rect == self.selected_rectangle:
                rect.border_color = (90, 110, 20)
            elif rect.mouse_pressed() is False:
                rect.border_color = rect.init_border_color
            else:
                pass

    def move_rectangle(self):
        try:
            if self.selected_rectangle.selected:
                self.selected_rectangle.move()
        except AttributeError:
            pass

    def exhibit(self):
        try:
            if self.selected_rectangle.mouse_collide() and self.selected_rectangle.normal_size is True:
                self.selected_rectangle.resize(self.selected_rectangle.resized_width, self.selected_rectangle.resized_height)
                self.selected_rectangle.normal_size = False
                self.selected_rectangle.set_text()
            elif self.selected_rectangle.mouse_collide() is False and self.selected_rectangle.normal_size is False:
                self.selected_rectangle.resize(self.selected_rectangle.original_width_size, self.selected_rectangle.original_height_size)
                self.selected_rectangle.go_to_original_font_size()
                self.selected_rectangle.go_to_initial_pos()
                self.normal_size = True
        except:
            pass


    def check_click(self, event):
        try:
            if self.selected_rectangle.mouse_click(event):
                self.set_mouse_distance()
            else:
                pass
        except AttributeError:
            pass

    def set_mouse_distance(self):
        self.selected_rectangle.mouse_distancex = mouse.get_pos()[0] -  self.selected_rectangle.rect.x
        self.selected_rectangle.mouse_distancey = mouse.get_pos()[1] -  self.selected_rectangle.rect.y

card_handler = RectangleHandler(hand.cards)