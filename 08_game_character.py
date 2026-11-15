class GameCharacter:
    def __init__(self, name, health, power):
        self.name = name
        self.health = health
        self.power = power

    def attack(self):
        print(self.name, "attacks with power", self.power)

    def take_damage(self, damage):
        self.health = self.health - damage

        if self.health < 0:
            self.health = 0

        print(self.name, "health:", self.health)

hero = GameCharacter("Hero", 100, 20)
hero.attack()
hero.take_damage(30)
