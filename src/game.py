'''
@author:Tony Astuhuamán
@author:Jorge Ata
'''
'''
Tendra toda la informacion del juego(jugabilidad)
Tambien tendra las funciones de los movimientos
'''

class Juego():
    #tabla 8x8
    def __init__(self):  #esto es un constructor de intialize
        self.tabla = [
            ["fT_groudon-torre", "fC_rapidash-caballo", "fA_infernape-alfil", "fr_reshiram-reina", "fR_charizard","fA_infernape-alfil", "fC_rapidash-caballo", "fT_groudon-torre"],
            ["f_charmander", "f_charmander", "f_charmander", "f_charmander", "f_charmander", "f_charmander", "f_charmander", "f_charmander"],
            ["**", "**", "**", "**", "**", "**", "**", "**"],
            ["**", "**", "**", "**", "**", "**", "**", "**"],
            ["**", "**", "**", "**", "**", "**", "**", "**"],
            ["**", "**", "**", "**", "**", "**", "**", "**"],
            ["a_magikarp", "a_magikarp", "a_magikarp", "a_magikarp", "a_magikarp", "a_magikarp", "a_magikarp", "a_magikarp"],
            ["aT_kyogre-torre", "aC_seadra-caballo", "aA_empoleon-alfil", "ar_milotic-reina", "aR_gyarados", "aA_empoleon-alfil", "aC_seadra-caballo", "aT_kyogre-torre"]
        ]

        self.Turno_Agua = True
        self.lista_movimientos= [] #reserva los movimientos especiales que el usuario usa
        self.posicion_gyarados = (7,4)
        self.posicion_charizard = (0,4)
        self.gameOver=False

    def movimiento_nuevo(self, movi):
        self.tabla[movi.sFila][movi.sCol] ="**" # cuando dejamos movemos una pieza dejamos un espacio
        self.tabla[movi.eFila][movi.eCol] = movi.pieza_mov
        self.lista_movimientos.append(movi) #log el movimeinto , y luego lo podemos cambiar
        self.Turno_Agua = not self.Turno_Agua #este constructor nos hace cambiar el jugador de Agua a Fuego

        '''esto es el check y nos sirve para '''
        if movi.pieza_mov =='aR_gyarados':
            self.posicion_gyarados =(movi.eFila,movi.eCol)
        elif movi.pieza_mov == 'fR_charizard':
            self.posicion_charizard = (movi.eFila,movi.eCol)


    #deshacer el ultimo movimiento
    def Regresar(self):
        if len(self.lista_movimientos) != 0: #le decimos si es que existe un movimiento para retroceder
            movi = self.lista_movimientos.pop() # sacara el ultimo movimiento
            self.tabla[movi.sFila][movi.sCol] = movi.pieza_mov
            self.tabla[movi.eFila][movi.eCol] = movi.captura_pieza  #error
            self.Turno_Agua = not self.Turno_Agua #intercambiamos turnos de regreso

            if movi.pieza_mov == 'aR_gyarados':
                self.posicion_gyarados = (movi.sFila, movi.sCol)
            elif movi.pieza_mov == 'fR_charizard':
                self.posicion_charizard = (movi.sFila, movi.sCol)
    # todos los movimiendos validos

    def mov_validos(self):
        return self.todos_mov()  # no cuenta los hackes,en passant y otros movimientos especiales


    #todos los movimientos considerando los checks
    def todos_mov(self):
        moves=[] #Movimiento_piezas((6,4),(4,4),self.tabla)
        for f in range(len(self.tabla)): # numero de filas
            for c in range(len(self.tabla[f])): # numero de columas dadas en una fila
                turno = self.tabla[f][c][0]
                if (turno == 'a' and self.Turno_Agua) or (turno == 'f' and not self.Turno_Agua): # tomamos los primeros valores de la tabla
                    pieza = self.tabla[f][c][1]
                    if pieza == '_':  #charmander(noobs pokemons)
                        self.noob(f,c, moves)
                    elif pieza =='T': #torre
                        self.torres(f,c,moves)
                    elif pieza == 'A': #alfil
                        self.alfil(f,c,moves)
                    elif pieza == 'C': #caballo
                        self.caballo(f,c,moves)
                    elif pieza == 'r': #reina
                        self.reina(f,c,moves)
                    elif pieza == 'R': #rey
                        self.rey(f,c,moves)

        return moves

    ''' limitamos las funciones de cada pieza'''
    #aqui vemos el movimiento de los peones tamando referencia la fila, columna y añadimos los movimientos a la lista 'moves' definida en 'todos_mov'
    def noob(self, f,c, moves):
       if self.Turno_Agua: #movimiento de los peones de agua
           if self.tabla[f - 1][c] == "**": #el movimiento de un peon
               moves.append(Movimiento_piezas((f,c),(f-1,c),self.tabla))
               ''' en la fila 6 enpiezan los peones de agua'''
               if f == 6 and self.tabla[f-2][c] == "**": #2 movimiento del peon
                   moves.append(Movimiento_piezas((f,c),(f-2,c),self.tabla))

           if c >= 0: #captura la izquierda
               if self.tabla[f-1][c-1][0] == 'f': #captura a la pieza de fuego
                    moves.append(Movimiento_piezas((f,c),(f-1,c-1),self.tabla))
           if c+1 <= 7:  #captura el de la derecha
                   if self.tabla[f-1][c+1][0] == 'f': #captura a la pieza de fuego
                        moves.append(Movimiento_piezas((f,c),(f-1,c+1),self.tabla))

       else: # movimiento de los peones de fuego
           if self.tabla[f + 1][c] == "**": #el movimiento de un peon
               moves.append(Movimiento_piezas((f,c),(f+1,c),self.tabla))
               #en la fila 6 enpiezan los peones de agua
               if f == 1 and self.tabla[f+2][c] == "**": #2 movimiento del peon
                   moves.append(Movimiento_piezas((f,c),(f+2,c),self.tabla))

           if c-1 >= 0: #captura izquierda
               if self.tabla[f+1][c-1][0] == 'a': #captura a la pieza de agua
                    moves.append(Movimiento_piezas((f,c),(f + 1,c-1),self.tabla))
           if c + 1 <= 7:  #captura el de la derecha
                   if self.tabla[f+1][c+1][0] == 'a': #captura a la pieza de agua
                        moves.append(Movimiento_piezas((f,c),(f+1,c+1),self.tabla))



    # aqui vemos el movimiento de las torres tamando referencia la fila, columna y añadimos los movimientos a la lista 'moves' definida en 'todos_mov'
    def caballo(self, f, c, moves):
        movimientos = ((-2, -1), (-2, 1), (-1, -2), (-1, 2), (1, -2), (1, 2), (2, -1), (2, 1))
        if self.Turno_Agua:
            enemigo = 'f'
            amigo = 'a'
        else:
            enemigo = 'a'
            amigo = 'f'
        for i in movimientos:
            eFila = f + i[0]
            eCol = c + i[1]
            if 0 <= eFila < 8 and 0 <= eCol < 8:
                nPieza = self.tabla[eFila][eCol]
                if nPieza[0] != amigo:
                    moves.append(Movimiento_piezas((f, c), (eFila, eCol), self.tabla))
                    #prueba

                # if nPieza[0] == enemigo: # si es pieza enemiga(espacio vacio y pieza) ERROR

    def torres(self,f,c,moves):
        direcciones = ((-1,0),(0,-1),(1,0),(0,1)) # parte superior, izquierda, abajo , derecha
        if self.Turno_Agua:
            enemigo = 'f'
            amigo ='a'
        else:
            enemigo = 'a'
            amigo='f'
        for eje in direcciones:
            for i in range(1,8):
                eFila = f + eje[0] *i
                eCol = c + eje[1] * i
                if 0 <= eFila <8 and 0 <= eCol <8:  #los cuadrados que estan en el tablero
                    nPieza = self.tabla[eFila][eCol]
                    if nPieza == "**":
                        moves.append(Movimiento_piezas((f,c),(eFila,eCol), self.tabla))
                    elif nPieza[0] == enemigo: #pieza del enemigo
                        moves.append(Movimiento_piezas((f,c),(eFila,eCol), self.tabla))
                    '''else:   #si el movimiento es correcto
                        break
                else:    #esta fuera del tablero
                    break'''


    def alfil(self,f,c,moves):
        movimientos = ((-1, -1), (-1, 1), (1, -1), (1, 1))  # parte superior, izquierda, abajo , derecha
        if self.Turno_Agua:
            enemigo = 'f'
            amigo ='a'
        else:
            enemigo = 'a'
            amigo ='f'
        for eje in movimientos:
            for i in range(1, 8):
                eFila = f + eje[0] * i
                eCol = c + eje[1] * i
                if 0 <= eFila < 8 and 0 <= eCol < 8:  # los cuadrados que estan en el tablero
                    nPieza = self.tabla[eFila][eCol]
                    if nPieza == "**":
                        moves.append(Movimiento_piezas((f, c), (eFila, eCol), self.tabla))
                    elif nPieza[0] == enemigo:  # pieza del enemigo
                        moves.append(Movimiento_piezas((f, c), (eFila, eCol), self.tabla))
                        #codigo
                    '''    break
                    else:  # si el movimiento es correcto
                        break
                else:  # esta fuera del tablero
                    break
'''
    def reina(self, f, c, moves): #combinamos los movimientos de la torre y el alfil
        self.alfil(f, c, moves)
        self.torres(f, c, moves)

    def rey(self,f,c,moves):
        movimientos=((-1,-1),(-1, 0),(-1,1),(0,-1),(0,1),(1,-1),(1,0),(1,1))
        if self.Turno_Agua:
            enemigo = 'f'
            amigo ='a'
        else:
            enemigo = 'a'
            amigo='f'
        for i in range(0,8):
            eFila = f + movimientos[i][0]
            eCol = c + movimientos[i][1]
            if 0 <= eFila <8 and 0<=eCol < 8 :
                nPieza = self.tabla[eFila][eCol]
                if nPieza[0] != amigo:
                    moves.append(Movimiento_piezas((f, c), (eFila, eCol), self.tabla))





class Movimiento_piezas(): #hacemos una clase para hacer el seguimiento de las piezas y la mejor forma es con
    # mapeamos los valores en un diccionario  key:value

    rango_Fila = {"1": 7, "2": 6, "3": 5, "4": 4, "5": 3, "6": 2, "7": 1, "8": 0}

    fila_rango = {value: key for key, value in rango_Fila.items()}
    arch_columnas = {"a": 0, "b": 1, "c": 2, "d": 3, "e": 4, "f": 5, "g": 6, "h": 7}

    columnas_arch = {value: key for key, value in arch_columnas.items()}

    #constructores
    def __init__(self, start, end, tabla): #este inicializador nos sirve para tener la informacion de todos los movimientos en cada bloque en el tablero
        self.sFila= start[0]
        self.sCol = start[1]
        self.eFila = end[0]
        self.eCol = end[1]
        self.pieza_mov = tabla[self.sFila][self.sCol]
        self.captura_pieza = tabla[self.eFila][self.eCol]
        self.moveID = self.sFila * 1000 + self.sCol *100 + self.eFila * 10 + self.eCol
        # 0 a 7 * 1000 o asigna a cada casillero un ID del 0 a 7777, similar a "hash functions"
        '''print("ID:",self.moveID)'''

    def __eq__(self, other):
        if isinstance(other, Movimiento_piezas):
            return self.moveID == other.moveID
        return False


    def Apuntes_chess(self):
        return self.obtenerRangos(self.sFila, self.sCol) + self.obtenerRangos(self.eFila, self.eCol)

    def obtenerRangos(self, f, c):
        return self.columnas_arch[c] + self.fila_rango[f]