from visual import *

def sumaEscalar(vector1, escalar):
    vecAux=vector(vector1.x,vector1.y,vector1.z)

    x=vecAux.x
   #print(x)
    #print(escalar)
    x=x+escalar

    y=vecAux.y
    y=y+escalar

    z=vecAux.z
    z=z+escalar

    vecAux=vector(x, y, z)
    return vecAux

def sumaVectores(vec1,vec2):
    vecAux=vector(0.0,0.0,0.0)
    vecAux=vector(vec1.x+vec2.x, vec1.y+vec2.y + vec1.z+vec2.z)
    return vecAux

def restaEscalar(vector1, escalar):
    vecAux=vector(0,0,0)
    vecAux=(vector1.x-escalar, vector1.y-escalar, vector1.z-escalar)
    return vecAux

def EscalarResta(escalar,vector1):
    vecAux=vector(0,0,0)
    x=vector1.x
    x=escalar-x

    y=vector1.y
    y=escalar-y

    z=vector1.z
    z=escalar-z

    vecAux=vector(x, y, z)
    return vecAux

def productoEscalar(vector1,vector2):
    
    escalar=vector1.x+vector2.x
    escalar=escalar+(vector1.y+vector2.y)
    escalar=escalar+(vector1.z+vector2.z)

    return escalar

def multiplicar(vector1,vector2):
    x=vector1.x*vector2.x
    y=vector1.y*vector2.y
    z=vector1.z*vector2.z
    aux=vector(x,y,z)
    return aux

def dividir(vector1,vector2):

    #print(type(vector2))
    x=vector1.x/vector2.x
    y=vector1.y/vector2.y
    z=vector1.z/vector2.z
    aux=vector(x,y,z)
    return aux

def escalarPorVector(vec, escalar):
    aux=vector(0,0,0)
    x=vec.x*escalar
    y=vec.y*escalar
    z=vec.z*escalar
    aux=vector(x, y, z)
    return aux

def proyeccion(vector1, vector2):

    escalar=vector1.x+vector2.x
    escalar=escalar+(vector1.y+vector2.y)
    escalar=escalar+(vector1.z+vector2.z)
    cuadrado=sqrt( (pow(vector2.x,2))+  (pow(vector2.y,2)) +  (pow(vector2.z,2))  )

    pro=escalar/cuadrado
    pro=pro*vector2

    return pro