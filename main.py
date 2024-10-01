from visual import *
from ClaseParticula import *
from SistemaParticulas import *
from Dinamica import *
from DinamicaEstable import *
#-------------------
import GestorColisiones
import MetodosIntegracion
import OperacionesVectoriales
import Fuente
import Vecinas
import vecinasHash
import Canvas
import Binario


print('inicio sistema')


#Implementacion de la ventana de simulacion

scene = display(title="SPH", width=500, height=500, x=0, y=0, center = (1./2.,1./2.,1./2.), forward = (129.620536, 3.904938, 123.748005) )
scene.autoscale = False

scene.forward # position
scene.center # look up
#Canvas.ejes()

#Generar contenedor con el que colisiona las particulas.
caja = box(pos=(0.15,0,0.9), length=4.5, height=3, width=2.0)
caja.opacity = 0.1

#Se genera un objeto de colision y a ese objeto se le pasa para como parametro la caja

#-----------------------------
#Limites de X
posicionX = caja.pos.x
LimSupX = posicionX + (0.5*caja.length)
LimInfX = posicionX - (0.5*caja.length)
LimitesX = [LimInfX,LimSupX]
#Limites de Y
posicionY = caja.pos.y
LimSupY = posicionY + (0.5*caja.height)
LimInfY = posicionY - (0.5*caja.height)
LimitesY = [LimInfY,LimSupY]
#Limites de Z
posicionZ = caja.pos.z
LimSupZ = posicionZ + (0.5*caja.width)
LimInfZ = posicionZ - (0.5*caja.width)
LimitesZ = [LimInfZ,LimSupZ]


#-----------------------------
#-----GeneraParticulas--------
#-----------------------------

#viscosidad=0.86
viscosidad=0
masa = 0.1
radio = 0.04
h = 0.18 #radio dominio soportado
separacion = 1.08 * h
numParticulasX = 7#7
numParticulasY = 10#10
numParticulasZ = 20#20
posicionInicial = vector(-0.5,0.0, 0.25)
velocidadInicial = vector(0.2,-4.0,0.5)

espesor = 0.0001+radio #cota de tolerancia a la colision

 

#Generar fuente de columna cuadrada
fluido = Fuente.generaColumna(posicionInicial, masa, numParticulasX, numParticulasY, numParticulasZ, separacion, velocidadInicial, radio)
numeroParticulas = fluido.getNumParticulas()
#----------------------------------------------------------

#Calcular fuerza externa, en este caso solo hay gravedad
aceleracion = vector(0.0,-9.81, 0.0)
fuerzaExterna = vector(masa*aceleracion.x,    masa*aceleracion.y,    masa*aceleracion.z) 

#--------------------------------------------------------------
#Variables para el bucle de simulacion.

K = 100
#200 peta, 100 no peta pero se queda en la pared (update, si peta pero ya a los 250 frames), siguiente 70K con la fuente movida y con mas particulas(7-10-20) (no paso nada asi que subo a 500-1000 peta, 200 un poco, 175 fundido, con 160 parece que va pero tampoco, con 100 si, con 125...)
#K=125
#rango entre 100 y 125
pasoTiempo = 0.001
cont = 0
Frame=0

#Calcular fuerzas internas con la clase dinamica 
#MyDynamica = Dinamica(fluido, h)
MyDynamica=DinamicaEstable(fluido,h, K, viscosidad)


#Hasta aqui la inicializacion

#parte iterativa del bucle de simulacion

while cont < 6000:
    rate(100)
    
    
    #Calcula vecinas. Lo calcula mediante busqueda exhaustiva
    vecinasHash.calculaVecinosHash(fluido,h)
    #Vecinas.calculaVecinasBruta(fluido,h)
    #print(cont)

    #Calcula la fuerza interna para todo el sistema
    #MyDynamica.calculaFuerzas(K)
    MyDynamica.calculaFuerzas()
    
    
    
    for i in range(numeroParticulas):
    
     #1 calcular colisiones
        particula_i = fluido.getParticula(i)
        GestorColisiones.detectaColisionLimites(LimitesX, LimitesY, LimitesZ, espesor, particula_i)
     
        if (particula_i.getColision() == True):
            particula_i.setColision(False)
            #la particula ha colisionado, como la cinematica se tiene que calcular
            #en el gestorColision ya estan calculadas la nueva posicion y velocidad,
            #por lo tanto solo hay que cambiar el estado de colision de la particula
            
        else:
            #La particula no esta colisionando, entonces calculo con la MyDynamica calculo
            #las nuevas posiciones posicion y velocidad.
            
            velocidadParticula = particula_i.getVelocidad()
            posicionParticula = particula_i.getPosicion()
            
            #Se obtinen las fuerzas internas que calculadas en MyDynamica.
            fuerzasInternas = particula_i.getFuerzaInterna()
            fuerzaNeta = vector(fuerzasInternas.x + fuerzaExterna.x, fuerzasInternas.y + fuerzaExterna.y, fuerzasInternas.z + fuerzaExterna.z)
            aceleracion = OperacionesVectoriales.escalarPorVector(fuerzaNeta,(1/masa))
            
           
            nuevaCinematica = MetodosIntegracion.MetodoEuler(posicionParticula, velocidadParticula, aceleracion, pasoTiempo)
            particula_i.setPosicion(nuevaCinematica[0])
            particula_i.setVelocidad(nuevaCinematica[1])
            particula_i.resetFuerzasInternas()
    
    if (cont%15==0):
        Binario.exportar('Frame_binarios/archivo',Frame,fluido,radio)
        Frame=Frame+1
    
             
    cont+=1

print 'Simulacion Concluida'







    
