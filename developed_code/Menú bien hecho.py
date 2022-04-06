import os
import pygame
import pygame_menu
import game
pygame.init()
surface = pygame.display.set_mode((600, 600))
AZUL = (21, 67, 96)
CELESTE = (121, 179, 213)
FONDO = (0, 0, 0)

dimensiones = [512, 512]

ancho = int(dimensiones[0] / 8)
alto = int(dimensiones[1] / 8)
pygame.mixer_music.load("poke.mp3")
pygame.mixer_music.play(3)
'''ancho = alto = 512 # un poco menos es otra opcion como 300
dimension = 8 #dimensiones del tablero
tamaño_pieza= alto//dimensiones  # por eso escogi 512'''

Imagenes={}
'''
Creamos un diccionario que contenga las imagenes
'''
def imag():
    piezas=["aR_gyarados", "ar_milotic-reina", "aC_seadra-caballo", "aA_empoleon-alfil", "aT_kyogre-torre", "a_magikarp", "f_charmander", "fr_reshiram-reina", "fC_rapidash-caballo", "fA_infernape-alfil", "fT_groudon-torre","fR_charizard"]

    for pieza in piezas:  #iteremos por cada nombre de la pieza para meterlo a nuestra lista imagenes y asi no consumimos tantas lineas
        Imagenes[pieza] = pygame.transform.scale(pygame.image.load("pokemones/"+pieza +".png"),(ancho,alto)) #ERROR

def set_difficulty(value, difficulty):
    # Do the job here !
    pass

def start_the_game():
    # Do the job here !
    def main():

        # Inicia el juego
        pygame.init()

        # crear la pantalla

        pantalla = pygame.display.set_mode(dimensiones)

        # Titulo e iconos
        pygame.display.set_caption("Poke-Chess")
        icono = pygame.image.load("chess.png")
        pygame.display.set_icon(icono)

        reloj = pygame.time.Clock()
        juego = game.Juego()
        imag()  # para llamar a la funcion y cargar las imagenes
        movimientos_Validos = juego.mov_validos()
        jugador_movimiento = False

        Cuadrado = ()  # iran los cuadrados que seran seleccionados por el jugador /tupla (fila,columna)
        Click = []  # para saber que clicks a dado el jugador

        # Loop del juego para que la pantalla no se cierre al instante y cerrar el juego cuando queramos
        juego_terminado = False

        while juego_terminado is False:
            for evento in pygame.event.get():
                if evento.type == pygame.QUIT:
                    juego_terminado = True

                # parte para el movimiento de las piezas
                elif evento.type == pygame.MOUSEBUTTONDOWN:
                    lugar = pygame.mouse.get_pos()  # x,y posicion del mouse dentro del tablero
                    columna = lugar[0] // ancho
                    fila = lugar[1] // alto

                    if Cuadrado == (fila, columna):  # Si el jugador a clickeado el mismo cuadrado
                        Cuadrado = ()  # lo vacio ,por que ya esta tomado esa posicion
                        Click = []  # vaciamos la lista de los clicks que ha dado el jugador
                    else:
                        Cuadrado = (fila, columna)
                        Click.append(Cuadrado)  # append ambos clicks
                    if len(Click) == 2:  # cuando el click sea el segundo
                        move = game.Movimiento_piezas(Click[0], Click[1], juego.tabla)
                        print(move.Apuntes_chess())
                        if move in movimientos_Validos:
                            juego.movimiento_nuevo()
                            jugador_movimiento = True
                        juego.movimiento_nuevo(move)
                        Cuadrado = ()  # reseteamos los clicks a los cuadrados
                        Click = []
                elif evento.type == pygame.KEYDOWN:
                    if evento.key == pygame.K_q:  # RETROCEDE EL MOVIMIENTO DE LA PIEZA SI PRESIONA 'q'
                        juego.anterior_movimiento()
                        '''movimientos_Validos = juego.mov_validos() #llamamos a los movimientos'''
                        jugador_movimiento = True
            if jugador_movimiento:
                movimientos_Validos = juego.mov_validos()
                jugador_movimiento = False

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
            graphic_game(pantalla, juego)
            reloj.tick(5)
            pygame.display.flip()

        pygame.quit()

    def graphic_game(pantalla, juego):
        piezas(pantalla, juego.tabla)  # llamamos a la tabla del otro archivo y aqui se posicionan arriba del tablero

    def piezas(pantalla, tabla):
        # dibujamos las piezas
        for i in range(0, 8):
            for j in range(0, 8):
                pieza = tabla[i][j]
                if pieza != "**":
                    pantalla.blit(Imagenes[pieza], pygame.Rect(i * ancho, j * alto, ancho, alto))  # error

    main()
    pass

menu = pygame_menu.Menu(300, 400, 'Poke-Chess',
                       theme=pygame_menu.themes.THEME_SOLARIZED)


menu.add_selector('Difficulty :', [('Hard', 1), ('Easy', 2)], onchange=set_difficulty)
menu.add_button('Play', start_the_game)
menu.add_button('Quit', pygame_menu.events.EXIT)
menu.mainloop(surface)