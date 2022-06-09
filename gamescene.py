import pygame.event
import sys
from gameinterface import GameInterface
from screen import screen1
from player import player1
from enemy import Enemy
from recthandler import card_handler
from card import Card
from hand import hand
from fight import fight1


class GameScene:
    def __init__(self):
        self.interface = GameInterface()
        self.actual_fight = fight1
        self.position_enemy_on_screen()
        self.turn = 0
        player1.draw_initial_cards()

    def position_enemy_on_screen(self):
        card_width = 120
        for x, enemy in enumerate(self.actual_fight.enemies):
            enemy.rect.x = x * (enemy.rect.width + card_width) + 1200 - len(self.actual_fight.enemies) * (
                        enemy.rect.width + card_width) / 2
            enemy.rect.y = 400
            enemy.move_border()
            enemy.move_interface()

    def draw_creatures(self):
        for en in self.actual_fight.enemies:
            en.draw_interface()
        player1.draw_cards_interface()

    def enemies_turn(self):
        for enemy in self.actual_fight.enemies:
            enemy.attack(player1)

    def principal(self):
        screen1.fill((00,00,00))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    player1.draw_cards(1)

            if self.interface.pass_turn_button.check_mouse_click(event):
                self.turn += 1
                print(self.turn)

            for en in self.actual_fight.enemies:
                for card in hand.cards:
                    try:
                        player1.use_card(card, en, player1)
                    except AttributeError:
                        pass

            card_handler.select_rectangle(event)
            player1.selected_card = card_handler.selected_rectangle

        if self.turn%2 == 1:
            player1.discard_hand()
            self.enemies_turn()
            self.turn += 1
            player1.start_turn()
        card_handler.move_rectangle()
        self.interface.draw()
        self.draw_creatures()

