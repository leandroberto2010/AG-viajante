import numpy as np
import pandas as pd

df=pd.read_excel('TablaCapitales.xlsx', header=None)

datos=df.to_numpy()

class Cromosoma:
    
    def __init__(self, startingCity):
        self.totalDist=self.calcularDistancia()
        self.recorrido=self.generarRecorrido(startingCity)
    
    def generarRecorrido(self, startingCity):
        recorrido=np.array([], dtype=int)
        for i in range(24):
            recorrido=np.append(recorrido, i+1)
        
        recorrido=np.random.permutation(recorrido)
        recorrido=np.delete(recorrido, np.where(recorrido==startingCity))
        recorrido=np.insert(recorrido, 0, startingCity)

        return recorrido

    def calcularDistancia(self):
        for i in range(self.recorrido.size-1):
            sum += datos[self.recorrido[i], self.recorrido[i+1]]