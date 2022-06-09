from cardpile import deck, discardpile
from random import choice
from hand import hand

class PlayerGameLogic:

    initial_draw = 5

    def shuffle_discard_pile(self):
        for card in discardpile.cards:
            deck.add_card(card)
        discardpile.cards.clear()

    def draw_cards(self, num):
        for x in range(num):
            if len(deck.cards) > 0:
                drawn_card = deck.cards[0]
                deck.remove_card(drawn_card)
                hand.add_card(drawn_card)
            else:

                print("Não há cartas no seu deck")

    def draw_initial_cards(self):
        for x in range(self.initial_draw):
            self.draw_cards(1)

    def use_card(self, card, target, player):
        if card.play(target):
            card.use(target, player)
            hand.remove_card(card)
            card.selected = False
            discardpile.add_card(self)