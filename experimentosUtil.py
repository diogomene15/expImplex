import random
import time
from ordenacaoUtil import *

def medirTempo(metodo, vetor, ini = None, fim = None):
    vetorCopia = vetor.copy()
    params = [vetorCopia, ini, fim]
    params = [ p for p in params if p != None]
    
    inicioT = time.perf_counter()
    metodo(*params)
    fimT = time.perf_counter()
    return fimT - inicioT

def geraVetorAleatorio(tam):
    vetor = []
    for _ in range(1, tam+1):
        vetor.append(random.randint(1, tam*4))
    return vetor


def iniciar(inc,fim,stp,rpt):
    resultAleatorio = []
    resultOrdemCrescente = []
    resultOrdemDecrescente = []
    resultQuaseOrdenado = []

    tamanhosVetores = range(inc, fim+1, stp)
    
    for _ in range(rpt):
        
        for tam in tamanhosVetores:
            for nomeOrd, metodoOrd in ordenadores.items():
                resultadoVetor = [tam]
                vetorAleatorio = geraVetorAleatorio(tam)
                params = []
                if(nomeOrd == "mergeSort" or nomeOrd == "quickSort"):
                    params = [metodoOrd, vetorAleatorio, 0, len(vetorAleatorio)-1]
                elif(nomeOrd == "countingSort"):
                    params = [metodoOrd, vetorAleatorio, max(vetorAleatorio)]
                else:
                    params = [metodoOrd, vetorAleatorio]
                resultadoVetor.append(medirTempo(*params))
                resultadoVetor.append(nomeOrd)
                print(resultadoVetor)

iniciar(10000, 100000, 10000, 1)