from Organismo import Organismo

class Planta(Organismo):
    def init(self, Pos_x, Pos_y, Vida, Energia, Velocidad, Sexo, NombreP):
        super().init(Pos_x, Pos_y, Vida, Energia, Velocidad, Sexo)
        self.NombreP = NombreP

    def Fotosintesis(self):
        print(self.NombreP, " esta haciendo fotosintesis.")

    def Reproducirse(self):
        print(self.NombreP, " se esta reproduciendo.")