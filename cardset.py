class CardSet:
    def __init__(self):
        self.cards = []
        self.num_of_cards = 0

    def add_card(self, card):
        self.cards.append(card)

    def remove_card(self, card):
        self.cards.remove(card)

    def empty_cards(self):
        self.cards.clear()

    def count_cards(self):
        self.num_of_cards = len(self.cards)