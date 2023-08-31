import random
import time
from ordenacaoUtil import *

def medirTempo(metodo, vetor, ini = None, fim = None):
    vetorCopia = vetor.copy()
    params = []

    if(ini == None and fim == None):
        params = [vetorCopia]
    else:
        params = [vetorCopia, ini, fim]
    
    inicioT = time.time()
    metodo(*params)
    fimT = time.time()
    return fimT - inicioT

def geraVetor(tam):
    vetor = []
    for _ in range(1, tam+1):
        vetor.append(random.randint(0, 99999999))
    return vetor


def iniciar(inc,fim,stp,rpt):
    resultados = []
    tamanhosVetores = range(inc, fim+1, stp)
    for _ in range(rpt):
        for tam in tamanhosVetores:
            resultadoVetor = [tam]
            vetor = geraVetor(tam)
            resultadoVetor.append(medirTempo(mergeSort, vetor, 0, len(vetor)-1))
            print(resultadoVetor)
iniciar(10, 10000, 1000, 2)