from Organismo import Organismo

class Especie(Organismo):
    def init(self, Pos_x, Pos_y, Vida, Energia, Velocidad, Sexo, NombreE, Dieta, Edad):
        super().init(Pos_x, Pos_y, Vida, Energia, Velocidad, Sexo)
        self.NombreE = NombreE
        self.Dieta = Dieta
        self.Edad = Edad

    def Cazar(self):
        if(self.Energia > 5):
            print(self.NombreE, " esta cazando.")
        else:
            print(self.NombreE, " no tiene suficiente energia para cazar.")

    def Huir(self):
        if(self.Energia > 5):
            print(self.NombreE, " ha logrado huir.")
        else:
            print(self.NombreE, " no ha logrado huir.")

    def Nadar(self):
        print(self.NombreE, " esta nadando.")

    def Reproducirse(self):
        print(self.NombreE, " se esta reproduciendo.")