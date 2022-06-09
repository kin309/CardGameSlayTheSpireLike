from enemy import Enemy

class Fight:
    def __init__(self, num_of_enemies):
        self.number_of_enemies = num_of_enemies
        self.enemies = []
        self.rewards = []
        self.add_enemies(2, Enemy())

    def add_enemies(self, num, enemy):
        for x in range(num):
            self.enemies.append(enemy)

fight1 = Fight(2)