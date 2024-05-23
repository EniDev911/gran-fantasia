from personaje import Character
from mensajes import leer_dialogos
from random import uniform

if __name__ == "__main__":
    print(leer_dialogos('principal'))
    print(leer_dialogos('p1'))
    name_jugador = input()
    p1 = Character(name_jugador)
    p1.consultar_estado()
    print(leer_dialogos('inicio'))
    orco = Character("Orco")

    Character.acciones(p1.probabilidad_de_ganar(orco))