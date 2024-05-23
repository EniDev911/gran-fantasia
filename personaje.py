from mensajes import leer_dialogos

class Character:

    nivel = 1
    experience = 0 # min: 0 - max: 99
    probability = 0

    def __init__(self, name):
        self.name = name
        self.__experience = 0

    def consultar_estado(self):
        print(f"NOMBRE: {self.name.upper()}", end="\t\t")
        print(f"NIVEL: {self.nivel}", end="\t")
        print(f"EXPERIENCIA: {self.experience}")

    @property
    def experience(self):
        return self.__experience
    
    @experience.setter
    def experience(self, nuevo):
        self.__experience = nuevo

    @staticmethod
    def acciones(probabilidad: int):
        print(leer_dialogos('probabilidad') % probabilidad)
        print(leer_dialogos('si_ganas'))
        print(leer_dialogos('si_pierdes'))
        print(leer_dialogos('jugar'))
        return input('> ')

    def actualizar_estado(self, experience: int):
        escala = experience // 99

        if experience < 0:
            self.experience -= abs(experience % 100)
            if self.experience <= 0:
                if self.nivel == 1:
                    self.nivel = 1
                    self.experience = 0
                else:
                    self.nivel -= 1
                    self.experience = 0
        else:
            self.experience = experience % 100
            self.nivel += escala

    def probabilidad_de_ganar(self, other):
        if self > other:
            self.probability = 66
        elif self < other:
            self.probability = 33
        elif self == other:
            self.probability = 50

        return f'{self.probability}%'

    def __gt__(self, other):
        return self.nivel > other.nivel
    def __lt__(self, other):
        return self.nivel < other.nivel
     
    def __eq__(self, other):
        return self.nivel == other.nivel


if __name__ == "__main__":

    p1 = Character("puffy")
    p2 = Character("laly")
    p2.experience = 30
    print(p2.experience)
    # p1.actualizar_estado(250)
    # p1.actualizar_estado(-201)
    # print(p1.consultar_estado())


