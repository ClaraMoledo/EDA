import numpy as np  
import matplotlib.pyplot as plt

def f(x):
    return x**3 + x - 2 

def metodo_bissecao (f, a, b, precisao):
    if f(a) * f(b) >= 0:
        return "Não existe raiz no intervalo"
    
    iteracoes = []
    iteracao = 0
    erro = b - a
    
    while erro > precisao:
        iteracao += 1
        m = ( a + b ) / 2  
        