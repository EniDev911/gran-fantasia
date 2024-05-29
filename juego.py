from personaje import Personaje
from dialogos import leer_dialogos
import random, time, os


if __name__ == "__main__":

    print(leer_dialogos("principal"))
    print(leer_dialogos("p1"))
    clear = lambda: os.system("cls" if os.name == "nt" else "clear")
    p1 = Personaje(input())
    orco = Personaje("Orco")

    while True:

        print(p1.estado + "\n")
        jugar = Personaje.jugar(p1.probabilidad_de_ganar(orco) * 100)
        if jugar == 1:
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
        else:
            break

print("¡Has huido! El orco ha quedado atrás.")
