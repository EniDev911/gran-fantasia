from dialogos import leer_dialogos


class Personaje:

    # Constructor
    def __init__(self, nombre):
        self.nombre = nombre  # 👈 atributo de instancia asignado por parámetro
        self.nivel = 1  # 👈 valor asignado en atributo de instancia
        self.experiencia = 0  # 👈 valor asignado en atributo de instancia

    # Getter de estado
    @property
    def estado(self):
        return (
            f"NOMBRE:{self.nombre.upper():10}"
            f"NIVEL:{self.nivel:<10}"
            f"EXPERIENCIA:{self.experiencia}"
        )

    # Setter de estado
    @estado.setter
    def estado(self, exp):
        tmp_exp = self.experiencia + exp

        while tmp_exp >= 100:
            self.nivel += 1
            tmp_exp -= 100

        while tmp_exp < 0:
            if self.nivel > 1:
                tmp_exp = 100 + tmp_exp
                self.nivel -= 1
            else:
                tmp_exp = 0
        self.experiencia = tmp_exp

    @staticmethod
    def jugar(probabilidad: int):
        print(leer_dialogos("inicio"))
        print(leer_dialogos("probabilidad").format(probabilidad))
        print(leer_dialogos("si_ganas"))
        print(leer_dialogos("si_pierdes"))
        print(leer_dialogos("jugar"))
        return int(input("> "))

    def probabilidad_de_ganar(self, other):
        if self > other:
            self.probabilidad = 0.66
        elif self < other:
            self.probabilidad = 0.33
        elif self == other:
            self.probabilidad = 0.5

        return self.probabilidad

    def __gt__(self, other):
        return self.nivel > other.nivel

    def __lt__(self, other):
        return self.nivel < other.nivel

    def __eq__(self, other):
        return self.nivel == other.nivel


if __name__ == "__main__":
    import random

    aleatorio = random.uniform(0, 1)
    p1 = Personaje("puffy")
    p2 = Personaje("laly")
    Personaje.jugar(p1.probabilidad_de_ganar(p2) * 100)

    if aleatorio > p1.probabilidad:
        p1.estado = -30
        p2.estado = 50
    else:
        p1.estado = 50
        p2.estado = -30

    print(p1.estado)
    print(p2.estado)
