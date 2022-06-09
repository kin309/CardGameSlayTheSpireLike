from pygame import Rect, draw, mouse
from screen import screen1
from rectangle import InteractiveRectangle
from text import Text
from hand import hand


class Card(InteractiveRectangle):
    def  __init__(self, x=0, y=0, width=120, height=160, color=(100, 170, 30), cost=0, card_name="card"):
        super().__init__(x, y, width, height, color, True, (155, 205, 145))
        self.cost = cost
        self.font_size = 20
        self.original_font_size = 20
        self.resized_font = int(self.original_font_size*1.4)
        self.cost_text = Text(f"{self.cost}", self.rect.x, self.rect.y, self.font_size)
        self.description_text = "Essa carta não possui descrição!"
        self.description = Text(self.description_text, self.rect.x, self.rect.y, int(self.font_size * 0.7))
        self.card_name = card_name
        self.card_name_text = Text(self.card_name, self.rect.x, self.rect.y, self.font_size)
        self.draggin = False

    def play(self, target):
        if self.rect.y < 460 and mouse.get_pressed()[0] is True:
            return True
        else:
            return False

    def set_text(self):
        self.cost_text = Text(f"{self.cost}", self.rect.x, self.rect.y, self.font_size)
        self.set_card_name_text()
        self.set_description_text()

    def texts_interface(self):
        self.card_name_text.draw()
        self.cost_text.draw()
        self.description.draw()

    def set_card_name_text(self):
        self.card_name_text = Text(self.card_name, self.rect.x+25, self.rect.y, self.font_size)

    def set_description_text(self):
        self.description = Text(self.description_text, self.rect.x, self.rect.y + 30, int(self.font_size * 0.7))


    def move(self):
        self.rect.x = mouse.get_pos()[0] - self.mouse_distancex
        self.rect.y = mouse.get_pos()[1] - self.mouse_distancey
        self.set_text()
        try:
            self.move_border()
        except AttributeError:
            pass

    def go_to_initial_pos(self):
        self.rect.x = self.pos[0]
        self.rect.y = self.pos[1]
        self.set_text()
        self.move_border()

    def interface(self):
        self.draw()
        self.texts_interface()

    def resize_font(self):
        self.font_size = self.resized_font

    def go_to_original_font_size(self):
        self.font_size = self.original_font_size

    def go_to_original_size(self):
        self.resize(self.original_width_size, self.original_height_size)
        self.go_to_original_font_size()

    def resize(self, width, height):
        self.rect.width = width
        self.rect.height = height
        self.resize_border()
        self.reposition()
        self.resize_font()

    def exhibit(self):
        if self.mouse_collide() and self.normal_size:
            self.resize(self.resized_width, self.resized_height)
            self.normal_size = False
            self.set_text()
        elif self.mouse_collide() is False and self.normal_size is False:
            self.resize(self.original_width_size, self.original_height_size)
            self.go_to_original_font_size()
            self.go_to_initial_pos()
            self.normal_size = True


    def use(self, target, player):
        if mouse.get_pressed()[0] is True:
            pass

class AttackCard(Card):
    def __init__(self, x=0, y=0, width=140, height=180, color=(100, 30, 30), damage=3, cost = 1):
        super(AttackCard, self).__init__(x, y, width, height, color, cost = cost, card_name="Attack Card")
        self.damage = damage
        self.description_text = "1 Dano"
        self.set_description_text()

    def play(self, target):
        if self.rect.colliderect(target) and mouse.get_pressed()[0] is True and target.current_hp > 0:
            return True
        else:
            return False

    def use(self, target, player):
        target.take_damage(self.damage)


class DefenseCard(Card):
    def __init__(self, x = 0, y = 0, width = 140, height = 180, color=(30, 30, 100), block = 2, cost = 1):
        super(DefenseCard, self).__init__(x, y, width, height, color, cost=cost, card_name="Defense Card")
        self.block = block


    def use(self, target, player):
        if mouse.get_pressed()[0] is True:
            player.current_block += self.block

class BuyCard(Card):
    def __init__(self, x = 0, y = 0, width = 140, height = 180, color=(30, 30, 100), block = 2, cost = 1):
        super(BuyCard, self).__init__(x, y, width, height, color, cost=cost, card_name="Buy Card")
        self.block = block
        self.num_of_cards_to_buy = 1
        self.description_text = "Compra 1"
        self.set_description_text()


    def use(self, target, player):
        if mouse.get_pressed()[0] is True:
            for x in range(self.num_of_cards_to_buy):
                player.draw_cards(1)