from rectangle import Rectangle
from cardpile import discardpile, deck
from hand import hand
from creature import Creature
from card import *
from random import choice
from playergamelogic import PlayerGameLogic
from text import Text

class Player(Creature, PlayerGameLogic):
    def __init__(self, x=180, y=400, width=100, height=100, colorz=(10,120,30), border=True, border_color=(100,170,100)):
        Creature.__init__(self, 10, x, y, width, height, colorz, border, border_color)
        PlayerGameLogic.__init__(self)

        hand.set_interface()
        for x in range(7):
            deck.add_card(BuyCard())
        for x in range(2):
            deck.add_card(AttackCard())
        for x in range(2):
            deck.add_card(DefenseCard())
        deck.shuffle()

        self.energy_text = Text(f"ENG: {self.current_energy}/{self.max_energy}", self.rect.x, self.rect.y, 30)

        self.selected_card = Card()

    def draw_cards_interface(self):
        self.draw()
        self.draw_interface()
        deck.draw_interface()
        discardpile.draw_interface()
        for card in hand.cards:
            card.interface()
        try:
            self.selected_card.interface()
        except AttributeError:
            pass
        self.show_energy()

    def show_energy(self):
        self.change_energy_text()
        self.energy_text.draw()

    def change_energy_text(self):
        self.energy_text = Text(f"ENG: {self.current_energy}/{self.max_energy}", self.rect.x, self.rect.y, 30)







player1 = Player()