import numpy as np
import pandas as pd

df=pd.read_excel('TablaCapitales.xlsx', header=None)

datos=df.to_numpy()

class Cromosoma:
    def __init__(self, recorrido=0, distancia=0):
        self.recorrido=recorrido
        self.totalDist=distancia
        self.fitness=0
    
    def getRecorrido(self):
        return self.recorrido

    def setRecorrido(self, recorrido):
        self.recorrido = recorrido
    
    def getDistancia(self):
        return self.totalDist

    def setDistancia(self, dist):
        self.totalDist=dist
    
    def generarRecorrido(self, startingCity):
        recorrido=np.array([], dtype=int)
        for i in range(24):
            recorrido=np.append(recorrido, i+1)
        
        recorrido=np.random.permutation(recorrido)
        recorrido=np.delete(recorrido, np.where(recorrido==startingCity))
        recorrido=np.insert(recorrido, 0, startingCity)
        recorrido=np.append(recorrido, startingCity)

        return recorrido

    def calcularDistancia(self):
        sum=0
        for i in range(len(self.recorrido)-1):
            sum += int(datos[self.recorrido[i], self.recorrido[i+1]])
        return sum
    
    def setFitness(self, fitness):
        self.fitness=fitness

    def getFitness(self):
        return self.fitness

    def imprimirRecorrido(self):
        print('El recorrido es: ')
        for i in self.recorrido:
            print(datos[0, i])
            print('')
        
        print('Distancia total: ', self.totalDist)