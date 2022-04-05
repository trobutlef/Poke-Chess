'''
@author:Tony Astuhuamán
@author:Jorge Ata
'''

import pygame
import pygame_menu
import game
pygame.init()
surface = pygame.display.set_mode((600, 600))
AZUL = (21, 67, 96)
CELESTE = (121, 179, 213)
FONDO = (0, 0, 0)

dimensiones = [720, 720]

ancho = int(dimensiones[0] / 8)
alto = int(dimensiones[1] / 8)
pygame.mixer_music.load("LowTide.mp3")
pygame.mixer_music.play(-1)
pygame.mixer.music.set_volume(0.01)

Imagenes={}



'''
Creamos un diccionario que contenga las imagenes
'''
def imag():
    piezas=["aR_gyarados", "ar_milotic-reina", "aC_seadra-caballo", "aA_empoleon-alfil", "aT_kyogre-torre", "a_magikarp", "f_charmander", "fr_reshiram-reina", "fC_rapidash-caballo", "fA_infernape-alfil", "fT_groudon-torre","fR_charizard"]

    for pieza in piezas:  #iteremos por cada nombre de la pieza para meterlo a nuestra lista imagenes y asi no consumimos tantas lineas
        Imagenes[pieza] = pygame.transform.scale(pygame.image.load("pokemones/"+pieza +".png"),(ancho,alto)) #ERROR

def set_difficulty(value, difficulty):
    pass

def start_the_game():
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

        imag()  # para llamar a la funcion y cargar las imagenes
        juego = game.Juego()

        mov_validos = juego.mov_validos()
        jugador_movimiento = False #nos hace saber cuando se creo el movimiento

        Bloque= ()  # iran los cuadrados que seran seleccionados por el jugador /tupla (fila,columna)
        Click = []  # para saber que clicks a dado el jugador  tuplas de dos [(),()]

        # Loop del juego para que la pantalla no se cierre al instante y cerrar el juego cuando queramos
        juego_terminado = False

        while juego_terminado is False:
            for evento in pygame.event.get():
                if evento.type == pygame.QUIT:
                    juego_terminado = True

                # parte para el movimiento de las piezas
                elif evento.type == pygame.MOUSEBUTTONDOWN:
                    lugar = pygame.mouse.get_pos()  # x,y posicion del mouse dentro del tablero
                    columna = lugar[0] // alto
                    fila = lugar[1] // ancho

                    if Bloque == (fila, columna):  # Si el jugador a clickeado el mismo cuadrado
                        Bloque = ()  # lo vacio ,por que ya esta tomado esa posicion
                        Click = []  # vaciamos la lista de los clicks que ha dado el jugador

                    else:
                        Bloque = (fila, columna)
                        Click.append(Bloque)  # append ambos clicks
                    if len(Click) == 2:  # cuando el click sea el segundo
                        movi = game.Movimiento_piezas(Click[0], Click[1], juego.tabla)
                        #archivo = open("Clicks", "w+")
                        #for i in mov_validos:
                        '''archivo.write(movi.Apuntes_chess(),"\n")
                        archivo.close()'''
                        print(movi.Apuntes_chess()) #imprimimos las notaciones de los bloques

                        if movi in mov_validos:
                            juego.movimiento_nuevo(movi)  #error
                            jugador_movimiento = True
                            #error de doble llamaso del movimiento_nuevo(movi)
                            Bloque = ()  # reseteamos los clicks a los cuadrados
                            Click = []

                        else:
                            Click = [Bloque]
                elif evento.type == pygame.KEYDOWN:
                    if evento.key == pygame.K_q:  # RETROCEDE EL MOVIMIENTO DE LA PIEZA SI PRESIONA 'q'
                        juego.Regresar()
                        jugador_movimiento= True
            if jugador_movimiento:
                mov_validos = juego.mov_validos() #llamamos a los movimientos
                jugador_movimiento = False



            pantalla.fill(CELESTE)
            color = 0

            for fila in range(0, dimensiones[0], ancho):
                for columna in range(0, dimensiones[1], alto):
                    if color % 2 == 0:
                        pygame.draw.rect(pantalla, AZUL, [fila, columna, ancho, alto], 0)
                    else:
                        pygame.draw.rect(pantalla, CELESTE, [fila, columna, ancho, alto], 0)
                    color += 1
                color += 1
            graphic_game(pantalla, juego)
            reloj.tick(5)
            pygame.display.flip()

        pygame.quit()

    #ordenamos las piezas en el tablero-parte grafica
    def graphic_game(pantalla, juego):
        piezas(pantalla, juego.tabla)  # llamamos a la tabla del otro archivo y aqui se posicionan arriba del tablero

    def piezas(pantalla, tabla):
        # dibujamos las piezas
        for fila in range(0, 8):
            for columna in range(0, 8):
                pieza = tabla[fila][columna]
                if pieza != "**":
                    pantalla.blit(Imagenes[pieza], pygame.Rect( columna *ancho, fila*alto,ancho, alto))

    main()


menu = pygame_menu.Menu(300, 400, 'Poke-Chess',theme=pygame_menu.themes.THEME_SOLARIZED)


#menu.add_selector('Jugador :', [('Agua', 1), ('Fuego', 2)], onchange=set_difficulty)
menu.add_button('Play', start_the_game)
menu.add_button('Quit', pygame_menu.events.EXIT)
menu.mainloop(surface)