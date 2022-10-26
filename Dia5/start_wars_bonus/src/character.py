from character_interface import CharacterInterface


class Character(CharacterInterface):
    # primeiro parametro é equivalente a "this"

    def __init__(self, name, race, peso, heigth, hp):
        self.name = name
        self.race = race
        self.__heigth = heigth
        self.__peso = peso
        self.__hp = hp

    def get_peso(self):
        return self.__peso

    def get_heigth(self):
        return self.__heigth

    def get_hp(self):
        return self.__hp

    def damage_hp(self, damage):
        self.__hp -= damage

    def speak(self):
        return "Eu sei falar"

# infos confidencias ou menos acesso = private
