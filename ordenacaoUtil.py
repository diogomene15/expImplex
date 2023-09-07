# Diogo de Lima Menezes e Marcos Vinicius Medeiros
def selectionSort(lista):
  for i in range(len(lista) - 1, 0, -1):
    posicao = 0
    for local in range(1, i + 1):
      if lista[local] > lista[posicao]:
        posicao = local

    posicaoTroca = lista[i]
    lista[i] = lista[posicao]
    lista[posicao] = posicaoTroca


def insertionSort(lista):
  Tam_a = len(lista)

  for j in range(1, Tam_a):
    chave = lista[j]

    i = j - 1
    while i >= 0 and lista[i] > chave:
      lista[i + 1] = lista[i]

      i = i - 1
    lista[i + 1] = chave


def _merge(lista, inicio, meio, fim):
  l1 = meio - inicio + 1
  l2 = fim - meio
  Nl = []
  Nr = []
  for i in range(0, l1):
    Nl.append(lista[inicio + i])

  for j in range(0, l2):
    Nr.append(lista[meio + 1 + j])

  i = 0
  j = 0
  k = inicio

  while i < l1 and j < l2:
    if Nl[i] <= Nr[j]:
      lista[k] = Nl[i]
      i += 1
    else:
      lista[k] = Nr[j]
      j += 1
    k += 1

  while i < l1:
    lista[k] = Nl[i]
    i += 1
    k += 1

  while j < l2:
    lista[k] = Nr[j]
    j += 1
    k += 1


def mergeSort(lista, inicio, fim):
  if inicio < fim:
    meio = (inicio + fim) // 2
    mergeSort(lista, inicio, meio)
    mergeSort(lista, meio + 1, fim)
    _merge(lista, inicio, meio, fim)


def _partition(lista, inicio, fim):
  x = lista[fim]
  i = inicio - 1
  temp = None
  j = inicio
  while j < fim:
    if lista[j] <= x:
      i += 1
      temp = lista[i]
      lista[i] = lista[j]
      lista[j] = temp
    j += 1
  temp = lista[i + 1]
  lista[i + 1] = lista[fim]
  lista[fim] = temp
  return i + 1


def quickSort(lista, inicio, fim):
  if inicio >= fim:
    return
  a = _partition(lista, inicio, fim)
  quickSort(lista, inicio, a - 1)
  quickSort(lista, a + 1, fim)


def _heapify(lista, n, ini):
  maior = ini
  esq, dir = 2 * ini + 1, 2 * ini + 2

  if esq< n and lista[esq] > lista[maior]:
      maior = esq

  if dir < n and lista[dir] > lista[maior]:
      maior = dir

  if maior != ini:
      temp = lista[ini]
      lista[ini] = lista[maior]
      lista[maior] = temp
      ini = maior
  else:
      return;

def heapSort(lista):
  n = len(lista)
  for i in range(n // 2 - 1, -1, -1):
      _heapify(lista, n, i)
  for i in range(n - 1, 0, -1):
      temp = lista[i]
      lista[i] = lista[0]
      lista[0] = temp
      _heapify(lista, i, 0)


def countingSort(lista, maior):
  tamanho = len(lista)
  saida = [0] * tamanho
  contador = [0] * (maior + 1)

  for num in lista:
    contador[num] += 1

  for i in range(1, maior + 1):
    contador[i] += contador[i - 1]

  for num in reversed(lista):
    saida[contador[num] - 1] = num
    contador[num] -= 1

  lista[:] = saida


ordenadores = {
  "selectionSort": selectionSort,
  "insertionSort": insertionSort,
  "mergeSort": mergeSort,
  "heapSort": heapSort,
  "quickSort": quickSort,
  "countingSort": countingSort
}
