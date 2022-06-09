from cardset import CardSet

class Hand(CardSet):
    def __init__(self):
        super(Hand, self).__init__()

        self.x = 400
        self.y = 770
        self.max = 7
        self.set_interface()

    def set_interface(self):
        for x, card in enumerate(self.cards):
            card.pos[0], card.pos[1] = (x * (card.area[0]-10)) + self.x - len(self.cards) * (card.area[0]-10)/10, self.y
            card.init_posx, card.init_posy = card.rect.x, card.rect.y
            card.go_to_initial_pos()
            card.move_border()

    def add_card(self, card):
        self.cards.append(card)
        self.set_interface()
        self.count_cards()

    def remove_card(self, card):
        self.cards.remove(card)
        self.set_interface()
        self.count_cards()

hand = Hand()