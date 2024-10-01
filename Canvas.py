#'CAMARA Y EJES'
from visual import *

#Dibujar ejes
def ejes():

    ejeX = arrow(pos=vector(0,0,0), axis=vector(1,0,0), shaftwidth=0.05)
    ejeY = arrow(pos=vector(0,0,0), axis=vector(0,1,0), shaftwidth=0.05)
    ejeZ = arrow(pos=vector(0,0,0), axis=vector(0,0,1), shaftwidth=0.05)

    ejeX.color = (1,0,0)
    ejeY.color = (0,1,0)
    ejeZ.color = (0,0,1)

    #Escribir labels
    
    label(pos=vector(1,0,0), text='X')
    label(pos=vector(0,1,0), text='Y')
    label(pos=vector(0,0,1), text='Z')
    

#Modificar el zoom del visualizado
scene.range=3
