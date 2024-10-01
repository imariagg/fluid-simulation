from visual import *
from ClaseParticula import *
#from OperacionesVectoriales import *

def calculaVecinosHash(listaParticulas,h):
    n = listaParticulas.getNumParticulas()
    #print('Numero de particulas' +str(n))
    nh = prime(2*n)
    hash_table = {}

    #Prueba
    #a=listaParticulas.getParticula(2)
    #print(a.getPosicion())

    #Anadimos cada particula asociada a su correspondiente clave    
    for i in range(n):
        #print(i)
        p=listaParticulas.getParticula(i)
        r = p.getPosicion()
        #print(r)
        rUnit = rUnitario(r,h)
        #print(rUnit)
        key = hash(rUnit,nh)
        
        #if(hash_table.has_key(key)):
        if(key in hash_table):
            hash_table[key].append(p)
        else:
            hash_table[key] = [p]
    #Por cada particula, calculamos sus limites MAX y MIN e iteramos sobre
    #cada posicion discreta, asociando a P las particulas asociadas a esas posiciones
    
    for i in range(n):
        listaVecinas = []      
        p=listaParticulas.getParticula(i)
        rQ = p.getPosicion()
        rUnit = rUnitario(rQ,h) 
        rMin = rQ - (h,h,h)
        rMax = rQ + (h,h,h)
        
        #Calculamos los limites
        BBMin = rUnitario(rMin,h)
        BBMax = rUnitario(rMax,h)
        #Iteramos sobre las direcciones entre posMin y posMax
        i = BBMin.x
        j = BBMin.y
        k = BBMin.z
        while i < (BBMax.x+1):
            while j < (BBMax.y+1):
                while k < (BBMax.z+1):
                    key = hash(vector(i,j,k),nh)
                    #if(hash_table.has_key(key)):
                    if(key in hash_table):
                        for elem in hash_table[key]:
                            if(listaVecinas.count(elem)==0 and elem!=p):#asegura que no esta en la lista de vecinas y que no es la misma particula
                                d = mag(elem.getPosicion()-p.getPosicion())
                                if d < h:
                                    listaVecinas.append(elem)
                    k = k + 1
                k = BBMin.z
                j = j + 1
            k = BBMin.z
            j = BBMin.y
            i = i + 1
        #p.setListaVecinas(listaVecinas)#<---adaptar a vuestro proyecto
        p.setVecinas(listaVecinas)#<---adaptar a vuestro proyecto
        #listaParticulas.setSistemaParticulas(listaVecinas)


   
def prime(x):
    i = x
    while(isPrime(i)== false):
        i=i+1
    return i

def isPrime(number):
    if number<=1 or number%2==0:
        return 0
    check=3
    maxneeded=number
    while check<maxneeded+1:
        maxneeded=number/check
        if number%check==0:
            return 0
        check+=2
    return 1

def hash(rUnit,nh):    
    p1 = 73856093
    p2 = 19349663
    p3 = 83492791
    return math.fmod((int(rUnit.x*p1) ^ int(rUnit.y*p2) ^ int(rUnit.z*p3)),nh)

def rUnitario(r,h):
    i = int(math.floor(r.x/h))
    j = int(math.floor(r.y/h))
    k = int(math.floor(r.z/h))
    return vector(i,j,k)
