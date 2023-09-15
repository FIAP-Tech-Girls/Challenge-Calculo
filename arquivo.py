'''
Demonstração da aplicação de derivadas relacionadas ao trânsito, abordado em Python.
Nesta demonstração, levamos em conta uma lista de posições de um veículo em intervalos 
de tempo igualmente espaçados, para calcular a velocidade e aceleração instantâneas em
um determinado ponto da trajetória. Segue o exemplo:
'''
import numpy as np

# Dados de tempo (em segundos)
tempo = np.array([0, 1, 2, 3, 4, 5])

# Dados de posição (em metros)
posicao = np.array([0, 10, 20, 35, 50, 70])

# Calcular a velocidade usando a derivada da posição em relação ao tempo
velocidade = np.gradient(posicao, tempo)

# Calcular a aceleração usando a derivada da velocidade em relação ao tempo
aceleracao = np.gradient(velocidade, tempo)

# Escolha um ponto específico no tempo para análise (por exemplo, t = 3 segundos)
tempo_analise = 3
indice_tempo_analise = np.abs(tempo - tempo_analise).argmin()

# Resultados para o tempo de análise
print("Tempo:", tempo[indice_tempo_analise], "s")
print("Posição:", posicao[indice_tempo_analise], "m")
print("Velocidade:", velocidade[indice_tempo_analise], "m/s")
print("Aceleração:", aceleracao[indice_tempo_analise], "m/s^2")
