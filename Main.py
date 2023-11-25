import pygame, sys
from pygame.locals import *

pygame.init()

Ancho, Alto = 528, 396
Anch_Sprite, Alt_Sprite = 100, 100

Pantalla = pygame.display.set_mode((Ancho, Alto))
pygame.display.set_caption("Progra_Ecosistema")

imagen_agua = pygame.image.load("Sprites/Agua.png").convert_alpha()


Escen_Panta=[
    [0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1],
    [0, 1, 0, 1, 0, 1, 0, 1, 1, 1, 0, 1],
    [0, 1, 0, 1, 0, 1, 0, 0, 0, 1, 0, 1],
    [0, 1, 0, 1, 0, 1, 1, 1, 0, 1, 0, 1],
    [0, 1, 0, 1, 0, 1, 0, 0, 0, 1, 0, 1],
    [0, 1, 0, 1, 0, 1, 0, 1, 1, 1, 0, 1],
    [0, 1, 0, 1, 0, 1, 0, 0, 0, 1, 0, 1],
    [0, 1, 0, 1, 0, 1, 1, 1, 0, 1, 0, 1],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1],
]

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

    Pantalla.fill((255, 255, 255))  # Llenar la pantalla con un color de fondo

    for fila in range(len(Escen_Panta)):
        for columna in range(len(Escen_Panta[fila])):
            if Escen_Panta[fila][columna] == 0:
                try:
                    Pantalla.blit(imagen_agua, (columna * Anch_Sprite, fila * Alt_Sprite))
                except pygame.error as e:
                    print(f"Error al cargar la imagen: {e}")

    pygame.display.flip()
  
