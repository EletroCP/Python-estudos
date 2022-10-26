from character import Character
from ligth_saber import LigthSaber
from random import choice, randint


class Jedi(Character):
    def __init__(self, name, race, peso, heigth, hp):
        super().__init__(name, race, peso, heigth, hp)
        self.ligth_saber = LigthSaber('green', randint(15, 30))

    def defense(self):
        defense = choice([True, False])
        if defense:
            print(f"{self.name} defendeu")
            return defense

    def counter_atack(self, enemy):
        enemy.damage_hp(self.ligth_saber.power)

    def speak(self):
        return "Que a força esteja com você"
