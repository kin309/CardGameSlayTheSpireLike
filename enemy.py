from creature import Creature
from timer import timer1


class Enemy(Creature):
    def __init__(self, damage, x=0, y=0, width=100, height=100, colorz=(40, 50, 10), border=True, border_color=(10, 10, 20)):
        super(Enemy, self).__init__(10, x, y, width, height, colorz, border, border_color)
        self.damage = damage
        self.attacked = False
        self.start_time_attack = 0
        self.attack_duration = 1000
        self.my_turn = False

    def attack(self, target):
        if not self.attacked and self.current_hp > 0:
            target.take_damage(self.damage)
            self.attacked = True

    def start_turn(self):
        self.start_time_attack = timer1.get_ms_time()
        self.attacked = False