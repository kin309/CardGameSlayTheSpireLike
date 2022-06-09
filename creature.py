from pygame import Rect, draw
from rectangle import Rectangle
from text import Text
from screen import screen1


class Creature(Rectangle):
    def __init__(self, max_hp, x=0, y=0, width=100, height=100, colorz=(100, 50, 40), border=True, border_color=(50,25,20)):
        super(Creature, self).__init__(x, y, width, height, colorz, border, border_color)
        self.max_hp = max_hp
        self.current_hp = max_hp
        self.current_block = 1

        self.healthb_posx = self.rect.x - 10
        self.healthb_posy = self.rect.y + self.rect.height + 14
        self.healthb_width = 120
        self.healthb_height = 30

        self.block_text = Text(f"Block: {self.current_block}", self.rect.x, self.rect.y + self.rect.height + 50, 30)
        self.life_text = Text(f"{self.current_hp}/{self.max_hp}", self.healthb_posx+self.rect.width/2, self.healthb_posy+self.healthb_height/2, 20, "center")
        self.texts = [self.block_text, self.life_text]

    def draw_interface(self):
        self.draw()
        self.healthbar()
        self.block_text.draw()
        self.life_text.draw()

    def healthbar(self):
        bar_color = (10, 100, 10)

        progres_bar = self.current_hp * self.healthb_width / self.max_hp
        draw.rect(screen1, (70, 10, 10), (self.healthb_posx, self.healthb_posy, self.healthb_width, self.healthb_height))
        draw.rect(screen1, bar_color, (self.healthb_posx, self.healthb_posy, progres_bar, self.healthb_height))

    def move_interface(self):
        self.healthb_posx = self.rect.x - 10
        self.healthb_posy = self.rect.y + self.rect.height + 14
        self.block_text.x = self.rect.x
        self.block_text.y = self.rect.y + self.rect.height + 50
        self.life_text = Text(f"{self.current_hp}/{self.max_hp}", self.healthb_posx+self.rect.width/2,
                              self.healthb_posy+self.healthb_height/2, 20, "center")

    def take_damage(self, damage):
        print(self.current_block)
        hp_taken_dmg = damage - self.current_block
        self.current_block -= damage
        if damage - self.current_block < 0:
            hp_taken_dmg = 0
        self.current_hp -= hp_taken_dmg
        if self.current_block < 0:
            self.current_block = 0
        if self.current_hp < 0:
            self.current_hp = 0
        self.life_text = Text(f"{self.current_hp}/{self.max_hp}", self.healthb_posx + self.rect.width / 2,
                              self.healthb_posy + self.healthb_height / 2, 20, "center")
        self.block_text = Text(f"Block: {self.current_block}", self.rect.x, self.rect.y + self.rect.height + 50, 30)

