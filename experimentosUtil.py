import random
def geraVetor(tam):
    vetor = []
    for _ in range(1, tam+1):
        vetor.append(random.randint(0, 99999999))
    return vetor


def iniciar(inc,fim,stp,rpt):
    tamanhosVetores = range(inc, fim+1, stp)
    for tam in tamanhosVetores:
        vetor = geraVetor(tam)
        print(vetor)

iniciar(10, 100, 10, 1)