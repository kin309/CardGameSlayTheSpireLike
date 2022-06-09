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
                hand.add_card(drawn_card)
                deck.remove_card(drawn_card)
            else:
                for card in discardpile.cards:
                    deck.add_card(card)
                discardpile.cards.clear()
                deck.shuffle()
                hand.add_card(deck.cards[0])
                deck.remove_card(deck.cards[0])

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
