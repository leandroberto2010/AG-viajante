import numpy as np
import Cromosoma

def generarPoblacion(cantidad, startingCity):
    poblacion=np.array([], dtype=int)
    for i in range(cantidad):
        cromosoma=Cromosoma()
        cromosoma.setRecorrido(cromosoma.generarRecorrido(startingCity))
        cromosoma.setDistancia(cromosoma.calcularDistancia())
        poblacion=np.append(poblacion, cromosoma)
    return poblacion

def evaluarPoblacion(poblacion):
    for p in poblacion:
        total+= p.getDistancia()
    for p in poblacion:
        p.setFitness(p.getDistancia()/total)
    poblacion.sort(key=lambda x: x.fitness)

def crossover(padres, mutRate, crossRate):
    r1=padres[0].getRecorrido()
    r2=padres[1].getRecorrido()

    if np.random.random()<crossRate:
        return padres
    else:
    
        hijo1=Cromosoma()
        hijo2=Cromosoma()
        hijo1.setRecorrido(np.full_like(r1, -1)) #lleno hijo1 de -1, con longitud de padre 1
        hijo2.setRecorrido(np.full_like(r2, -1)) #lleno hijo2 de -1, con longitud de padre 2

        h1=hijo1.getRecorrido()
        h2=hijo2.getRecorrido()
        puntoInicio=np.random.randint(len(r1)-1)
        puntoActual=puntoInicio

        while True:
            h1[puntoActual] = r1[puntoActual]
            puntoActual=np.where(r1==r2[puntoActual][0][0])#Los [0][0] estan para que me devuelva el primer valor, y no un array de valores de tamaño 1
            if puntoActual==puntoInicio:
                break
        
        puntoActual=puntoInicio

    #Repito para hijo2
        while True:
            h2[puntoActual] = r2[puntoActual]
            puntoActual=np.where(r2==r1[puntoActual][0][0])
            if puntoActual==puntoInicio:
                break
        
    #Reemplazo los valores -1 por los valores que tienen los padres en cada hijo usando el padre opuesto
        for i in range(len(r1)-1):
            if h1[i]==-1:
                h1[i]=r2[i]
            
            if h2[i]==-1:
                h2[i]=r1[i]
        
        hijo1.setRecorrido(h1)
        hijo2.setRecorrido(h2)

        hijo1.setDistancia(hijo1.calcularDistancia())
        hijo2.setDistancia(hijo2.calcularDistancia())

        if np.random.random()>mutRate:
            mutacion(hijo1)
        if np.random.random()>mutRate:
            mutacion(hijo2)
        
        return hijo1, hijo2


def mutacion(cromosoma):
    pos1=np.random.randint(len(cromosoma.getRecorrido())-1)
    pos2=np.random.randint(len(cromosoma.getRecorrido())-1)

    m1=cromosoma.getRecorrido()
    
    #Intercambio dos valores aleatorios de lugar
    temp=m1[pos1]
    m1[pos1]=m1[pos2]
    m1[pos2]=temp

    cromosoma.setRecorrido(m1)
    cromosoma.setDistancia(cromosoma.calcularDistancia())

def ruleta(poblacion):
    padres=[]
    while len(padres)<2:
        acum = 0   
        peso = np.random.random()
        for ind in poblacion:
            acum += ind.getFitness()
            if acum >= peso:
                padres.append(ind)
                break
    return padres