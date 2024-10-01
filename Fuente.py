from visual import *
from ClaseParticula import *
from SistemaParticulas import *


def generaColumna(posicionInicial, masa, numParticulasX, numParticulasY, numParticulasZ, separacion, vel,radio):

    fuente = SistemaParticulas()
    for i in range(numParticulasY):
        
        for j in range(numParticulasZ):
            it=0
            for w in range(numParticulasX):
                if j%2==0:
                    it=0.1
                
                pos=posicionInicial+ vector((separacion*i)+it,(separacion*j),(separacion*w))
                parti=Particula(pos,radio,vel, masa, color=(0.4,0.5,0.8))
                
                fuente.agregaParticula(parti)

    return fuente

