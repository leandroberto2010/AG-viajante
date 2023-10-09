import Cromosoma as crom
import Logic as logic
import numpy as np

ciclos=200
cantPob=50
mutRate=0.05
crossRate=0.30

poblacion=logic.generarPoblacion(cantPob, 1)
logic.evaluarPoblacion(poblacion)
for i in range(ciclos):
    nuevaPoblacion=np.array([])
    while len(nuevaPoblacion)<len(poblacion):
        padres=logic.ruleta(poblacion)
        nuevaPoblacion=np.append(nuevaPoblacion, logic.crossover(padres, crossRate, mutRate))
    logic.evaluarPoblacion(nuevaPoblacion)
    poblacion=nuevaPoblacion

poblacion[0].imprimirRecorrido()