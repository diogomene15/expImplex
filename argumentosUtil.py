# Diogo de Lima Menezes e Marcos Vinicius Medeiros
import sys


class Args:

  def __init__(self):
    self.inc = 0
    self.fim = 0
    self.stp = 0
    self.rpt = 0
    self.carregarArgs()

  def checarArg(self, argInteiro, errMsg):
    if (not argInteiro.isdigit() or int(argInteiro) <= 0):
      print(errMsg)
      exit()

  def carregarArgs(self):
    args = sys.argv[1:]
    if len(args) % 2 != 0:
      print("Número de argumentos inválido")
      exit()
    if ("--inc" in args):
      self.inc = args[args.index("--inc") + 1]
      self.checarArg(
        self.inc,
        "o tamanho inicial dos vetores deve ser um número inteiro > 0")
    else:
      self.inc = input("Insira o tamanho inicial dos vetores: ")
      self.checarArg(
        self.inc,
        "o tamanho inicial dos vetores deve ser um número inteiro > 0")

    if ("--fim" in args):
      self.fim = args[args.index("--fim") + 1]
      self.checarArg(
        self.fim,
        "o tamanho final dos vetores (fim) deve ser um número inteiro > 0")
    else:
      self.fim = input("Insira o tamanho final dos vetores: ")
      self.checarArg(
        self.fim,
        "o tamanho final dos vetores (fim) deve ser um número inteiro > 0")

    if ("--stp" in args):
      self.stp = args[args.index("--stp") + 1]
      self.checarArg(
        self.stp,
        "o tamanho de intervalo entre os vetores (stp) deve ser um número inteiro > 0"
      )
    else:
      self.stp = input("Insira o tamanho de intervalo entre os vetores: ")
      self.checarArg(
        self.stp,
        "o tamanho de intervalo entre os vetores (stp) deve ser um número inteiro > 0"
      )
    if ("--rpt" in args):
      self.rpt = args[args.index("--rpt") + 1]
      self.checarArg(
        self.rpt,
        "o numero de repeticoes (rpt) deve ser um número inteiro > 0")
    else:
      self.rpt = input("Insira o número de repetições: ")
      self.checarArg(
        self.rpt,
        "o numero de repeticoes (rpt) deve ser um número inteiro > 0")
    self.inc = int(self.inc)
    self.fim = int(self.fim)
    self.stp = int(self.stp)
    self.rpt = int(self.rpt)
