from visual import *
from Fuente import * 

def calculaVecinasBruta(sistemaParticulas,h):

    numParticulas =  sistemaParticulas.getNumParticulas()

    for i in range(numParticulas):
        parti_i = sistemaParticulas.getParticula(i)
        listaVecinas=[]

        for j in range(numParticulas):
            parti_j = sistemaParticulas.getParticula(j)
            
            if (parti_i != parti_j):
                #Si la particula_i no es igual a particula_j sacas la distancia entre ambas y después su módulo
                distancia_vector=parti_j.getPosicion() - parti_i.getPosicion()
                distancia = mag(distancia_vector)
               
                if (distancia < h):
                    listaVecinas.append(parti_j)

        parti_i.setVecinas(listaVecinas)

