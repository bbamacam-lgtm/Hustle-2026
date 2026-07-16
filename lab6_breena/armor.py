import random

class Armor:
    def __init__(self, name, max_block):
        self.max_block = max_block
        self.name = name

    def block(self):
        random_damage = random.randint(0, self.max_block)
        print (random_damage)
        return random_damage

if __name__ == "__main__":
    armor_1 = Ability("Really Strong Helmet", 50)
    print(armor_1.name)
    print(armor_1.max_block)
    armor_1.block()