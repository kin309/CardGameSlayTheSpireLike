from creature import Creature
from timer import timer1
from text import Text
from colors import Color

class Enemy(Creature):
    def __init__(self, damage, x=0, y=0, width=100, height=100, colorz=(40, 50, 10), border=True, border_color=(10, 10, 20)):
        super(Enemy, self).__init__(10, x, y, width, height, colorz, border, border_color)
        self.damage = damage
        self.attacked = False
        self.start_time_attack = 0
        self.attack_duration = 1000
        self.my_turn = False
        self.damage_text = Text(f"{self.damage}", self.rect.x, self.rect.y, 26, align="center", color=(220, 30, 30))

    def attack(self, target):
        if not self.attacked and self.current_hp > 0:
            target.take_damage(self.damage)
            self.attacked = True

    def start_turn(self):
        self.start_time_attack = timer1.get_ms_time()
        self.attacked = False

    def show_damage(self):
        self.damage_text.draw()
        self.damage_text.move(self.rect.x + self.rect.width/2, self.rect.y-50)

    def draw_interface(self):
        self.draw()
        self.healthbar()
        self.block_text.draw()
        self.life_text.draw()
        self.show_damage()
