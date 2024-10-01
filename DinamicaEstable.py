from visual import *
from ClaseParticula import *
from SistemaParticulas import *
import OperacionesVectoriales
import math

'''
Este template de clase estatica es posible calcular la fuerza interna en un
modelo SPH estabilizado y simplificado. 
'''
'''
 import dinamicaEstable
 
'''

class DinamicaEstable:

    def __init__(self, sistemaParticulas,h, K, viscosidad):
        self.sistemaParticulas = sistemaParticulas
        self.h=h
        self.K=K/10.0
        self.viscosidad=viscosidad
        self.numSistemaParticulas=sistemaParticulas.getNumParticulas()


    def kernel(self,distancia):
        # Wij = (alpha * 315 * (h^2 - r^2)) / (64*pi*h^7)  siendo alpha 1.08*h^2
        '''
        alpha = (1.08 * self.h * self.h) 
        #print(distancia)
        auxH=self.h * self.h
        auxDistancia = mag(distancia)
        #print(type(auxDistancia))
        #auxDH=OperacionesVectoriales.EscalarResta(auxH,auxDistancia)
        #print(auxDH)
        form1 = alpha * 315 * (self.h*self.h - auxDistancia*auxDistancia)
        #form1 = OperacionesVectoriales.escalarPorVector(auxDH,form1)

        form2 = 64 * math.pi * pow(self.h,7)
        kernel = form1/form2
        return kernel
        '''

        
        # Wij = (alpha * 315 * (h^2 - r^2)) / (64*pi*h^7)  siendo alpha 1.08*h^2
        auxDistancia=mag(distancia)

        alpha = (1.08 * self.h * self.h) 
        form1 = alpha * 315 * (self.h*self.h - auxDistancia*auxDistancia)
        form2 = (64 * math.pi)* math.pow(self.h,7)
        kernel = form1/form2
        return kernel
        '''

        alpha = 1.08*self.h*self.h
        numerador = alpha*315
        denominador = (64*math.pi)*math.pow(self.h,7)
        multiplicador = numerador/denominador
        coef_dist=(self.h*self.h)-(distancia*distancia)
        coef_dist = math.pow(coef_dist,3)
        resultado = multiplicador*coef_dist
        return resultado 
        '''

    def gradKernel(self, distancia):
        alpha = 3.18
        beta  = 2.12
        gamma = 0.85
        cota = self.h * 0.96

        inicial = (gamma + alpha)
        inicial = 2.0*(inicial - 2.0*beta)
        inicial = inicial / cota

        segundo = 2.0*((beta-alpha)/cota)
        segundo = segundo - ((0.5 * inicial)*cota)
            
        cuadratico = inicial * (distancia * distancia)
        lineal = segundo * distancia
        Wij = cuadratico + lineal
        Wij = Wij + alpha
        return Wij



    def calculaDensidad(self):
        '''
        #aqui calculas las densidades de las particulas
        n = self.numSistemaParticulas

        for i in range(n):

            #para cada particula i
            particula_i = self.sistemaParticulas.getParticula(i)
            vecinas = particula_i.getVecinas()
            rho_i =0.0
            
            for j in range(len(vecinas)):
                #print (12)

                #rho_i = \sum_{N(i)}m_j Wij
                #masa de particula j
                masa_j = vecinas[j].getMasa()
                #calculas kernel {kernel(h,distancia)}
                distancia = vecinas[j].getPosicion() - particula_i.getPosicion()
                calculaKernel = self.kernel(distancia)
                #print(calculaKernel)
                rho_j = calculaKernel*masa_j
                #print(rho_j)
                rho_i = rho_i+rho_j

            particula_i.setDensidad(rho_i)
        '''

        #aqui calculas las densidades de las particulas
        n = self.sistemaParticulas.getNumParticulas()
        for i in range(n):
            #para cada particula i
            particula_i = self.sistemaParticulas.getParticula(i)
            vecinas = particula_i.getVecinas()
            rho_i = 0.0
            for j in range(len(vecinas)):
            #rho_i = \sum_{N(i)}m_j Wij
                #masa de particula j
                m_j= vecinas[j].getMasa()
                #calculas kernel {kernel(h,distancia)}
                distancia = vecinas[j].getPosicion() - particula_i.getPosicion()
                #distancia = mag(vecinas[j].getPosicion() - particula_i.getPosicion())
                #h = self.h
                calculaKernel = self.kernel(distancia)
                rho_j = m_j * calculaKernel 
                rho_i = rho_i + rho_j

            particula_i.setDensidad(rho_i)

    def calculaFuerzasPSPH(self):
        n = self.sistemaParticulas.getNumParticulas()
        for i in range(n):
            fuerzaTotal = vector(0.0,0.0,0.0)
            particula_i = self.sistemaParticulas.getParticula(i)
            vecinas = particula_i.getVecinas()
            numVecinas = len(vecinas)
            posicion_i = particula_i.getPosicion()
            densidad_i = particula_i.getDensidad()
            fuerzaPresion = vector(0.0,0.0,0.0)
            fuerzaViscosidad = vector(0.0,0.0,0.0)
            for j in range(numVecinas):
                particula_j = vecinas[j]
                posicion_j = particula_j.getPosicion()
                densidad_j = particula_j.getDensidad()
                direccion = posicion_j - posicion_i
                distancia = mag(direccion)             
                direccion = norm(direccion)             
                if distancia < self.h:
                    fPresion = vector(0.0,0.0,0.0)  
                    incremento = distancia - self.h
                    gradienteKernel = self.gradKernel(distancia)
                    
                    rho_max = densidad_i
                    if(densidad_j > rho_max):
                        rho_max = densidad_j
                    modulo_densidad = 0.5 * ((densidad_i+densidad_j)/rho_max)
                    modulo_densidad = (self.K * modulo_densidad)
                    
                    modulo = modulo_densidad * incremento * gradienteKernel
                    fPresion.x = (modulo*0.6) * direccion.x
                    fPresion.y = (modulo*0.75) * direccion.y
                    fPresion.z = (modulo*0.65) * direccion.z
                    fuerzaPresion = fuerzaPresion + fPresion
                #///////////////////////
                #Ahora la viscosidad
                #esta fuerza de viscosidad no requiere del laplaciano de la funcion kernel
                vrelativa = particula_i.getVelocidad() - particula_j.getVelocidad()
                modProyectado = vrelativa.dot(direccion)#producto escalar de vrelativa y direccion
                vrelativa = (modProyectado*direccion)#producto del escalar modProyectado por el vector direccion
                fViscosidad = self.viscosidad * vrelativa#producto del escalar viscosidad por el vector direccion
                fuerzaViscosidad = fuerzaViscosidad + fViscosidad
            fuerzaTotal = fuerzaPresion + fuerzaViscosidad
            particula_i.setFuerzaInterna(fuerzaTotal)



    #este gradiente de funcion kernel es totalmente operativo y mas simplificado que 
    #el usado anteriormente

    

    def calculaFuerzas(self):
        self.calculaDensidad()
        self.calculaFuerzasPSPH()




