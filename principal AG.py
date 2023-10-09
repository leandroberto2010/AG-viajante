import Cromosoma as crom
import Logic as logic
import numpy as np
import copy as cp

ciclos=200
cantPob=50
mutRate=0.05
crossRate=0.30
minimos=[]
maximos=[]

def start():
    poblacion=logic.generarPoblacion(cantPob, 1)
    logic.evaluarPoblacion(poblacion)
    logic.save_data(maximos, minimos, poblacion)
    for i in range(ciclos):
        if i==10:
            print("100 ciclos")
        if i==199:
            print('breaking')
        nuevaPoblacion=np.array([])
        while len(nuevaPoblacion)<len(poblacion):
            padres=cp.deepcopy(logic.ruleta(poblacion))
            nuevaPoblacion=np.append(nuevaPoblacion, logic.crossover(padres, crossRate, mutRate))
        logic.evaluarPoblacion(nuevaPoblacion)
        poblacion=np.array([])
        poblacion=np.append(poblacion, (cp.deepcopy(nuevaPoblacion)))
        logic.save_data(maximos, minimos, poblacion)

    poblacion[0].imprimirRecorrido()

    logic.graficar(maximos, minimos)

start()