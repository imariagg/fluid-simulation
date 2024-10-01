from visual import *
import OperacionesVectoriales 

class Dinamica:

    def __init__(self, sistemaParticulas,h):
        self.sistema = sistemaParticulas
        self.h=h
        #self.numParticulas=sistemaParticulas.

    def calculaFuerzas(self,k):
        
        fuerzaI=vector(0.0,0.0,0.0)
        fuerzaJ=vector(0.0,0.0,0.0)
        numParticulasSistema=self.sistema.getNumParticulas()
                
        for i in range (numParticulasSistema):
            particulasI = self.sistema.getParticula(i)      
            vecinas = particulasI.getVecinas()
            F = vector(0.0,0.0,0.0)
           #print(len(vecinas))
            for j in range (len(vecinas)):
                particulaJ = vecinas[j]

                direccion = particulaJ.getPosicion() - particulasI.getPosicion()
                distancia = mag(direccion)
                
                form1= distancia - self.h
                vUnitario = direccion.norm()
                fuerzaVecina = vector(form1*vUnitario.x,form1*vUnitario.y,form1*vUnitario.z)
                fuerzaJ=vector(fuerzaVecina.x+F.x,fuerzaVecina.y+F.y,fuerzaVecina.z+F.z)
                
                
            fuerzaI = vector(k*fuerzaJ.x, k*fuerzaJ.y, k*fuerzaJ.z)
            particulasI.setFuerzaInterna(fuerzaI)
            
