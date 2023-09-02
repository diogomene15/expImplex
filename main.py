import sys
import experimentosUtil
from argumentosUtil import Args
sys.setrecursionlimit(1000000000) # para evitar o erro de recursão no quicksort com vetores grandes ordenados

inc = 0
fim = 0
stp = 0
rpt = 0

args = Args()
experimentosUtil.iniciar(args.inc, args.fim, args.stp, args.rpt)
