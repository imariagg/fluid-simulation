#CLASE PARTICULA
from visual import *

class Particula:

    def __init__(self,posicion,radio,velocidad, masa, color):
        self.posicion=posicion
        self.radio=radio
        self.velocidad=velocidad
        self.masa=masa
        self.densidad = 0
        self.colision=False

        self.vecinas=[]
        self.fuerzaInterna=vector(0.0,0.0,0.0)
        self.esfera=sphere(pos=posicion, radius=radio, color=color)
        self.esfera.velocity = velocidad
    



    #Metodos consultores
    def getPosicion(self):
        return self.esfera.pos

    def getRadio(self):
        return self.esfera.radius
    
    def getVelocidad(self):
        return self.velocidad

    def getColor(self):
        return self.esfera.color

    def getColision(self):
        return self.colision

    def getMasa(self):
        return self.masa

    def getDensidad(self):
        return self.densidad

    def getVecinas(self):
        return self.vecinas

    def getNumVecinas(self):
        return len(self.vecinas)

    def getFuerzaInterna(self):
        return self.fuerzaInterna


    #Metodos modificadores
    def setPosicion(self, posicion):
        self.esfera.pos=posicion

    def setRadio(self, radio):
        self.esfera.radius=radio

    def setVelocidad(self, velocidad):
        self.velocidad=velocidad
        self.esfera.velocity=velocidad

    def setColor(self, color):
        self.esfera.color=color

    def setColision(self, bool):
        self.colision=bool

    def setMasa(self, masa):
        self.masa=masa
        
    def setDensidad(self, densidad):
        self.densidad=densidad

    def setVecinas(self,lista):
        self.vecinas = lista

    def setFuerzaInterna(self, fuerzaInterna):
        self.fuerzaInterna=fuerzaInterna

    def resetFuerzasInternas(self):
        self.fuerzaInterna=vector(0.0,0.0,0.0)
