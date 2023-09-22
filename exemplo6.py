import math

def f(x):
   return (x**5/3) - x**4 + x + 1

def golden_ratio_search(a, b, epsilon):
    phi = (1 + math.sqrt(5)) / 2
    x1 = b - (b - a) / phi
    x2 = a + (b - a) / phi

    while abs(b - a) > epsilon:
        if f(x1).real < f(x2).real:
            a = x1
            x1 = x2
            x2 = a + (b - a) / phi
        else:
            b = x2
            x2 = x1
            x1 = b - (b - a) / phi

    return (a + b) / 2

max_value = golden_ratio_search(-1, 1.5, 10e-8)
print("Feito por Fulvio Diniz Santos")
print("O valor máximo da função é:", max_value)
