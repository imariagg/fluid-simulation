from visual import *
import OperacionesVectoriales 


def MetodoEuler(posicion, velocidad, aceleracion, pasoTiempo):
   
    nuevaCinematica=[]

    #v_n+1 = v_n + a_n*t
    nuevaVelocidad = velocidad + (aceleracion*pasoTiempo)

    if(nuevaVelocidad.y > 4.5):
        nuevaVelocidad.y = 0.85 * nuevaVelocidad.y

    tAceleracion = (0.5 * pasoTiempo) * pasoTiempo
    tVelocidad = nuevaVelocidad * pasoTiempo 
    nuevaPosicion = vector(tVelocidad.x+tAceleracion, tVelocidad.y+tAceleracion, tVelocidad.z+tAceleracion )
    nuevaPosicion = nuevaPosicion + posicion 

    nuevaCinematica.append(nuevaPosicion)
    nuevaCinematica.append(nuevaVelocidad)
    return nuevaCinematica
   

