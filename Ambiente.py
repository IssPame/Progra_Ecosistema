class Ambiente:
    def __init__(self, Temperatura, Salinidad):
        self.Temperatura = Temperatura
        self.Salinidad = Salinidad
        
    def Marea_Roja(self):
        if((self.Salinidad > 20) or (self.Temperatura > 30)):
            print("Hay marea roja")
        else:
            print("No hay peligro de marea roja")
            
    def Marea_Negra(self):
        print("Un barco a derramado petroleo")