from personaje import Character
from mensajes import leer_dialogos
import random

if __name__ == "__main__":
    print(leer_dialogos('principal'))
    print(leer_dialogos('p1'))
    name_jugador = input()
    p1 = Character(name_jugador)
    p1.consultar_estado()
    print(leer_dialogos('inicio'))
    orco = Character("Orco")

    while True:
        opcion = Character.acciones(p1.probabilidad_de_ganar(orco))
        numero = round(random.uniform(random.random(), p1.probability), 2)
        if opcion == "1":
            break
        

