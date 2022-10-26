from character import Character
from ligth_saber import LigthSaber
from random import randint


class Sith(Character):
    def __init__(self, name, race, peso, heigth, hp):
        super().__init__(name, race, peso, heigth, hp)
        # chamando o metodo super ele estrutura da mesma forma que a classe pai
        self.ligth_saber = LigthSaber('red', randint(15, 30))

    def atack(self, enemy):
        if not enemy.defense():
            enemy.damage_hp(self.ligth_saber.power)

    def speak(self):
        return "Venha para o lado negro da força"
