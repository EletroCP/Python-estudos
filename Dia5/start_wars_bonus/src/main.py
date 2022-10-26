from character import Character
from jedi import Jedi
from sith import Sith
# Para criar um personagem é necessario passar nessa orde:
# Nome, Raça, Peso, altura e vida

# Exemplo de criação de personagem comum
personagem1 = Character("Padme", "Humana", 58, 1.65, 40)
# Exemplo de criação de Jedi
personagem2 = Jedi("Yoda", "yoda", 30, 0.80, 150)
# Exemplo de criação de Sith
personagem3 = Sith("Darth Mal", "Sla", 80, 2.0, 250)


def combat(Sith: Sith, Jedi: Jedi):
    print("Inicio do combater")
    print(f"{Sith.name} Vs {Jedi.name}")
    print(f"""
    {Sith.name}:
    Sabre de cor: {Sith.ligth_saber.color}
    Dano:{Sith.ligth_saber.power}
    """)
    print(f"""
    {Sith.name}:
    Sabre de cor: {Sith.ligth_saber.color}
    Dano:{Sith.ligth_saber.power}
    """)
    print("----------------------------")

    while Sith.get_hp() > 0:
        Sith.atack(Jedi)
        print(f"Sith: {Sith.name}: HP: {Sith.get_hp()}")
        print(f"Jedi: {Jedi.name}: HP: {Jedi.get_hp()}")

        Sith.atack(Jedi)

        if Jedi.get_hp() > 0:
            Jedi.counter_atack(Sith)
        else:
            print(f"{Sith.name} Vence")
            print(Sith.speak())
            break
        print("----------------------------")
    else:
        print("----------------------------")
        print(f"{Jedi.name} vence")
        print(Jedi.speak())


# Exemplo de combate
combat(personagem2, personagem3)

# Após criar um personagem, chame a função de combate com
# os seus nomes como parametro, !!! IMPORTANTE !!!
# Sith sempre atacam antes.
