################
# made by Tony #
################
import pygame
import os

#piezas de agua
ag_rey = pygame.image.load(os.path.join("pokemones" ,"gyarados.png"))
ag_reina = pygame.image.load(os.path.join("pokemones" ,"milotic-reina.png"))
ag_caballo = pygame.image.load(os.path.join("pokemones" ,"seadra-caballo.png"))
ag_alfil = pygame.image.load(os.path.join("pokemones" ,"empoleon-alfil.png"))
ag_torre = pygame.image.load(os.path.join("pokemones" ,"kyogre-torre.png"))
ag_peon = pygame.image.load(os.path.join("pokemones","magikarp.png"))

#piezas de fuego
fu_rey = pygame.image.load(os.path.join("pokemones" ,"charmander.png"))
fu_reina = pygame.image.load(os.path.join("pokemones" ,"reshiram-reina-fuego.png"))
fu_caballo = pygame.image.load(os.path.join("pokemones" ,"rapidash-caballo.png"))
fu_alfil = pygame.image.load(os.path.join("pokemones" ,"infernape-alfil.png"))
fu_torre = pygame.image.load(os.path.join("pokemones" ,"groudon-torre.png"))
fu_peon = pygame.image.load(os.path.join("pokemones","charmander.png"))

fuego = [fu_rey,fu_reina,fu_caballo,fu_alfil,fu_torre,fu_peon]
agua = [ag_rey,ag_reina,ag_caballo,ag_alfil,ag_torre,ag_peon]

Fuego=[]
Agua=[]

for pokemones in fuego:
    Fuego.append(pygame.transform.scale(pokemones, (55,55)))

for pokemones in agua:
    Agua.append(pygame.transform.scale(pokemones, (55,55)))

class pieza:
    pokemones = -1
    recta = (113, 113, 525, 525)
    E_X = recta[0]
    E_Y = recta[1]

    def __init__(self, fila, columna, color):
        self.fila = fila
        self.columna = columna
        self.color = color
        self.selected = False
        self.lista_movimientos = []
        self.rey = False
        self.peon = False

    def seleccionado(self):
        return self.selected

    def nuevo_mov_valido(self, tabla):
        self.lista_movimientos = self.mov_valido(tabla)

    def empate(self, gana , color):    #Dinamica del empate
        if self.color == "fuego":
            empateThis = Fuego[self.pokemones]
        else:
            empateThis = Agua[self.pokemones]

        x = (4 - self.columna) + round(self.E_X + (self.columna * self.recta[2] / 8))
        y = 3 + round(self.E_Y + (self.fila * self.recta[3] / 8))

        if self.selected and self.color == color:
            pygame.empate.rect(gana, (255, 0, 0), (x, y, 62, 62), 4)

        gana.blit(empateThis, (x, y))  #blit la pantalla de gana

        '''if self.selected and self.color == color:  # Remover el falso para dibujar puntos
            jugadas = self.jugadas_list
            for mov in jugadas:
                x = 33 + round(self.E_X + (move[0] * self.recta[2] / 8))
                y = 33 + round(self.E_Y + (move[1] * self.recta[3] / 8))
                pygame.empate.circle(win, (255, 0, 0), (x, y), 10)'''

    def cambio_pos(self, pos):
        self.fila = pos[0]
        self.columna = pos[1]

    def __str__(self):
        return str(self.columna) + " " + str(self.fila)


class peon(pieza):
    img = 5

#poo
    def __init__(self, fila, columna, color):
        super().__init__(fila, columna, color)
        self.primero = True
        self.reina = False
        self.peon = True

    def mov_valido(self, tabla):
        i = self.fila
        j = self.columna

        mov = []
        try:
            if self.color == "f":
                if i < 7:
                    p = tabla[i + 1][j]
                    if p == 0:
                        mov.append((j, i + 1))

                    # DIAGONAL
                    if j < 7:
                        p = tabla[i + 1][j + 1]
                        if p != 0:
                            if p.color != self.color:
                                mov.append((j + 1, i + 1))

                    if j > 0:
                        p = tabla[i + 1][j - 1]
                        if p != 0:
                            if p.color != self.color:
                                mov.append((j - 1, i + 1))

                if self.primero:
                    if i < 6:
                        p = tabla[i + 2][j]
                        if p == 0:
                            if tabla[i + 1][j] == 0:
                                moves.append((j, i + 2))
                        elif p.color != self.color:
                            mov.append((j, i + 2))
            # AGUA
            else:

                if i > 0:
                    p = tabla[i - 1][j]
                    if p == 0:
                        mov.append((j, i - 1))

                if j < 7:
                    p = tabla[i - 1][j + 1]
                    if p != 0:
                        if p.color != self.color:
                            mov.append((j + 1, i - 1))

                if j > 0:
                    p = tabla[i - 1][j - 1]
                    if p != 0:
                        if p.color != self.color:
                            mov.append((j - 1, i - 1))

                if self.primero:
                    if i > 1:
                        p = tabla[i - 2][j]
                        if p == 0:
                            if tabla[i - 1][j] == 0:
                                mov.append((j, i - 2))
                        elif p.color != self.color:
                            mov.append((j, i - 2))
        except:
            pass

        return mov

    '''import pygame
    import sys

    # set up ventana de inicio
    reloj = pygame.time.Clock()

    pygame.init()

    pygame.display.set_caption("Pokemon")
    pantalla = pygame.display.set_mode((600, 400))

    font = pygame.font.SysFont(None,20)

    def texto(text, font ,color ,surface, x ,y):
        textobj = font.render(text, 1, color)
        textrect = textobj.get_rect()
        textrect.topleft = (x,y)
        surface.blit(textobj, textrect)

    def menu():
        while True:

            pantalla.fill((0,0,0))
            texto('menu principal', font, (255, 255,255),pantalla, 20, 20)
            for event in pygame.event.get():
                if event.type ==  QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == KEYDOWN:
                    if event.key == K_ESCAPE:
                        pygame.quit()
                        sys.exit()

            pygame.display.update()
            reloj.tick(60)
        pygame.quit()

    menu()

    #errores:
    while True:
        pantalla.fill()
        pygame.display.flip()  #to update stuff that I am going to put in advance

    def game_intro():
        intro= True
        while intro:
            for event in pygame.event.get():



    def crash():
        message_display('Hubo un error')
        '''
