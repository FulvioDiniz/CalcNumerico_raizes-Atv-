import numpy as np
import math
from BuscaIncremental import busca_incremental
from BuscaIncremental import funcao
#Realizado por Fulvio Diniz Santos
valor_parada = 0.00001

def bissecao(a, b, funcao):
    global num_interacao
    num_interacao = 0
    if(funcao(a) * funcao(b) > 0):
        print("Não existe raiz no intervalo")
        return None
    else:
        while (abs(b-a) > valor_parada):
            num_interacao += 1
            x = (a+b)/2
            if(funcao(a) * funcao(x) < 0):
                b = x
            else:
                a = x
        return num_interacao, x

print("numero de interacao e raiz: ", bissecao(1.002, 2, funcao))










