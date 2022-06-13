from enemy import Enemy
import copy

class Fight:
    def __init__(self, num_of_enemies):
        self.number_of_enemies = num_of_enemies
        self.enemies = []
        self.rewards = []
        for x in range(num_of_enemies):
            self.add_enemie(Enemy(1))
            self.add_enemie(Enemy(1))

    def add_enemie(self, enemy):
        self.enemies.append(copy.copy(enemy))


fight1 = Fight(2)