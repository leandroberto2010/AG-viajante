import Cromosoma as crom
import Logic as logic
import numpy as np
import copy as cp

ciclos=1000
cantPob=50
mutRate=0.05
crossRate=0.30
minimos=[]
maximos=[]
nuevaPoblacion=[]
metodo='ruleta'
startingCity=20

def start():
    poblacion=cp.deepcopy(logic.generarPoblacion(cantPob, startingCity))
    logic.evaluarPoblacion(poblacion)
    logic.save_data(maximos, minimos, poblacion)
    for i in range(ciclos):
        nuevaPoblacion.clear()
        while len(nuevaPoblacion)<len(poblacion):
            if (metodo=='torneo'):
                padres=cp.deepcopy(logic.torneo(poblacion))
            else:
                padres=cp.deepcopy(logic.ruleta(poblacion))
            hijos=cp.deepcopy(logic.crossover(padres, crossRate, mutRate))
            for ind in hijos:
                nuevaPoblacion.append(cp.deepcopy(ind))
        logic.evaluarPoblacion(nuevaPoblacion)
        poblacion.clear()
        for ind in nuevaPoblacion:
            poblacion.append(cp.deepcopy(ind))
        logic.save_data(maximos, minimos, poblacion)

    poblacion[0].imprimirRecorrido()

    logic.graficar(maximos, minimos)

start()