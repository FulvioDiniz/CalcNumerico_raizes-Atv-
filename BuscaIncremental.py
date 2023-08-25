#Realizado por Fulvio Diniz Santos
import numpy as np
import math

intervalos = np.linspace(1.002, 2, 100)

def funcao(x):
    return 2*math.log(x-1) + 3
    
    
def busca_incremental(intervalos, funcao):
    for i in range (1,len(intervalos)):
        if(funcao(intervalos[i]) * funcao(intervalos[i-1]) < 0):
            print("Existe uma raiz entre esse intervalo ",round(intervalos[i-1], 4), " e ", round(intervalos[i], 4))
            
busca_incremental(intervalos, funcao)