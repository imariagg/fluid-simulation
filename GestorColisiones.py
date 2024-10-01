from visual import *
from ClaseParticula import *
import OperacionesVectoriales 

#CAJA

def detectaColisionLimites(LimitesX, LimitesY, LimitesZ, espesor, Particula):

    posicion = Particula.getPosicion()
    vectorNormal=vector(0.0,0.0,0.0)

    LimX_inf = LimitesX[0] + espesor
    LimX_sup = LimitesX[1] - espesor
    
    LimY_inf = LimitesY[0] + espesor
    LimY_sup = LimitesY[1] - espesor

    LimZ_inf = LimitesZ[0] + espesor
    LimZ_sup = LimitesZ[1] - espesor

    colisiona=False

 
    if posicion.x < LimX_inf or posicion.x > LimX_sup:
        if posicion.x < LimX_inf:
            colisiona=True
            #print('Choco con X')
            vectorNormalX=vector(1.0,0.0,0.0)
            vectorNormal=vectorNormal+vectorNormalX
        
        
        else:
            colisiona=True
            #print('Choco con X')
            vectorNormalX=vector(-1.0,0.0,0.0)
            vectorNormal=vectorNormal+vectorNormalX
            
        

    if posicion.y < LimY_inf:
        colisiona=True
        #print('Choco con Y')
        #print(Particula.getPosicion().y)
        vectorNormalY=vector(0.0,1.0,0.0)
        vectorNormal=vectorNormal+vectorNormalY

        


    if posicion.z < LimZ_inf or posicion.z > LimZ_sup:
        if posicion.z < LimZ_inf:
            colisiona=True
            #print('Choco con Z')
            vectorNormalZ=vector(0.0,0.0,1.0)
            vectorNormal=vectorNormal+vectorNormalZ


        else:
            colisiona=True
            #print('Choco con Z')
            vectorNormalZ=vector(0.0,0.0,-1.0)
            vectorNormal=vectorNormal+vectorNormalZ
            

    if colisiona==True:

        Particula.setColision(True)
        vectorNormal=vectorNormal.norm()
        respuestaColision(Particula, vectorNormal, espesor)



def respuestaColision(Particula, vectorNormal,espesor):
    #PARAMETROS
    tasaRozamiento=0.95
    tasaRebote=0.8  
    espesor=espesor*0.05
    ctrl=-1.0

    #INCIDENTES
    pos_i=Particula.getPosicion()
    vel_i=Particula.getVelocidad()

    #VELOCIDADES INCIDENTES
    velNormal_i=OperacionesVectoriales.proyeccion(vel_i,vectorNormal)
    velTang_i=vel_i - velNormal_i

    #VELOCIDADES RESULTANTES
    #HAY QUE HACER UNA COMPROBACION DE LA VELOCIDAD QUE SEA POSITIVA O NEGATIVO
    if mag(velNormal_i)>0:
        ctrl=1.0
        #print('hola')
    
    tasaRebote=tasaRebote*ctrl
    
    velNormal_r=tasaRebote* velNormal_i
    velTang_r=tasaRozamiento*velTang_i
    
    #VELOCIDAD RESPUESTA
    velRespuesta=velNormal_r+velTang_r
    Particula.setVelocidad(velRespuesta)

    #posicion_respuesta= pos_i+((0.49*vectorNormal.x),(0.49*vectorNormal.y),(0.49*vectorNormal.z))
    posicion_respuesta= pos_i+((espesor*vectorNormal.x),(espesor*vectorNormal.y),(espesor*vectorNormal.z))


    Particula.setPosicion(posicion_respuesta)
