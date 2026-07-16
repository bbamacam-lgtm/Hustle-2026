import random

class Weapon(Ability):
   def __init__(self, name, max_damage):
        self.name = name
        self.max_damage = max_damage
         
    def attack(self):
        half_damage = self.max_damage // 2
        return random.randint(half_damage, self.max_damage)