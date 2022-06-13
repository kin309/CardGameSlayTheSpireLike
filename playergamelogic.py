from cardpile import deck, discardpile
from random import choice
from hand import hand
from creature import Creature

class PlayerGameLogic(Creature):
    def __init__(self, x=180, y=400, width=100, height=100, colorz=(10,120,30), border=True, border_color=(100,170,100)):
        Creature.__init__(self, 10, x, y, width, height, colorz, border, border_color)
        self.initial_draw = 5
        self.draw_for_turn = 5
        self.max_energy = 5
        self.current_energy = 5

    def shuffle_discard_pile(self):
        for card in discardpile.cards:
            deck.add_card(card)
        discardpile.cards.clear()

    def draw_cards(self, num):
        for x in range(num):
            if len(deck.cards) > 0:
                drawn_card = deck.cards[0]
                hand.add_card(drawn_card)
                deck.remove_card(drawn_card)
            else:
                for card in discardpile.cards:
                    deck.add_card(card)
                discardpile.empty_cards()
                deck.shuffle()
                if len(deck.cards) > 0:
                    hand.add_card(deck.cards[0])
                    deck.remove_card(deck.cards[0])

    def discard_hand(self):
        for card in hand.cards:
            discardpile.add_card(card)
        hand.cards.clear()

    def draw_initial_cards(self):
        for x in range(self.initial_draw):
            self.draw_cards(1)

    def use_card(self, card, target, player):
        if card.play(target) and player.current_energy >= card.cost:
            player.current_energy -= card.cost
            player.change_energy_text()
            card.use(target, player)
            hand.remove_card(card)
            card.selected = False
            discardpile.add_card(card)
        elif card.play(target):
            print("Sem energa")
            card.go_to_initial_pos()
            card.selected = False

    def start_turn(self):
        self.current_energy = self.max_energy
        self.draw_cards(self.draw_for_turn)
        self.current_block = 0
        self.change_block_text()

    def end_turn(self):
        self.discard_hand()

