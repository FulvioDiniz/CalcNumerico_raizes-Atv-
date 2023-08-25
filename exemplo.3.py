#Realizado por Fulvio Diniz Santos
import math
valor_parada = 0.00001
def funcao(x):
    return 2*math.log(x-1) + 3

def subintervalo_falsaposicao(a, b, funcao):   
    x = (a * funcao(b) - b * funcao(a)) / (funcao(b) - funcao(a))    
    if abs(funcao(x)) < valor_parada:
        return x    
    if funcao(a) * funcao(x) < 0:
        return subintervalo_falsaposicao(a, x, funcao)
    else:
        return subintervalo_falsaposicao(x, b, funcao)

a = subintervalo_falsaposicao(1.002, 2, funcao)
print("subintervalo:",a)
