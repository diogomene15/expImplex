Alunos: Diogo de Lima Menezes e Marcos Vinicius Medeiros
---------------------------------------------------------

argumentosUtil.py - realiza a leitura e validação dos 
argumentos de execução dos experimentos.

experimentosUtil.py - reúne métodos responsáveis pela
geração de objetos, vetores, acionamento de funções de
ordenação e organização de informações

ordenacaoUtil.py - arquivo que contém funções responsáveis
pela realização da ordenação dos vetores utilizados como
entradas dos experimentos

main.py - arquivo principal da aplicação de experimentos.
Aciona função 'iniciar' (experimentosUtil.py) que inicia
os experimentos.


Na pasta 'graficosGnu', encontram-se os arquivos .data e
.plt utilizados para geração dos gráficos contidos no re-
latório de resultados (relatorio.pdf). Bem como os próprios
gráficos em si. Todos em formato .png.

---------------------------------------------------------

Professor, realizaram-se vários testes com os algoritmos aqui
contidos. Há apenas um caso que nos causa receio de erro: in-
compatibilidade da função 'sys.setrecursionlimit(1000000000)'
, utilizada no no arquivo principal para prevenir erros rela-
cionados à grande quantidade de chamadas recursivas no quick sort,
no caso de vetores ordenados (ascendentemente ou descendentemente).

Pensou-se sobre a utilização de processamento paralelo, para lidar
com a lentidão inerente ao python, mas resolveu-se por evitar, para
, justamente, previnir mais qualquer outra possibilidade de erro.

Aliás, vale ressalter essa lentidão. Muito provavelmente, em outro
trabalho semenlhante, não optaríamos pelo desenvolvimento com python.
Pois, embora fácil, flexível e rica, foi um fator que nos levou a
vários minutos esperando por uma rodade de experimentos. Fizemos alguns
testes com C - e até com Cython - e a diferença, embora linear, é
extremamente significativa (para nós, humanos apressados).

---------------------------------------------------------
GitHub da aplicação: https://github.com/diogomene15/expImplex
---------------------------------------------------------

Agradecemos pela atenção.

Diogo de Lima Menezes e Marcos Vinicius Medeiros.

