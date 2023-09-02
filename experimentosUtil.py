import random
import time
import copy
from ordenacaoUtil import *

def medirTempo(metodo, vetor, ini=None, fim=None):
  vetorCopia = vetor.copy()
  params = [vetorCopia, ini, fim]
  params = [p for p in params if p != None]

  inicioT = time.perf_counter()
  metodo(*params)
  fimT = time.perf_counter()
  return fimT - inicioT


def geraVetorAleatorio(tam):
  vetor = []
  for _ in range(1, tam + 1):
    vetor.append(random.randint(1, tam * 4))
  return vetor


def desordenaVetor(vetor, porcentagemDesordem=10):
  tamVetor = len(vetor)
  numItemsDesordem = int(porcentagemDesordem / 100 * tamVetor)
  indicesDesordenados = random.sample(range(tamVetor), numItemsDesordem)
  for indiceDes in indicesDesordenados:
    novoIndice = random.randint(0, tamVetor - 1)
    temp = vetor[novoIndice]
    vetor[novoIndice] = vetor[indiceDes]
    vetor[indiceDes] = temp


def geraVetores(tam):
  vetorAleatorio = geraVetorAleatorio(tam)
  vetorOrdemCresc = vetorAleatorio[:]
  vetorOrdemCresc.sort()
  vetorReverso = vetorAleatorio[:]
  vetorReverso.sort(reverse=True)
  vetorQuaseOrdenado = vetorOrdemCresc[:]
  desordenaVetor(vetorQuaseOrdenado)
  return {
    "aleatorio": vetorAleatorio,
    "crescente": vetorOrdemCresc,
    "reverso": vetorReverso,
    "quaseOrdenado": vetorQuaseOrdenado
  }


def media(vetor):
  return sum(vetor) / len(vetor)


def imprimirResultados(resultados):
  for tipoVetor, valoresTipoVetor in resultados.items():
    print(f"[ [{tipoVetor}] ]")
    print("n\t\tSelection\tInsertion\tMerge\t\tHeap\t\tQuick\t\tCounting")
    print(
      "---------------------------------------------------------------------------"
    )
    for tam, valoresTam in valoresTipoVetor.items():
      print(f"{tam}\t\t", end="")
      for nomeOrd, valOrd in valoresTam.items():
        print("{0:.6f}\t".format(valOrd), end="")
      print()
    print("\n")


def iniciar(inc, fim, stp, rpt):
  modeloResultado = {}
  tamanhosVetores = range(inc, fim + 1, stp)
  for tam in tamanhosVetores:
    modeloResultado[tam] = {}
    for nomeOrd in ordenadores:
      modeloResultado[tam][nomeOrd] = []
  resultados = {
    "aleatorio": copy.deepcopy(modeloResultado),
    "crescente": copy.deepcopy(modeloResultado),
    "reverso": copy.deepcopy(modeloResultado),
    "quaseOrdenado": copy.deepcopy(modeloResultado)
  }

  for tam in tamanhosVetores:
    for _ in range(rpt):
      vetoresTeste = geraVetores(tam)
      for nomeTipoVetor, vetor in vetoresTeste.items():
        for nomeOrd, metodoOrd in ordenadores.items():
          params = []
          if (nomeOrd == "mergeSort" or nomeOrd == "quickSort"):
            params = [metodoOrd, vetor, 0, len(vetor) - 1]
          elif (nomeOrd == "countingSort"):
            params = [metodoOrd, vetor, max(vetor)]
          else:
            params = [metodoOrd, vetor]
          resultados[nomeTipoVetor][tam][nomeOrd].append(medirTempo(*params))
  for tipoVetor in resultados:
    for tam in tamanhosVetores:
      for nomeOrd in ordenadores:
        vetorTempoOrd = resultados[tipoVetor][tam][nomeOrd]
        resultados[tipoVetor][tam][nomeOrd] = sum(vetorTempoOrd) / rpt
  imprimirResultados(resultados)
  return (resultados)
