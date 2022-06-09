from rectangle import Rectangle
from cardset import CardSet
from text import Text
from card import Card


class CardPile(Rectangle, CardSet):
    def __init__(self, colorz, border_color, x=80, y=780, width=140, height=160,  border=True):
        Rectangle.__init__(self, x, y, width, height, colorz, border, border_color)
        CardSet.__init__(self)
        self.count_cards()
        self.text = Text(f"{self.num_of_cards}", self.rect.x+self.rect.width/2, self.rect.y+self.rect.height/2, 40, "center")

    def draw_interface(self):
        self.draw()
        self.text.draw()

    def add_card(self, card):
        self.cards.append(card)
        self.count_cards()
        self.text = Text(f"{self.num_of_cards}", self.rect.x + self.rect.width / 2, self.rect.y + self.rect.height / 2,
                         40, "center")

    def remove_card(self, card):
        self.cards.remove(card)
        self.count_cards()
        self.text = Text(f"{self.num_of_cards}", self.rect.x + self.rect.width / 2, self.rect.y + self.rect.height / 2,
                         40, "center")

    def empty_cards(self):
        self.cards.clear()
        self.count_cards()
        self.text = Text(f"{self.num_of_cards}", self.rect.x + self.rect.width / 2, self.rect.y + self.rect.height / 2,
                         40, "center")

discardpile = CardPile((120, 120, 100), (80, 80, 80), x=1440)
deck = CardPile((100,100,120),(80,80,80), x=20)