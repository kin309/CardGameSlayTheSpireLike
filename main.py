import sys
import pygame
from screen import screen1
from button import InterfaceButton
from card import Card
from recthandler import RectangleHandler
from rectangle import InteractiveRectangle
from gamescene import GameScene

scene = 1
# p1 = Player()
# button1 = InterfaceButton("Jogar")

gamescene1=GameScene()

# rects = RectangleHandler(p1.hand.cards)

# def test():
#     screen1.fill(pygame.color.Color("black"))
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             pygame.quit()
#             sys.exit()
#
#         if event.type == pygame.KEYDOWN:
#             if event.key == pygame.K_SPACE:
#                 p1.hand.add_card(Card())
#         # rects.check_click(event)
#
#         # if button1.check_mouse_click(event):
#         #     pass
#     # rects.select_rectangle()
#     # rects.move_rectangle()
#     p1.draw()
#     p1.draw_cards_interface()
#
#     # button1.draw()
#     # button1.draw_text()

def scenes():
    while True:
        if scene == 1:
            gamescene1.principal()

            pygame.display.update()
            pygame.time.Clock().tick(60)

scenes()