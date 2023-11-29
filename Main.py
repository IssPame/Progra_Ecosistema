import pygame
import sys
from pygame.locals import *
from Ambiente import Ambiente
from Organismo import Organismo 
from random import randint

pygame.init()

Ancho, Alto = 528, 396
Anch_Sprite, Alt_Sprite = 30, 30

Pantalla = pygame.display.set_mode((Ancho, Alto))
pygame.display.set_caption("Progra_Ecosistema")

imagen_Tiburon = pygame.image.load("Sprites/TB.png")
imagen_agua = pygame.image.load("Sprites/Agua.png")

ambiente=Ambiente(Temperatura=25,Salinidad=25)



Escen_Panta = [
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
]

EvalMar = False

reloj = pygame.time.Clock() 

ambiente.posicion_tiburon=[0,0,100,50,5,"M"] #x, y, Vida, Energia, Velocidad, Sexo

movimientos = {0: (0, -1),  # Arriba
               1: (0, 1),   # Abajo
               2: (-1, 0),  # Izquierda
               3: (1, 0)}   # Derecha


direccion = randint(0, 3)

ambiente.posicion_tiburon = [0, 0]
Pantalla.blit(imagen_Tiburon, (ambiente.posicion_tiburon[0] * Anch_Sprite, ambiente.posicion_tiburon[1] * Alt_Sprite))


while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

    if not EvalMar:
        ambiente.Marea_Roja()
        EvalMar = True

    # Cambio la direccion
    direccion = randint(0, 3)

    # Aplicacion del tiburon
    dx, dy = movimientos[direccion]
    ambiente.posicion_tiburon[0] = max(0, min(ambiente.posicion_tiburon[0] + dx, len(Escen_Panta[0]) - 1))
    ambiente.posicion_tiburon[1] = max(0, min(ambiente.posicion_tiburon[1] + dy, len(Escen_Panta) - 1))

    for fila in range(len(Escen_Panta)):
        for columna in range(len(Escen_Panta[fila])):
            if Escen_Panta[fila][columna] == 0:
                try:
                    Pantalla.blit(imagen_agua, (columna * Anch_Sprite, fila * Alt_Sprite))
                except pygame.error as e:
                    print(f"Error al cargar la imagen: {e}")

    Pantalla.blit(imagen_Tiburon, (ambiente.posicion_tiburon[0] * Anch_Sprite, ambiente.posicion_tiburon[1] * Alt_Sprite))

   
    reloj.tick(4)
   

    pygame.display.flip()
    