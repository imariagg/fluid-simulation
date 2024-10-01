from visual import *
from ClaseParticula import *

class SistemaParticulas:

    def __init__(self):
        self.miSistema=[]


    def getNumParticulas(self):
        return len(self.miSistema)

    def agregaParticula(self, Particula):
        self.miSistema.append(Particula)

    def getParticula(self, indice):
        return self.miSistema[indice]

    def setSistemaParticulas(self,nuevoSParticulas):
        self.sistemaParticulas = nuevoSParticulas
