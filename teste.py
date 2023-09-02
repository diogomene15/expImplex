import random
import time
def selectionSort(lista):
   for i in range(len(lista)-1, 0, -1):
       posicao=0
       for local in range(1, i+1):
           if lista[local] > lista[posicao]:
               posicao = local

       posicaoTroca = lista[i]
       lista[i] = lista[posicao]
       lista[posicao] = posicaoTroca

def geraVetorAleatorio(tam):
    vetor = []
    for _ in range(1, tam+1):
        vetor.append(random.randint(1, tam*4))
    return vetor

lista = geraVetorAleatorio(20000)

inicioT = time.perf_counter()
selectionSort(lista)
fimT = time.perf_counter()

print(fimT - inicioT)