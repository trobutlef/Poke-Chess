#########################
#  made by Jorge Ata.   #    
#########################
import pygame

AZUL=(21, 67, 96)
CELESTE=(121, 179,213)
FONDO=(0, 0, 0)

#Inicia el juego
pygame.init()

#crear la pantalla
dimensiones = [600, 600]
pantalla = pygame.display.set_mode(dimensiones)

#Titulo e iconos
pygame.display.set_caption("Aje-Chess")
icono = pygame.image.load("chess.png")
pygame.display.set_icon(icono)

#Loop del juego para que la pantalla no se cierre al instante y cerrar el juego cuando queramos
juego_terminado = False
reloj = pygame.time.Clock()
ancho = int(dimensiones[0] / 8)
alto = int(dimensiones[1] / 8)

while juego_terminado is False:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            juego_terminado = True
    pantalla.fill(CELESTE)
    color = 0
    for i in range(0, dimensiones[0], ancho):
        for j in range(0, dimensiones[1], alto):
            if color % 2 == 0:
                pygame.draw.rect(pantalla, AZUL, [i, j, ancho, alto], 0)
            else:
                pygame.draw.rect(pantalla, CELESTE, [i, j, ancho, alto], 0)
            color += 1
        color += 1
    pygame.display.flip()
    reloj.tick(5)
pygame.quit()
#hasta aqui parte de Jorge