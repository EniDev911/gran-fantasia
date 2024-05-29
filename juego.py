from personaje import Personaje
from dialogos import leer_dialogos
import random, time, os


if __name__ == "__main__":

    print(leer_dialogos("principal"))
    print(leer_dialogos("p1"))
    clear = lambda: os.system("cls" if os.name == "nt" else "clear")
    p1 = Personaje(input())
    orco = Personaje("Orco")
    jugar = 1

    while jugar == 1:

        print(p1.estado)
        jugar = Personaje.jugar(p1.probabilidad_de_ganar(orco) * 100)

        if random.uniform(0, 1) < p1.probabilidad:
            p1.estado = 50
            orco.estado = -30
            clear()
            print(leer_dialogos("ganado"))
            time.sleep(2)
            clear()
        else:
            p1.estado = -30
            orco.estado = 50
            clear()
            print(leer_dialogos("perdido"))
            time.sleep(2)
            clear()

print("¡Has huido! El orco ha quedado atrás.")
