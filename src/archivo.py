from io import open
from game import Score

Record=Score
Archivo_chess=open("archivo.txt","w")
Record="Tu record es:"+ str(Score)
Archivo_chess.write(Score)

Archivo_chess.close()

Archivo_chess=open("archivo.txt","a")

Archivo_chess.write("\nNuevo Record:"+str(Score))

Archivo_chess.close()
