import os
import pygame
import pygame_menu

AZUL=(21, 67, 96)
CELESTE=(121, 179,213)
GRANATE=(146, 43, 33)
ROJO=(205, 97, 85)

FONDO=(0, 0, 0)
pygame.init()
os.environ['SDL_VIDEO_CENTERED'] = '1'
surface = pygame.display.set_mode((600, 600))

dimensiones = [600, 600]
pantalla = pygame.display.set_mode(dimensiones)
pygame.display.set_caption("poke-Chess")
icono = pygame.image.load("chess.png")
pygame.display.set_icon(icono)
#imagenfondo= pygame.image.load("pokemon.jpg")

def set_difficulty(selected, value):
    """
    dificultad del juego.
    """
    print('Set difficulty to {} ({})'.format(selected[0], value))


def start_the_game():
    """
    funcion que empieza el juego. This is raised by the menu button,
    here menu can be disabled, etc.
    """
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
            menu = pygame_menu.Menu(height=300,
                                    width=400,
                                    theme=pygame_menu.themes.THEME_SOLARIZED,
                                    title='AJECHESS')

            menu.add_selector('Difficulty: ', [('Hard', 1), ('Easy', 2)], onchange=set_difficulty)
            pygame.mixer.music.load("poke.mp3")
            pygame.mixer.music.play(3)
            if __name__ == '__main__':
                menu.mainloop(surface)
                pygame.quit()
