from random import randint
class Ambiente:
    def __init__(self, Temperatura, Salinidad):
        self.Temperatura = Temperatura
        self.Salinidad = Salinidad
        
    def Marea_Roja(self):

        probabilidadMaRed = randint(1,100)

        if((self.Salinidad > 20) or (self.Temperatura > 30)) and probabilidadMaRed <=50:
            print("Hay marea roja")
        else:
            print("No hay marea roja")
        
    def Marea_Negra(self):
        print("Un barco a derramado petroleo")